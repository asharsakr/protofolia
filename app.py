import streamlit as st
import base64

# Encode image
with open("ashar.jpg", "rb") as f:
    img_base64 = base64.b64encode(f.read()).decode()

# Read HTML
with open("Ashar_Salama_Portfolio.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace image src with base64
html_content = html_content.replace(
    'src="ashar.jpg"',
    f'src="data:image/jpeg;base64,{img_base64}"'
)

st.set_page_config(page_title="Ashar Salama Portfolio", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .stApp { background-color: #ffffff !important; }
        header[data-testid="stHeader"] { display: none !important; }
        .block-container { padding: 0 !important; max-width: 100% !important; }
    </style>
""", unsafe_allow_html=True)

st.components.v1.html(html_content, height=8000, scrolling=False)
