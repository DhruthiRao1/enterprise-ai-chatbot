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

    return {
        "answer": "Question not supported yet.",
        "confidence": 0.30,
        "source_type": "fallback",
        "sources": [],
        "fallback": True
    }
