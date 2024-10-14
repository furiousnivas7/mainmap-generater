import streamlit as st

def home():
    st.title("AI-Powered Mind Map Generator")
    st.write("Welcome to the AI-powered mind map generator. This app helps you create visual representations of your study notes.")

    uploaded_file = st.file_uploader("Upload your notes (txt, pdf, or audio)", type=["txt", "pdf", "mp3"])

    if uploaded_file:
        st.success("File uploaded successfully!")
        # Placeholder for processing the file
        st.write("Navigate to the 'Generate Mind Map' page to start creating a mind map.")

    if st.button("Generate Mind Map"):
        st.write("Navigate to 'Generate Mind Map' page.")
        st.experimental_rerun()
