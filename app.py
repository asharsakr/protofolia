import streamlit as st

st.set_page_config(
    page_title="Ashar Salama Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI elements and force white background
st.markdown("""
    <style>
        #root > div:nth-child(1) > div > div > div > div > section > div {
            padding: 0 !important;
        }
        .stApp {
            background-color: #ffffff !important;
        }
        header[data-testid="stHeader"] {
            display: none !important;
        }
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        iframe {
            display: block;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

with open("Ashar_Salama_Portfolio.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=8000, scrolling=False)
