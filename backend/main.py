from fastapi import FastAPI

app = FastAPI(
    title="CyberShield AI",
    description="AI-Powered Cybersecurity Intelligence Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "CyberShield AI Backend Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }