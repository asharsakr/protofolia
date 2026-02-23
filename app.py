import streamlit as st

st.set_page_config(page_title="Ashar Salama Portfolio", layout="wide")

with open("Ashar_Salama_Portfolio.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=8000, scrolling=True)