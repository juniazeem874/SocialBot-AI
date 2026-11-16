from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SocialBot AI API",
    version="0.1.0",
    description="API for AI reel creation and social publishing.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return {"status": "ok", "service": "socialbot-ai-api"}


@app.get("/api/v1")
async def api_root():
    return {
        "name": "SocialBot AI",
        "version": "0.1.0",
        "status": "scaffold",
    }
