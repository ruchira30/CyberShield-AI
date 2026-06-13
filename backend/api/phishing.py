from fastapi import APIRouter

router = APIRouter(
    prefix="/phishing",
    tags=["Phishing Detection"]
)

@router.post("/predict")
def detect_phishing(email_text: str):
    return {
        "email": email_text,
        "prediction": "safe",
        "confidence": 0.95
    }