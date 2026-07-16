from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Enterprise AI Chatbot"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Enterprise AI Chatbot Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
