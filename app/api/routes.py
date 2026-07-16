from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
def chat(payload: dict):

    question = payload.get("question", "")

    return {
        "answer": f"You asked: {question}",
        "confidence": 0.95,
        "source_type": "demo",
        "sources": [
            "sample_sales.csv"
        ],
        "fallback": False
    }
