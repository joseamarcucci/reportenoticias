from sqlalchemy import create_engine
import streamlit as st
import pandas as pd

import re 
import socket 
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
db_connection_str = 'mysql+pymysql://clayssorg_orgar_2020:anitA&2020@69.16.228.38:3306/clayssorg_noti_ext'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM watchdog where type="mail"', con=db_connection)
#df2 = pd.read_sql('SELECT * FROM simplenews_subscriber', con=db_connection)
#s=df["variables"]
#lst = re.findall('\S+@\S+', s) 
st.write(local_ip)
st.table(df)
