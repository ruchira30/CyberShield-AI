from fastapi import APIRouter
from api.endpoints.phishing import router as phishing_router
from api.endpoints.url import router as url_router
from api.endpoints.ddos import router as ddos_router

router = APIRouter()

@router.get("/")
def home():
    return {"message": "CyberShield AI Running"}

@router.get("/health")
def health():
    return {"status": "healthy"}

router.include_router(phishing_router)
router.include_router(url_router)
router.include_router(ddos_router)