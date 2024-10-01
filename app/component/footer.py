import streamlit as st

# Function to create the footer
@st.cache_data
def footer():
    st.markdown("""
    <footer style="position:fixed; left:0; bottom:0; width:100%; background-color:#333; color:white; text-align:center; padding:10px; border-radius:5px">
        © 2024 My StreamKing App
    </footer>
    """, unsafe_allow_html=True)