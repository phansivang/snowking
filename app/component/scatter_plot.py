import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def scatter_plot():
    data = pd.DataFrame({
        'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Y': [2, 4, 3, 6, 5, 7, 6, 8, 9, 10]
    })
    fig = px.scatter(data, x='X', y='Y', title='Sample Scatter Plot')
    st.plotly_chart(fig)
