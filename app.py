from mysql.connector import (connection)
from mysql.connector.network import MySQLTCPSocket
import os
import re
import streamlit as st
import pandas as pd
import socket
import socks
st.set_page_config(
page_title="CLAYSS",
page_icon="https://clayss.org/sites/default/files/favicon2.ico",
layout="wide",
)
st.markdown("<h2 style='text-align: left; color: #00b8e1;'>Reporte de envio boletín</h2>", unsafe_allow_html=True)
buff1,buff, col = st.beta_columns([1,2,2])
with buff1:st.markdown("<a href='https://noticias.clayss.org' target='_blank'><img src='https://clayss.org/sites/default/files/logo_blanco2.png' style='width:90%;border-radius:3px;background: #FFA600;'></a>", unsafe_allow_html=True)
display_code =   buff1.radio("Mostrar", ( "Envios","Rebotes", "Suscriptores", "Buscar"))
os.environ['QUOTAGUARDSHIELD_URL']="http://ei6z5sz4ag4ds7:ehfv7imkeokiydd85aa2cun7lih@us-east-static-07.quotaguard.com:9293"
try:
    QG_ENVVAR=os.environ['QUOTAGUARDSHIELD_URL']
    #"http://ei6z5sz4ag4ds7:ehfv7imkeokiydd85aa2cun7lih@us-east-static-07.quotaguard.com:9293" = os.environ['QG_ENVVAR']
except KeyError:
    try:
        QG_ENVVAR = os.environ['http://ei6z5sz4ag4ds7:ehfv7imkeokiydd85aa2cun7lih@us-east-static-07.quotaguard.com:9293']
    except KeyError:
        print("Missing QUOTAGUARDSTATIC_URL and QUOTAGUARDSHIELD_URL. Exiting")
        exit(1)

QG_PORT = 1080
QG_USER, QG_PASS, QG_HOST = re.split(r"[:@\/]", QG_ENVVAR)[3:-1]

PATCH = True

def monkey_patch_open_connection(self):
    """Open the TCP/IP connection to the MySQL server
    """
    # Get address information
    addrinfo = [None] * 5
    try:
        addrinfos = socket.getaddrinfo(self.server_host,
                                       self.server_port,
                                       0, socket.SOCK_STREAM,
                                       socket.SOL_TCP)
        # If multiple results we favor IPv4, unless IPv6 was forced.
        for info in addrinfos:import streamlit as st
import smtplib
import ssl
import streamlit.components.v1 as components
import datetime
import requests
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
        .css-17eq0hr {
    background-color: #fff;
    background-attachment: fixed;
    border-right:2px solid #008357;
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
    border: 1px solid #dedede;
}
    </style>
