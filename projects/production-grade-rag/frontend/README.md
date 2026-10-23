# Production RAG Assistant — Frontend

A responsive React chat interface prototype for the Production RAG App.

## Run locally

```bash
npm install
npm run dev
```

Open the local URL printed by Vite.

## Modes

- **Demo stream**: streams sample UI content locally. It does not query ChromaDB or an LLM.
- **Backend stream**: sends `POST /api/chat/stream` with JSON `{ "message": "..." }` and expects a streaming text response.

The backend mode is a contract placeholder. The Python backend must expose the matching endpoint, and the frontend may need a Vite proxy or a full API URL depending on how the services are run.

## Important

The displayed demo source cards are illustrative and explicitly labelled as demo sources. They are not retrieved from your knowledge base. Connect source metadata from your backend before presenting real citations.
