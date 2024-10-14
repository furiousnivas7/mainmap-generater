import streamlit as st
from pages import home, generate_mindmap, customize_mindmap, previous_mindmaps, settings

# Sidebar for navigation
st.sidebar.title("Mind Map Generator")
# Define the `page` variable here with a selectbox for page navigation
page = st.sidebar.selectbox("Choose a page", ["Home", "Generate Mind Map", "Customize Mind Map", "Previous Mind Maps", "Settings"])

# Page routing
if page == "Home":
    home.home()
elif page == "Generate Mind Map":
    generate_mindmap.generate_mindmap()
elif page == "Customize Mind Map":
    customize_mindmap.customize_mindmap()
elif page == "Previous Mind Maps":
    previous_mindmaps.previous_mindmaps()
elif page == "Settings":
    settings.settings()
