from fastapi import FastAPI

from src.routes.api import router

# Create the FastAPI application
app = FastAPI(
    title="Structured Extraction Service",
    description="Extract structured sustainability information from PDF reports.",
    version="1.0.0"
)

# Register all API routes
app.include_router(router)