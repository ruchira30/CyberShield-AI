from fastapi import FastAPI

from api.routes import router as base_router
from api.phishing import router as phishing_router
from api.url import router as url_router
from api.ddos import router as ddos_router

app = FastAPI(
    title="CyberShield AI",
    version="1.0.0"
)

app.include_router(base_router)
app.include_router(phishing_router)
app.include_router(url_router)
app.include_router(ddos_router)