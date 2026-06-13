from fastapi import FastAPI

from api.routes import router as base_router

app = FastAPI(
    title="CyberShield AI",
    version="1.0.0"
)

app.include_router(base_router)