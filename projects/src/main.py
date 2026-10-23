from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from src.retrieval import retrieve_and_rerank
from src.generation import generate_answer

app = FastAPI(title="Production RAG API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def health_check():
    return {"status": "running", "message": "Production RAG API is ready"}


@app.post("/api/chat/stream")
def chat_stream(request: ChatRequest):
    question = request.message.strip()

    if not question:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    try:
        passages = retrieve_and_rerank(question)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Document retrieval failed. Check the backend logs.",
        ) from exc

    def stream_response():
        try:
            for token in generate_answer(question, passages):
                yield token
        except Exception:
            yield "\n\n[Error: Answer generation failed. Check backend logs.]"

    return StreamingResponse(
        stream_response(),
        media_type="text/plain; charset=utf-8",
    )
