from fastapi import APIRouter

from app.sql.analytics import (
    get_total_sales,
    compare_sales_last_3_years,
    get_highest_growth_region,
    get_quarterly_sales,
    get_top_products,
    summarize_sales_report,
    get_top_region
)

router = APIRouter()


@router.post("/chat")
def chat(payload: dict):

    question = payload.get("question", "").lower()

    if "total sales" in question and "2025" in question:
        return {
            "answer": f"Total sales for 2025: {get_total_sales(2025)}",
            "confidence": 0.95,
            "source_type": "sql",
            "sources": ["sample_sales.csv"],
            "fallback": False
        }

    if "compare sales" in question:
        return {
            "answer": str(compare_sales_last_3_years()),
            "confidence": 0.95,
            "source_type": "sql",
            "sources": ["sample_sales.csv"],
            "fallback": False
        }

    if "highest growth" in question:
        return {
            "answer": f"Highest growth region: {get_highest_growth_region()}",
            "confidence": 0.95,
            "source_type": "sql",
            "sources": ["sample_sales.csv"],
            "fallback": False
        }

    if "quarterly sales" in question:
        return {
            "answer": str(get_quarterly_sales()),
            "confidence": 0.95,
            "source_type": "sql",
            "sources": ["sample_sales.csv"],
            "fallback": False
        }

    if "products contributed most" in question or "top products" in question:
        return {
            "answer": str(get_top_products()),
            "confidence": 0.95,
            "source_type": "sql",
            "sources": ["sample_sales.csv"],
            "fallback": False
        }

    if "summarize" in question and "sales report" in question:
        return {
            "answer": summarize_sales_report(),
            "confidence": 0.95,
            "source_type": "sql",
            "sources": ["sample_sales.csv"],
            "fallback": False
        }

    if (
        "highest region" in question
        or "top region" in question
        or "highest revenue" in question
    ):
        result = get_top_region()

        return {
            "answer": f"{result['region']} generated {result['revenue']} revenue",
            "confidence": 0.95,
            "source_type": "sql",
            "sources": ["sample_sales.csv"],
            "fallback": False
        }

    return {
        "answer": "Question not supported yet.",
        "confidence": 0.30,
        "source_type": "fallback",
        "sources": [],
        "fallback": True
    }
