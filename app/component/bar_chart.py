import streamlit as st
import pandas as pd
import plotly.express as px
from app.connection.connector import snowflake_connector as sc

@st.cache_data
def bar_chart():
    query = "SELECT * FROM ACCOUNT_USAGE.ACCESS_HISTORY LIMIT 1;"
    access_history_columns = sc().sql(query).columns

    data = pd.DataFrame({
        'Category': access_history_columns,
        'Value': [12, 32, 22, 5, 42,21,90,75,4,26]
    })
    fig = px.bar(data, x='Category', y='Value', title='Sample Bar Chart')
    print(222)
    st.plotly_chart(fig)