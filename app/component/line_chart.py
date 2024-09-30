import streamlit as st
import pandas as pd
import plotly.express as px

def line_chart():
    data = pd.DataFrame({
        'X': range(1, 11),
        'Y': [2, 4, 3, 6, 5, 7, 6, 8, 9, 10]
    })
    fig = px.line(data, x='X', y='Y', title='Sample Line Chart')
    st.plotly_chart(fig)