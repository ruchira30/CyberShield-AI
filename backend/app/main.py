#Import FastAPI
from fastapi import FastAPI
#Create an instance of FastAPI
app = FastAPI(
    title="CyberShield AI",
    description = "Cybersecurity AI backend API",
    version="1.0.0"
)
#Define a route endpoint
@app.get("/") #Define GET request for the root endpoint
def home():
    return {"message": "App is running!"} #Return a JSON response indicating the app is running

# Define a health check endpoint to verify that the API is operational
@app.get("/health")
def health():
    return {"status": "ok"}