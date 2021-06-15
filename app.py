from sqlalchemy import create_engine
import streamlit as st
import pandas as pd
from datetime import datetime
import re 
import socket 
st.set_page_config(
page_title="CLAYSS",
page_icon="https://clayss.org/sites/default/files/favicon2.ico",
layout="wide",
)
st.markdown("<h2 style='text-align: left; color: #00b8e1;'>Reporte de envio boletín</h2>", unsafe_allow_html=True)
buff1,buff, col = st.beta_columns([1,2,2])
with buff1:st.markdown("<a href='https://noticias.clayss.org' target='_blank'><img src='https://clayss.org/sites/default/files/logo_blanco2.png' style='width:90%;border-radius:3px;background: #FFA600;'></a>", unsafe_allow_html=True)
display_code =   buff1.radio("Mostrar", ( "Envios","Rebotes", "Suscriptores", "Buscar"))
#hostname = socket.gethostname()
#local_ip = socket.gethostbyname(hostname)
db_connection_str = 'mysql+pymysql://clayssorg_orgar_2020:anitA&2020@69.16.228.38:3306/clayssorg_noti_ext'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM watchdog where type="mail"', con=db_connection)
df2 = pd.read_sql('SELECT * FROM simplenews_subscriber', con=db_connection)
#df['Marca temporal'] = pd.to_datetime(df['Marca temporal']).dt.strftime('%d/%m/%y')
df['timestamp']=pd.to_datetime(df['timestamp'],unit='s')
df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%d/%m/%y')
#lst = re.findall('\S+@\S+', s) 
#st.write(local_ip)
df.index = [""] * len(df) 
df2.index = [""] * len(df2) 
if display_code == "Envios":
   
   buff.table(df[['message','variables','timestamp']])
if display_code == "Suscriptores":
   df5=pd.value_counts(df2['mail'].unique())
   times3t=df5.index
   aulast=len(times3t)
   with buff1:st.write("cantidad:", aulast)
   buff.table(df2['mail'].unique())
if display_code == "Buscar":
   maill=buff1.text_input('mail')
   if maill:
   
     df33=(df2[df2['mail'].str.contains(maill, regex= True)])
     buff.table(df33[['status','mail']])
   
