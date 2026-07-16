import streamlit as st
import requests

API_URL = "http://localhost:8000/chat"

st.set_page_config(
    page_title="Enterprise AI Assistant",
    page_icon="🤖"
)

st.title("🤖 Enterprise AI Assistant")

question = st.text_input(
    "Ask a question",
    placeholder="Show total sales for 2025"
)

if st.button("Submit"):

    response = requests.post(
        API_URL,
        json={
            "question": question
        }
    )

    if response.status_code == 200:

        result = response.json()

        st.success("Response Generated")

        st.write(
            result["answer"]
        )

        st.write(
            f"Confidence: {result['confidence']}"
        )

        st.write(
            f"Source Type: {result['source_type']}"
        )

        st.write(
            "Sources:"
        )

        for source in result["sources"]:
            st.write(source)

    else:
        st.error(
            "API Error"
        )
