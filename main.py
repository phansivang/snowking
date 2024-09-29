import streamlit as st
import pandas as pd
from app.connection.connector import snowflake_connector

query = "SELECT * FROM ACCOUNT_USAGE.ACCESS_HISTORY LIMIT 50;"

snowflake_connector = snowflake_connector()

dataframe = pd.DataFrame(snowflake_connector.sql(query).collect())

st.title("Access History")
st.write(dataframe)