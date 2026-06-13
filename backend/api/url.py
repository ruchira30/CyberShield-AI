from fastapi import APIRouter

router = APIRouter(
    prefix="/url",
    tags=["Malicious URL Detection"]
)

@router.post("/predict")
def detect_url(url: str):
    return {
        "url": url,
        "prediction": "malicious",
        "confidence": 0.89
    }