""", unsafe_allow_html=True) 

#st.sidebar.markdown("<h2 style='text-align: left; color: #00b8e1;'>Envio de Noticias</h2>", unsafe_allow_html=True)
buff1,buff, col = st.beta_columns([1,2,2])
# specify the correct name of the Google Sheet
sheet = gclient.open('noticiasusal').worksheet('datos')
sheet2 = gclient.open('noticiasusal').worksheet('envios')
# Get all values in the Google Sheet
row_values_list = sheet.get_all_records()

# specify email and GMail App Password
from_email = 'yzur76@gmail.com'
password = 'hocwnvbdeoenagtt'
st.sidebar.markdown('<img style="float: left;width:100%;margin-top:-40px;background:#FFA600;" src="https://noticias.clayss.org/sites/default/files/logo_blanco2.png" />', unsafe_allow_html=True)
display_code =   st.sidebar.radio("Mostrar", ( "Enviar Boletín","No enviados", "Enviados"))
today = date.today()

hoy2=today.strftime('%d-%m-%y')
    #SHEET_ID = '12D4hfpuIkT7vM69buu-v-r-UYb8xx4wM1zi-34Fs9ck'
data=pd.read_csv('https://docs.google.com/spreadsheets/d/1v6hHLiNhviftzcyVP3x6RKYYsp16rNBXhFkARO1mg4k/export?format=csv')
#data=data.sort_values(by=['orden'],ascending=False)
imagen=str(data.iloc[-1]['imagen'])
news=str(data.iloc[-1]['newsletter'])
# iterate on every row of the Google Sheet
if display_code=='Enviar Boletín':


# embed streamlit docs in a streamlit app
    #components.iframe("https://noticias.clayss.org/mails/clayss.html")
    #html_string = 'https://noticias.clayss.org/mails/clayss.html' # load your HTML from disk here
    #st.markdown (html_string, unsafe_allow_html=True)
    #components.html("https://noticias.clayss.org/mails/clayss.html", width=200, height=200)
    #components.iframe("https://noticias.clayss.org/mails/clayss.html", width=800, height=900,, encoding='utf-8')
    #html_file=urllib.request.urlretrieve('clayss.html')
    HtmlFile = open(imagen,'r' ,encoding='utf-8')
    source_code = HtmlFile.read() 

    components.html(source_code, width=1000, height=5500)
    
    #st.write(news)
    
    #st.markdown (html_file, unsafe_allow_html=True)
    if st.sidebar.button('Enviar'):
      for row_value in row_values_list:

  # we are dealing with dictionary, so you can use get method
        name = row_value.get('name')
        token = str(row_value.get('token'))
        to_email = row_value.get('Email')


  # specify the path to your html email
        html = '''



'''
  
  # replace the variables with the values in the sheet
  #html = html.replace('${name}', name)
  #html = html.replace('${token}', token)
  
  # set up from, to and subject
        message = MIMEMultipart('alternative')
        message['Subject'] = news
        message['From'] = from_email
        message['To'] = to_email
  

        part1 = MIMEText(source_code, 'html')
  

        message.attach(part1)
  

        context = ssl.create_default_context()
  
     
    
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
          server.login(from_email, password)
          from email_validator import validate_email, EmailNotValidError 
          try:

              valid = validate_email(to_email)


          except EmailNotValidError as e:

            sheet2.append_row([hoy2,to_email,news, 'No enviada; mal nombre de dominio'])
            continue
          from validate_email import validate_email
          is_valid = validate_email(email_address=to_email, check_format=True)
    
          if is_valid==None:
            server.sendmail(from_email, to_email, message.as_string())
            sheet2.append_row([hoy2,to_email,news, 'enviada'])
       
          else:
            sheet2.append_row([hoy2,to_email,news, 'No enviada; mal nombre en la cuenta'])
      st.sidebar.write(news+' Enviada')
if display_code == "No enviados":
  datan=pd.read_csv('https://docs.google.com/spreadsheets/d/1v6hHLiNhviftzcyVP3x6RKYYsp16rNBXhFkARO1mg4k/export?format=csv&gid=70901914')
  datan['fecha'] = pd.to_datetime(datan['fecha']).dt.strftime('%d/%m/%y')
  datan=datan.sort_values(by=['fecha'],ascending=False)
  countries = datan['fecha'].unique()
  country = buff1.selectbox('Fecha:', countries)
  options = ['enviada'] 
  datan = datan.loc[~datan['estado'].isin(options)]
  datan.index = [""] * len(datan) 
  datanu=datan['fecha'] == country
  dupli=datan[datanu].drop_duplicates(subset = ['destinatario'])
  #st.markdown(datan.index.tolist())
  st.dataframe(dupli)
  df5=pd.value_counts(dupli['destinatario']) 
  times3t=df5.index
  aulast=len(times3t) 
  st.sidebar.write('No enviados:',aulast) 
  #dupli.index = [""] * len(dupli) 
  #st.table(dupli)
if display_code == "Enviados":
  datan=pd.read_csv('https://docs.google.com/spreadsheets/d/1v6hHLiNhviftzcyVP3x6RKYYsp16rNBXhFkARO1mg4k/export?format=csv&gid=70901914')
  datan['fecha'] = pd.to_datetime(datan['fecha']).dt.strftime('%d/%m/%y')
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
  st.dataframe(dupli)
  df5=pd.value_counts(dupli['destinatario']) 
  times3t=df5.index
  aulast=len(times3t) 
  st.sidebar.write('No enviados:',aulast) 
            if self.force_ipv6 and info[0] == socket.AF_INET6:
                addrinfo = info
                break
            elif info[0] == socket.AF_INET:
                addrinfo = info
                break
        if self.force_ipv6 and addrinfo[0] is None:
            raise errors.InterfaceError(
                "No IPv6 address found for {0}".format(self.server_host))
        if addrinfo[0] is None:
            addrinfo = addrinfos[0]
    except IOError as err:
        raise errors.InterfaceError(
            errno=2003, values=(self.get_address(), _strioerror(err)))
    else:
        (self._family, socktype, proto, _, sockaddr) = addrinfo

    # Instanciate the socket and connect
    try:
        self.sock = socks.socksocket(self._family, socktype, proto) #socket.socket(self._family, socktype, proto)
        self.sock.set_proxy(socks.SOCKS5, QG_HOST, QG_PORT, True, QG_USER, QG_PASS)
        self.sock.settimeout(self._connection_timeout)
        self.sock.connect(sockaddr)
    except IOError as err:
        raise errors.InterfaceError(
            errno=2003, values=(self.get_address(), _strioerror(err)))
    except Exception as err:
        raise errors.OperationalError(str(err))

# link in the monkey patch
if PATCH:
    MySQLTCPSocket.open_connection = monkey_patch_open_connection

if __name__ == "__main__":

    try:
        os.environ['DATABASE']='mysql://clayssorg_orgar_2020:anitA&2020@69.16.228.38:3306/clayssorg_noti_ext'
        DB_ENVVAR = os.environ['DATABASE']
        

        DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME = re.split(r"[:@\/]", DB_ENVVAR)[3:]
    except KeyError:
        print("Missing DATABASE environment variable")
        exit(1)

    print("Connecting {}:{} to {} on {}:{}".format(DB_USER, DB_PASS, DB_NAME, DB_HOST, DB_PORT))

    # test the connection
    cnx = connection.MySQLConnection(user=DB_USER, password=DB_PASS, host=DB_HOST, database=DB_NAME, port=DB_PORT)
   

#db_connection = sql.connect(host='69.16.228.38', database='clayssorg_noti_ext', user='clayssorg_orgar_2020', password='anitA&2020')
    df = pd.read_sql('SELECT * FROM watchdog where type="mail"', con=cnx)
    df.to_csv (r'C:\Usuarios\jmarcucci\export_data.csv', index = False)
    df2 = pd.read_sql('SELECT * FROM simplenews_subscriber', con=cnx)
    df3 = pd.read_sql('SELECT * FROM simplenews_mail_spool', con=cnx)
#df['Marca temporal'] = pd.to_datetime(df['Marca temporal']).dt.strftime('%d/%m/%y')
    df['timestamp']=pd.to_datetime(df['timestamp'],unit='s')
    df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%d/%m/%y')
    df3['timestamp']=pd.to_datetime(df3['timestamp'],unit='s')
    df3['timestamp'] = pd.to_datetime(df3['timestamp']).dt.strftime('%d/%m/%y')

#lst = re.findall('\S+@\S+', s) 
    
    df.index = [""] * len(df) 
    df2.index = [""] * len(df2) 
    df3.index = [""] * len(df3) 
    if display_code == "Envios":
   
        buff.table(df[['message','variables','timestamp']])
    if display_code == "Rebotes":
        df53=pd.value_counts(df3['mail'].unique())
        times53t=df53.index
        aulas5t=len(times53t)
        with buff1:st.write("rebotes:", aulas5t)
        buff.table(df3[['mail','newsletter_id','timestamp']])
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
    cursor = cnx.cursor()
    query = "SELECT SUBSTRING_INDEX(USER(),'@',-1)"

    cursor.execute(query)

    for (ip) in cursor:
        try:
            octet = "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
            match = "({}[-.]{}[-.]{}[-.]{})\.".format(octet, octet, octet, octet)
            found = re.sub(r"-", ".", re.search(match, ip[0]).group(1))

            #validate IP
            match = "({}\.{}\.{}\.{})".format(octet, octet, octet, octet)
            found = re.search(match, found).group(1)

            print("Connected via {}".format(found))
        except AttributeError:
            print("Connected, but unable to determine IP address: {}".format(ip[0]))


    cursor.close()
    cnx.close()
