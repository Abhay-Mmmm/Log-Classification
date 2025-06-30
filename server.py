import streamlit as st
from classify import classify_log

st.title("Log Classifier")

source = st.text_input("Log Source", "")
log_message = st.text_area("Log Message", "")

if st.button("Classify Log"):
    if log_message.strip():
        label = classify_log(source, log_message)
        st.success(f"Predicted Label: {label}")
    else:
        st.warning("Please enter a log message.")
