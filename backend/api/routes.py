from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {"message": "CyberShield AI Running"}

@router.get("/health")
def health():
    return {"status": "healthy"}