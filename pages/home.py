import streamlit as st

def home():
    st.title("AI-Powered Mind Map Generator")
    st.write("""
        Welcome to the AI-Powered Mind Map Generator. This application helps you to generate and customize mind maps 
        from your study notes, lecture files, or other sources.
    """)

    uploaded_file = st.file_uploader("Upload a text file, PDF, or audio for concept extraction", type=["txt", "pdf", "mp3"])

    if uploaded_file:
        st.success("File uploaded successfully!")
    
    if st.button("Generate Mind Map"):
        st.write("Mind Map generation will be implemented soon.")
