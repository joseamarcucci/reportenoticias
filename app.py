from sqlalchemy import create_engine
import streamlit as st
import pandas as pd

db_connection_str = 'mysql+pymysql://usal_orientate:pablO&2020@69.16.228.38:3306/usal_noticiasok'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM config', con=db_connection)
st.table(df)
