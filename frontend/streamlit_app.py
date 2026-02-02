import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.title("AI Data Cleaning Assistant")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    r = requests.post(f"{API}/upload", files={"file": file})
    data = r.json()
    st.success("File uploaded")
    file_id = data["file_id"]

    if st.button("Analyze"):
        res = requests.post(f"{API}/analyze", params={"file_id": file_id}).json()
        st.json(res)

    if st.button("Clean with Mean Imputation"):
        payload = {
            "file_id": file_id,
            "actions": [{"id": "simple_imputer_mean"}]
        }
        res = requests.post(f"{API}/clean", json=payload).json()
        st.success("Cleaning done")
        st.json(res)
