import streamlit as st
import smtplib
import ssl
import altair as alt
from altair import *
from email.message import EmailMessage
import streamlit.components.v1 as components
import datetime
from bs4 import BeautifulSoup # para web scraping
import requests               # para acceder a la web
from datetime import date
# these modules will allow you to create the client and interact
# with Google Sheet
import gspread
import pandas as pd
# these modules will help you create the HTML emails
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError
# create client using credentials downloaded from Google Cloud Platform
import urllib.request
import urllib.request as url
from oauth2client.service_account import ServiceAccountCredentials
urllib.request.urlretrieve('https://entendiste.ar/mail/service_account.json',"service_account.json")
from gspread import authorize
from oauth2client.service_account import ServiceAccountCredentials
FRT = datetime.timezone(datetime.timedelta(hours=+2))
scopes = ["https://spreadsheets.google.com/feeds",
                  "https://www.googleapis.com/auth/spreadsheets",
                  "https://www.googleapis.com/auth/drive",
                  "https://www.googleapis.com/auth/drive"]
cred = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scopes)
gclient = authorize(cred)
st.set_page_config(
page_title="Envio de Boletín Clayss",
page_icon="https://noticias.clayss.org/sites/default/files/favicon.ico.png",
layout="wide",
initial_sidebar_state="expanded",
)
    #st.markdown('<img style="float: left;" src="https://virtual.usal.edu.ar/branding/themes/Usal_7Julio_2017/images/60usalpad.png" />', unsafe_allow_html=True)
st.markdown('<style>div[data-baseweb="select"] > div {text-transform: capitalize;}body{background-color:#fff;}</style>', unsafe_allow_html=True)
st.markdown(
    """<style>
        .css-5h0m38 {
    display: inline-flex;
    flex-direction: column;
    border: 2px solid rgb(246, 51, 102);
    border-radius: 3px;
}
.st-cx {
    background-color: rgb(255, 255, 255);
    border: 1px solid #dedede;
}
        .css-1l02zno {
    background-color: #fff;
    background-attachment: fixed;
    border-right:2px solid rgb(255, 166, 0);
    flex-shrink: 0;
    height: 100vh;
    overflow: auto;
    padding: 5rem 1rem;
    position: relative;
    transition: margin-left 300ms ease 0s, box-shadow 300ms ease 0s;
    width: 21rem;
    z-index: 100;
    margin-left: 0px;
}    .css-1v3fvcr {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin-top: -100px;
    overflow: auto;
    -webkit-box-align: center;
    align-items: center;
    }
    .css-qbe2hs {
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.25rem;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    text-decoration: none;
    background-color: rgb(255, 255, 255);
    border: 1px solid rgba(38, 39, 48, 0.2);
}
     .css-qbe2hs a{ text-decoration: none;}
      .st-bx {
    color: rgb(38, 39, 48);
    
}
    </style>
""", unsafe_allow_html=True) 

#st.sidebar.markdown("<h2 style='text-align: left; color: #00b8e1;'>Envio de Noticias</h2>", unsafe_allow_html=True)
buff1,buff, col = st.beta_columns([1,2,2])
# specify the correct name of the Google Sheet

sheet2 = gclient.open('noticiasclayssf').worksheet('envios')
# Get all values in the Google Sheet


# specify email and GMail App Password
from_email = 'pruebas21@clayss.org'
password = 'pruebas2021'
st.sidebar.markdown('<img style="float: left;width:100%;margin-top:-40px;" src="https://noticias.clayss.org/sites/default/files/logo.png" />', unsafe_allow_html=True)
display_code =   st.sidebar.radio("Mostrar", ( "Enviar Boletín","No enviados", "Enviados"))
today = date.today()

hoy2=today.strftime('%d-%m-%y')
    #SHEET_ID = '12D4hfpuIkT7vM69buu-v-r-UYb8xx4wM1zi-34Fs9ck'
data=pd.read_csv('https://docs.google.com/spreadsheets/d/1TlT34mRvnvhilrY1PfKt-K6tvhKtfdID0fTYJc3CuBw/export?format=csv&gid=1295007447')
#data=data.sort_values(by=['orden'],ascending=False)
imagen=str(data.iloc[-1]['imagen'])
news=str(data.iloc[-1]['newsletter'])
df01 = pd.DataFrame(data, columns=['orden','newsletter', 'imagen'])
df01=df01.sort_values(by=['orden'],ascending=False)
values1 = df01['newsletter'].tolist()
options1 = df01['imagen'].tolist()
dic = dict(zip(options1, values1))
imagen = st.sidebar.selectbox('Seleccionar boletín:', options1, format_func=lambda x: dic[x])
x = df01.loc[df01.imagen == imagen, "newsletter"]
news=x.to_list()[0]
# iterate on every row of the Google Sheet
if display_code=='Enviar Boletín':
    data = data=pd.read_csv('https://docs.google.com/spreadsheets/d/1TlT34mRvnvhilrY1PfKt-K6tvhKtfdID0fTYJc3CuBw/export?format=csv&gid=1224603731')
    df0 = pd.DataFrame(data, columns=['nombre', 'base'])
    df0=df0.sort_values(by=['nombre'],ascending=True)
    values = df0['nombre'].tolist()
    options = df0['base'].tolist()
    dic = dict(zip(options, values))
    a = st.sidebar.selectbox('Seleccionar base:', options, format_func=lambda x: dic[x])
    sheet = gclient.open('noticiasclayssf').worksheet(a)
    row_values_list = sheet.get_all_records()


