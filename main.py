import streamlit as st
from app.component.footer import footer
from app.component.navbar import pages

def render_page(page):
    st.title(pages[page]["title"])
    st.write(pages[page]["description"])
    pages[page]["function"]()

def main():
    st.set_page_config(page_title="Multi-page Streamlit App", layout="wide")

    # Set default page to "Bar Chart"
    st.session_state.setdefault("page", "Bar Chart")

    # Sidebar Navigation
    st.sidebar.title("Navigation")
    for page_name in pages:
        if st.sidebar.button(page_name):
            st.session_state["page"] = page_name

    # Render selected page
    render_page(st.session_state["page"])

    # Render footer
    footer()

if __name__ == "__main__":
    main()
