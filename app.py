import streamlit as st

st.sidebar.title("Mind Map Generator")
# page = st.sidebar.selectbox("Go to", ["Home", "Generate Mind Map", "Customize Mind Map", "Previous Mind Maps", "Export & Download", "Settings"])

if page == "Home":
    import pages.home
elif page == "Generate Mind Map":
    import pages.customize_mindmap
elif page == "Customize Mind Map":
    import pages.customize_mindmap
elif page == "Previous Mind Maps":
    import pages.previous_mindmap
elif page == "Export & Download":
    import pages.export_download
elif page == "Settings":
    import pages.settings
