from sqlalchemy import create_engine
import streamlit as st
import pandas as pd
import re 
import socket 
st.markdown("<h2 style='text-align: left; color: #00b8e1;'>Reporte de envio boletín</h2>", unsafe_allow_html=True)
buff1,buff, col = st.beta_columns([1,2,2])
display_code =   buff1.radio("Mostrar", ( "Envios","Rebotes", "Suscriptores"))
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
db_connection_str = 'mysql+pymysql://clayssorg_orgar_2020:anitA&2020@69.16.228.38:3306/clayssorg_noti_ext'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM watchdog where type="mail"', con=db_connection)
df2 = pd.read_sql('SELECT * FROM simplenews_subscriber', con=db_connection)

#lst = re.findall('\S+@\S+', s) 
st.write(local_ip)
if display_code == "Envios":
   st.table(df)
if display_code == "Suscriptores":
   st.table(df2)