# embed streamlit docs in a streamlit app
    #components.iframe("https://noticias.clayss.org/mails/clayss.html")
    #html_string = 'https://noticias.clayss.org/mails/clayss.html' # load your HTML from disk here
    #st.markdown (html_string, unsafe_allow_html=True)
    #components.html("https://noticias.clayss.org/mails/clayss.html", width=200, height=200)
    #components.iframe("https://noticias.clayss.org/mails/clayss.html", width=800, height=900,, encoding='utf-8')
    #html_file=urllib.request.urlretrieve('clayss.html')

    #HtmlFile = open(connected,'r' ,encoding='utf-8')
    #source_code = HtmlFile.read() 
    url = imagen
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, "html.parser")
    soup1=(soup.prettify())
    r = requests.get(url)


    components.html(soup1, width=1000, height=8500)

    if st.sidebar.button('Enviar'):
      for row_value in row_values_list:

  # we are dealing with dictionary, so you can use get method
        name = row_value.get('name')
        token = str(row_value.get('token'))
        to_email = row_value.get('Email')


  # specify the path to your html email
        #html = ''''''
  
  # replace the variables with the values in the sheet
  #html = html.replace('${name}', name)
  #html = html.replace('${token}', token)
  
  # set up from, to and subject

  

  

        
        msg = EmailMessage()
        msg['Subject'] = news
        msg['From'] = 'info@clayss.org'
        msg['To'] = to_email
        #msg.set_content('And it actually works')
        msg.set_content(r.text, subtype='html')
     
    
        with smtplib.SMTP_SSL('mail.clayss.org', 465) as server:
          server.login(from_email, password)
          from email_validator import validate_email, EmailNotValidError 
          try:

              valid = validate_email(to_email)


          except EmailNotValidError as e:

            sheet2.append_row([hoy2,a,to_email,news, 'No enviada; mal nombre de dominio'])
            continue
          from validate_email import validate_email
          is_valid = validate_email(email_address=to_email, check_format=True)
          
          if is_valid==True or is_valid==None:
            server.send_message(msg)
            sheet2.append_row([hoy2,a,to_email,news, 'enviada'])
       
          else:
            sheet2.append_row([hoy2,a,to_email,news, 'No enviada; mal nombre en la cuenta'])
      st.sidebar.write(news+' Enviada')
if display_code == "No enviados":
  datan=pd.read_csv('https://docs.google.com/spreadsheets/d/1TlT34mRvnvhilrY1PfKt-K6tvhKtfdID0fTYJc3CuBw/export?format=csv&gid=607365779')
  datan=datan[datan['newsletter'] == news]
  #datan['fecha'] = pd.to_datetime(datan['fecha']).dt.strftime('%d/%m/%y')
  datan=datan.sort_values(by=['fecha'],ascending=False)
  countries = datan['fecha'].unique()
  country = buff1.selectbox('Fecha:', countries)
  options = ['enviada'] 
  datan = datan.loc[~datan['estado'].isin(options)]
  datan.index = [""] * len(datan) 
  datanu=datan['fecha'] == country
  dupli=datan[datanu].drop_duplicates(subset = ['destinatario'])
  st.dataframe(dupli[['fecha','newsletter','base','destinatario','estado']])
  df2=datan.groupby(['base','estado'],as_index=False)['destinatario'].count()
  df2.index = [""] * len(df2) 
  #st.markdown(datan.index.tolist())
  st.write(df2)

  chart = Chart(df2).mark_bar().encode(
  x=alt.X('estado:N', axis=None),
  y='destinatario:Q',
  color='estado:N',
  column='base:N'
  ).properties(width=80)

  st.write(chart)
  df5=pd.value_counts(dupli['destinatario']) 
  times3t=df5.index
  aulast=len(times3t) 
  st.sidebar.write('No enviados:',aulast) 
  #dupli.index = [""] * len(dupli) 
  #st.table(dupli)
if display_code == "Enviados":
  datan=pd.read_csv('https://docs.google.com/spreadsheets/d/1TlT34mRvnvhilrY1PfKt-K6tvhKtfdID0fTYJc3CuBw/export?format=csv&gid=607365779')
  datan=datan[datan['newsletter'] == news]
  #datan['fecha'] = pd.to_datetime(datan['fecha']).dt.strftime('%d/%m/%y')
  datan=datan.sort_values(by=['fecha'],ascending=False)
  countries = datan['fecha'].unique()
  country = buff1.selectbox('Fecha:', countries)
  options = ['No enviada; mal nombre de dominio','No enviada; mal nombre en la cuenta'] 
  # selecting rows based on condition 
  datan = datan.loc[~datan['estado'].isin(options)]
  datanu=datan['fecha'] == country
  dupli=datan[datanu].drop_duplicates(subset = ['destinatario'])
  dupli.index = [""] * len(dupli) 
  #st.markdown(datan.index.tolist())
  st.dataframe(dupli[['fecha','newsletter','base','destinatario','estado']])
  df2=datan.groupby(['base','estado'],as_index=False)['destinatario'].count()
  df2.index = [""] * len(df2) 
  st.write(df2)
  chart = Chart(df2).mark_bar().encode(
    x=alt.X('estado:N', axis=None),
    y='destinatario:Q',
    color='estado:N',
    column='base:N'
  ).properties(width=80)

  st.write(chart)
  df5=pd.value_counts(dupli['destinatario']) 
  times3t=df5.index
  aulast=len(times3t) 
  st.sidebar.write('Enviados:',aulast) 
