from fastapi import APIRouter
from app.sql.analytics import (
    get_total_sales,
    get_top_region
)



router = APIRouter()


@router.post("/chat")
def chat(payload: dict):

    question = payload.get(
        "question",
        ""
    ).lower()

    # SQL Analytics Queries

    if "total sales" in question and "2025" in question:

        sales = get_total_sales(2025)

        return {
            "answer": f"Total sales for 2025: {sales}",
            "confidence": 0.95,
            "source_type": "sql",
            "sources": [
                "sample_sales.csv"
            ],
            "fallback": False
        }

    if (
        "highest region" in question
        or "top region" in question
        or "highest revenue" in question
    ):

        result = get_top_region()

        return {
            "answer":
            f"{result['region']} generated {result['revenue']} revenue",
            "confidence": 0.95,
            "source_type": "sql",
            "sources": [
                "sample_sales.csv"
            ],
            "fallback": False
        }

    # LLM Fallback

    try:

        llm_answer = ask_llm(question)

        return {
            "answer": llm_answer,
            "confidence": 0.85,
            "source_type": "llm",
            "sources": [
                "OpenAI"
            ],
            "fallback": False
        }

    except Exception as e:

        return {
            "answer": f"LLM Error: {str(e)}",
            "confidence": 0.10,
            "source_type": "error",
            "sources": [],
            "fallback": True
        }
