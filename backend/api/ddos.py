from fastapi import APIRouter

router = APIRouter(
    prefix="/ddos",
    tags=["DDoS Detection"]
)

@router.post("/predict")
def detect_ddos(packet_count: int):
    return {
        "packet_count": packet_count,
        "prediction": "normal",
        "confidence": 0.97
    }