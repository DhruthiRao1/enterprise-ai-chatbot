import streamlit as st
import requests

# Railway Backend URL
API_URL = "https://enterprise-ai-chatbot-production.up.railway.app/chat"

st.set_page_config(
    page_title="Enterprise AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Enterprise AI Chatbot")
st.markdown(
    """
    Ask business questions about sales data.
    Examples:
    - Show total sales for 2025
    - Compare sales for the last three years
    - Which region had the highest growth?
    - Show quarterly sales trends
    - Which products contributed most to revenue?
    - Summarize last year's sales report
    """
)

question = st.text_input(
    "Enter your question:",
    placeholder="Show total sales for 2025"
)

if st.button("Ask"):

    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Analyzing..."):

            try:
                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=30
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("Response Generated")

                    st.subheader("Answer")
                    st.write(result.get("answer"))

                    st.subheader("Metadata")

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.metric(
                            "Confidence",
                            result.get("confidence", 0)
                        )

                    with col2:
                        st.metric(
                            "Source Type",
                            result.get("source_type", "N/A")
                        )

                    with col3:
                        st.metric(
                            "Fallback",
                            str(result.get("fallback", False))
                        )

                    st.write("Sources:")
                    st.write(result.get("sources", []))

                else:
                    st.error(
                        f"API Error: {response.status_code}"
                    )

            except Exception as e:
                st.error(f"Error: {str(e)}")

st.divider()

st.subheader("Quick Test Questions")

sample_questions = [
    "Show total sales for 2025",
    "Compare sales for the last three years",
    "Which region had the highest growth?",
    "Show quarterly sales trends",
    "Which products contributed most to revenue?",
    "Summarize last year's sales report"
]

for q in sample_questions:
    st.write(f"• {q}")
