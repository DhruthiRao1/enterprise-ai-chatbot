from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Chatbot"
)

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
