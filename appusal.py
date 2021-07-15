import streamlit as st


import smtplib
import ssl
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
buff1,buff, col = st.beta_columns([2,2,2])
# specify the correct name of the Google Sheet
sheet = gclient.open('noticiasclayssf').worksheet('datos')
sheet2 = gclient.open('noticiasclayssf').worksheet('envios')


#insert on the next available row
#st.write(next_row)
#sheet2.update_acell("A{}".format(next_row), v+1)
# Get all values in the Google Sheet
row_values_list = sheet.get_all_records()

# specify email and GMail App Password
from_email = 'pruebas@clayss.org'
password = 'pruebas2021'
st.sidebar.markdown('<img style="float: left;width:100%;margin-top:-40px;" src="https://noticias.clayss.org/sites/default/files/logo.png" />', unsafe_allow_html=True)
display_code =   st.sidebar.radio("Mostrar", ( "Enviar boletín","No enviados", "Enviados"))
today = date.today()

hoy2=today.strftime('%d-%m-%y')
    #SHEET_ID = '12D4hfpuIkT7vM69buu-v-r-UYb8xx4wM1zi-34Fs9ck'
data=pd.read_csv('https://docs.google.com/spreadsheets/d/1TlT34mRvnvhilrY1PfKt-K6tvhKtfdID0fTYJc3CuBw/export?format=csv')
data=data.sort_values(by=['orden'],ascending=False)
# Create the pandas DataFrame
#df0 = pd.DataFrame(data, columns=['Webinar', 'Planilla'])

values = data['newsletter'].tolist()
options = data['imagen'].tolist()

dic = dict(zip(options, values))

if display_code == 'Enviar boletín':
   a = buff1.selectbox('Seleccionar boletín:', options, format_func=lambda x: dic[x])

   news=data["newsletter"].loc[data["imagen"] == a].to_string(index = False)
   orden2=data["orden"].loc[data["imagen"] == a].to_string(index = False)



#reunion = data['newsletter'] ==a
#data=data.sort_values(by=['orden'],ascending=True)
   imagen=str(data.iloc[-1]['imagen'])
   news0=str(data.iloc[-1]['newsletter'])


# iterate on every row of the Google Sheet
if display_code=='Enviar boletín':
    #st.write(news)
    st.markdown ('<!DOCTYPE html><html><body><a href="https://noticias.usal.edu.ar"><img  width="800" src="'+a+'" /></a></body></html>', unsafe_allow_html=True)
    data = data=pd.read_csv('https://docs.google.com/spreadsheets/d/1TlT34mRvnvhilrY1PfKt-K6tvhKtfdID0fTYJc3CuBw/export?format=csv&gid=91437221')
    df0 = pd.DataFrame(data, columns=['nombre', 'base'])
    df0=df0.sort_values(by=['nombre'],ascending=True)
    values = df0['nombre'].tolist()
    options = df0['base'].tolist()
    dic = dict(zip(options, values))
    a = st.sidebar.selectbox('Seleccionar base:', options, format_func=lambda x: dic[x])
    sheet = gclient.open('noticiasclayssf').worksheet(a)
    if st.sidebar.button('Enviar'):
      for row_value in row_values_list:

  # we are dealing with dictionary, so you can use get method
        name = row_value.get('name')
        token = str(row_value.get('token'))
        to_email = row_value.get('Email')


  # specify the path to your html email
        html = '''<div id="message-content">
			
			<div class="rightcol" role="region" aria-labelledby="aria-label-messagebody">
			
				<div id="message-objects">


				<div id="messagebody"><div class="message-htmlpart" id="message-htmlpart1"><!-- html ignored --><!-- head ignored --><!-- meta ignored -->
<style type="text/css">#message-htmlpart1 div.rcmBody table tr td {
  font-family: Arial;
  font-size: 12px}</style>


<div class="rcmBody">
<div>
  <table width="800px" cellpadding="0" cellspacing="0">
    <tbody><tr>
      <td>
        <div style="padding: 0px 0px 0px 0px">






<style type="text/css">#message-htmlpart1 div.rcmBody html,#message-htmlpart1 div.rcmBody,#message-htmlpart1 div.rcmBody table,#message-htmlpart1 div.rcmBody tbody,#message-htmlpart1 div.rcmBody tr,#message-htmlpart1 div.rcmBody td,#message-htmlpart1 div.rcmBody div,#message-htmlpart1 div.rcmBody p,#message-htmlpart1 div.rcmBody ul,#message-htmlpart1 div.rcmBody ol,#message-htmlpart1 div.rcmBody li,#message-htmlpart1 div.rcmBody h1,#message-htmlpart1 div.rcmBody h2,#message-htmlpart1 div.rcmBody h3,#message-htmlpart1 div.rcmBody h4,#message-htmlpart1 div.rcmBody h5,#message-htmlpart1 div.rcmBody h6 {
margin: 0;
padding: 0}

#message-htmlpart1 div.rcmBody {
-ms-text-size-adjust: 100%;
-webkit-text-size-adjust: 100%}

#message-htmlpart1 div.rcmBody table {
border-spacing: 0;
mso-table-lspace: 0pt;
mso-table-rspace: 0pt}

#message-htmlpart1 div.rcmBody table td {
border-collapse: collapse}

#message-htmlpart1 div.rcmBody h1,#message-htmlpart1 div.rcmBody h2,#message-htmlpart1 div.rcmBody h3,#message-htmlpart1 div.rcmBody h4,#message-htmlpart1 div.rcmBody h5,#message-htmlpart1 div.rcmBody h6 {
font-family: 'Google sans', Verdana}

#message-htmlpart1 div.rcmBody .v1ExternalClass {
width: 100%}

#message-htmlpart1 div.rcmBody .v1ExternalClass,
#message-htmlpart1 div.rcmBody .v1ExternalClass p,
#message-htmlpart1 div.rcmBody .v1ExternalClass span,
#message-htmlpart1 div.rcmBody .v1ExternalClass font,
#message-htmlpart1 div.rcmBody .v1ExternalClass td,
#message-htmlpart1 div.rcmBody .v1ExternalClass div {
line-height: 100%}


#message-htmlpart1 div.rcmBody .v1ReadMsgBody {
width: 100%}

#message-htmlpart1 div.rcmBody img {
-ms-interpolation-mode: bicubic;
border:1px solid #f15c24}

#message-htmlpart1 div.rcmBody .v1titu{
    font-family:'Google sans', Verdana;
 font-size: 18px;
    color: #2c3850;
    font-weight: 600;
    line-height: 20px;
 mso-line-height: exactly;
  margin: 0;
text-align: left;
border-bottom: 2px solid #e65100;
height:80px;
    padding: 9px}
#message-htmlpart1 div.rcmBody .v1titup{
    font-family:'Google sans', Verdana;
 font-size: 24px;
    color: #2c3850;
    font-weight: 500;
    line-height: 20px;
 mso-line-height: exactly;
  margin: 0;
text-align: left;
border-bottom: 2px solid #e65100;
height:80px;
    padding: 9px}
#message-htmlpart1 div.rcmBody .v1leer{
    color: #fff!important;
    font-family: 'Google sans', Verdana;
    font-size: 12px;
    
    line-height: 14px;
    text-align: right;
    padding: 8px;
    letter-spacing: normal;
    border: 0px none;
    border-radius: 5px;
    border-collapse: separate!important;
    background-color: #e65100;
text-align:right}
#message-htmlpart1 div.rcmBody .v1fecha{
    font-family:'Google sans', Verdana;
font-size:12px;
color:#989fa7;
text-align:right;
padding-top:5px;
padding-bottom:3px;
border-bottom:1px solid #eeeeee}
#message-htmlpart1 div.rcmBody .v1cate{
    font-family:'Google sans', Verdana;
font-size:14px;
color:#e65100;
text-align:right;
padding-top:5px;
font-weight: 500}
#message-htmlpart1 div.rcmBody .v1cuerpo{

font-family:'Google sans', Verdana;
font-size:14px;
color:#2c3850;
line-height:18px;
text-align:justify;
padding:5px;
margin-bottom:10px;
height:80px}

#message-htmlpart1 div.rcmBody #v1icon-expand-des {
    position: absolute;
  
    color: #e65100;
    z-index: 8;
    font-size: 28px}
#message-htmlpart1 div.rcmBody #v1icon-expand-des img{

    border:0}</style>


<style type="text/css">#message-htmlpart1 div.rcmBody a[x-apple-data-detectors=true]{
color: inherit !important;
text-decoration: inherit !important}

#message-htmlpart1 div.rcmBody u + #v1body a {
color: inherit;
text-decoration: inherit !important;
font-size: inherit;
font-family: inherit;
font-weight: inherit;
line-height: inherit}

#message-htmlpart1 div.rcmBody a, #message-htmlpart1 div.rcmBody a:link, #message-htmlpart1 div.rcmBody .v1no-detect-local a, #message-htmlpart1 div.rcmBody .v1appleLinks a {
color: inherit !important;
text-decoration: inherit}</style>


<style type="text/css">#message-htmlpart1 div.rcmBody .v1width800 {
width: 800px;
max-width: 100%}

@media all and (max-width: 799px) {
#message-htmlpart1 div.rcmBody .v1width800 {
width: 100% !important}
}

@media screen and (min-width: 600px) {
#message-htmlpart1 div.rcmBody .v1hide-on-desktop {
display: none !important}
}

@media all and (max-width: 599px),
#message-htmlpart1 div.rcmBody only screen and (max-device-width: 599px) {
#message-htmlpart1 div.rcmBody .v1main-container {
width: 100% !important}

#message-htmlpart1 div.rcmBody .v1col {
width: 100%}

#message-htmlpart1 div.rcmBody .v1fluid-on-mobile { 
width: 100% !important;
height: auto !important;
 
text-align:center}

#message-htmlpart1 div.rcmBody .v1fluid-on-mobile img {
width: 100% !important}

#message-htmlpart1 div.rcmBody .v1hide-on-mobile { 
display:none !important;
 
width:0px !important;
height:0px !important;
 
overflow:hidden;
 
}
}</style>






<div class="rcmBody" id="v1body" marginwidth="0" marginheight="0" offset="0" style="font-family: 'Google sans', Verdana, sans-serif; font-size: 0px; margin: 0; padding: 0">

<style type="text/css">@media screen and (min-width: 600px) {
#message-htmlpart1 div.rcmBody .v1hide-on-desktop {
display: none}
}

@media all and (max-width: 599px) {
#message-htmlpart1 div.rcmBody .v1hide-on-mobile { 
display:none !important;
 
width:0px !important;
height:0px !important;
 
overflow:hidden;
 
}
#message-htmlpart1 div.rcmBody .v1main-container {
width: 100% !important}
#message-htmlpart1 div.rcmBody .v1col {
width: 100%}

#message-htmlpart1 div.rcmBody .v1fluid-on-mobile { 
width: 100% !important;
height: auto !important;
 
text-align:center}

#message-htmlpart1 div.rcmBody .v1fluid-on-mobile img {
width: 100% !important}
}</style>

<table cellpadding="0" cellspacing="0" border="0" width="100%" style="border: 2px solid #571d0f">
<tbody><tr>
<td width="100%">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tbody><tr>
<td align="center" width="100%">

<table class="v1width800 v1main-container" cellpadding="0" cellspacing="0" border="0" width="100%" style="max-width: 800px">
<tbody><tr>
<td width="100%">

<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tbody><tr>

<td valign="top">
<table cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#ffffff" style="background-color: #ffffff">
<tbody><tr>

<td valign="top" style="padding: 5px"><table cellpadding="0" cellspacing="0" border="0" width="100%" class="v1mcol">
<tbody><tr>
<td valign="top" style="padding: 0; mso-cellspacing: 0in">


<table cellpadding="0" cellspacing="0" border="0" width="100%" class="v1col" align="left">
<tbody><tr>
<td valign="top" width="100%" style="padding: 0">
<table cellpadding="0" cellspacing="0" border="0" width="100%" class="v1col" align="left">
<tbody><tr>
<td valign="top" width="100%" style="padding: 0">

<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tbody><tr>
<td valign="top" style="padding-top: 20px; padding-right: 0px; padding-bottom: 10px; padding-left: 0px">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tbody><tr>

<td valign="top" style="padding: 5px"><div style="font-family: 'Google sans', Verdana; font-size: 18px; color: #2c3850; font-weight: 500; line-height: 22px; padding: 0; margin: 0; text-align: center">CONVOCATORIA-Acompañamiento Virtual a Instituciones</div>
</td>

</tr>
</tbody></table>

<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tbody><tr>

<td style="padding: 5px; border-bottom: 1px solid #f15c24">
<table cellpadding="0" cellspacing="0" border="0" width="100%" style="border-top: 1px solid #">
<tbody><tr>

<td style="font-size: 0px; line-height: 0">&nbsp;
</td>
</tr>
</tbody></table>

</td>
</tr>
</tbody></table>

</td>

</tr>
</tbody></table>

</td>
</tr>
</tbody></table>
<table cellpadding="0" cellspacing="0" border="0" width="100%" >
<tbody><tr>

<td align="left" style="padding: 20px" valign="top"><div style="font-family: 'Google sans', Verdana; font-size: 14px; color: #2c3850;  line-height: 22px; padding: 0; margin: 0; text-align: left">
        <div>
          <p>Desde el Programa de apoyo a instituciones educativas solidarias &quot;Aprendizaje-Servicio Solidario en las Artes&quot;, CLAYSS convoca a instituciones de todos los niveles y modalidades de <b>Argentina, Brasil, Colombia y Perú</b> a participar del &quot;Acompañamiento Virtual a Instituciones (AVI) 2021&quot;. </p><br>
          <p>Desde el 22 de junio al 30 de julio de 2021 está abierta la convocatoria para participar del <b>AVI2021</b>. Pueden participar completando el formulario que se encuentra en <a href="https://www.tfaforms.com/4913545" target="_blank">https://www.tfaforms.com/4913545</a>. </p><br>
          <p>Bases y condiciones: https://bit.ly/3vSJMM7
            
            Para más información sobre el Programa &quot;AYSS en las Artes&quot;: <a href="https://programas.artes.clayss.org/es/bienvenidos_arte" target="_blank">https://programas.artes.clayss.org/es/bienvenidos_arte</a></p><br>
        </div>
      </div><br><a href="https://www.tfaforms.com/4913545" target="_blank"><img src="https://noticias.clayss.org/mails/convocatoria2021.jpg" style="width: 100%; text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; display: block" /></a></td>
</tr>
</tbody></table>

</td>
</tr>
</tbody></table>


<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tbody><tr>
<td align="center" width="100%">

<table class="v1width800 v1main-container" cellpadding="0" cellspacing="0" border="0" width="100%" style="max-width: 800px">
<tbody><tr>
<td width="100%">

<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tbody><tr>

<td valign="top">
<table cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#ffffff" style="background-color: #ffffff">
<tbody><tr>

<td valign="top" style="padding-top: 20px; padding-right: 20px; padding-bottom: 10px; padding-left: 20px"><table cellpadding="0" cellspacing="0" border="0" width="100%" class="v1mcol">
<tbody><tr>
<td valign="top" style="padding: 0; mso-cellspacing: 0in">




<table cellpadding="0" cellspacing="0" border="0" width="100%" class="v1col" align="left">
<tbody><tr>
<td valign="top" width="100%" style="padding: 0">

<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tbody><tr>

</tr></tbody></table><table cellpadding="0" cellspacing="0" border="0" width="100%">
<tbody><tr>

<td align="center"><div>
<img style="width: 99%; text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; display: block" src="https://noticias.clayss.org/sites/default/files/inline-images/piem.png" usemap="#Map">
</div></td>
</tr>
</tbody></table>
</td></tr>
</tbody></table>

</td>
</tr>
</tbody></table>


</td>
</tr>
</tbody></table>
</td>
</tr>
</tbody></table>

</td>
</tr>
</tbody></table>

</td>
</tr>
</tbody></table>

</td>
</tr>
</tbody></table>

</div></div></td>
</tr>
</tbody></table><div style="color: #555555; line-height: 1.2; padding: 10px"></div> 
</div></div></div> <map name="Map">
  <area shape="rect" coords="27,131,162,161" href="https://www.clayss.org.ar" target="_blank" rel="noreferrer">
  <area shape="rect" coords="551,138,582,168" href="https://www.facebook.com/CLAYSSDIGITAL/" target="_blank" rel="noreferrer">
  <area shape="rect" coords="595,137,622,168" href="https://www.instagram.com/clayssdigital/" target="_blank" rel="noreferrer">
  <area shape="rect" coords="640,142,663,165" href="https://twitter.com/clayssdigital" target="_blank" rel="noreferrer">
  <area shape="rect" coords="678,137,704,159" href="https://www.youtube.com/user/clayssdigital" target="_blank" rel="noreferrer">
  <area shape="rect" coords="722,140,750,161" href="https://www.linkedin.com/company/centro-latinoamericano-de-aprendizaje-y-servicio-solidario/" target="_blank" rel="noreferrer">
  <area shape="rect" coords="763,139,787,164" href="#v1">
 </map>
</div>

























        
      
    
  


</div>
</div>'''#.join(open('path/to/your/html').readlines())
  
  # replace the variables with the values in the sheet
  #html = html.replace('${name}', name)
  #html = html.replace('${token}', token)
  
  # set up from, to and subject
        message = MIMEMultipart('alternative')
        message['Subject'] = news
        message['From'] = from_email
        message['To'] = to_email
  

        part1 = MIMEText(html, 'html')
  

        message.attach(part1)
  

        context = ssl.create_default_context()
  
     
    
        with smtplib.SMTP_SSL('mail.clayss.org', 465) as server:
          server.login(from_email, password)
          from email_validator import validate_email, EmailNotValidError 
          try:

              valid = validate_email(to_email)


          except EmailNotValidError as e:
            
            str_list = list(filter(None, sheet2.col_values(1)))
    
            next_row = sheet2.cell(str(len(str_list)), 1).value 

            sheet2.append_row([hoy2,a,to_email,news, 'No enviada; mal nombre de dominio'])
            continue
          from validate_email import validate_email
          is_valid = validate_email(email_address=to_email, check_format=True)
          
          if is_valid==True or is_valid==None:
                        
            str_list = list(filter(None, sheet2.col_values(1)))
    
            next_row = sheet2.cell(str(len(str_list)), 1).value 
            server.sendmail(from_email, to_email, message.as_string())
            sheet2.append_row([ hoy2,a,to_email,news, 'enviada'])
       
          else:
                        
            str_list = list(filter(None, sheet2.col_values(1)))
    
            next_row = sheet2.cell(str(len(str_list)), 1).value 
            sheet2.append_row([hoy2,a,to_email,news, 'No enviada; mal nombre en la cuenta'])
      st.sidebar.write(news+' Enviada')
if display_code == "No enviados":
  #buff1.markdown("<h5>Envio</h5>", unsafe_allow_html=True)
  datan=pd.read_csv('https://docs.google.com/spreadsheets/d/1TlT34mRvnvhilrY1PfKt-K6tvhKtfdID0fTYJc3CuBw/export?format=csv&gid=70901914')
  #datan['fecha'] = pd.to_datetime(datan['fecha']).dt.strftime('%d/%m/%y')
  datan=datan.sort_values(by=['orden'],ascending=False)
  countries = datan['fecha'].unique()
  country = buff1.selectbox('Envio Viernes:', countries)
  options = ['enviada'] 
  datan = datan.loc[~datan['estado'].isin(options)]

  datan.index = [""] * len(datan)
  datanu=datan['fecha'] == country
  #newdf = datan[(datan.fecha == countries)]
  #st.write(datan.filter(items=['orden2']))
  #datanu=datan['orden2'] == orden2  


  dupli=datan[datanu].drop_duplicates(subset = ['destinatario'])
  #dupli['fecha52'] = pd.to_datetime(dupli['fecha']).dt.strftime('%d/%m/%y')
  #st.markdown(datan.index.tolist())
  #st.dataframe(dupli)
  #ag_grid(dupli[['Fecha','Destinatario','Newsletter', 'Estado']])
  
  #AgGrid(dupli[['fecha','newsletter','destinatario','estado']])
  st.dataframe(dupli[['fecha','newsletter','base','destinatario','estado']])

  df5=pd.value_counts(dupli['destinatario']) 
  times3t=df5.index
  aulast=len(times3t) 
  st.sidebar.write('No enviados:',aulast) 
  #dupli.index = [""] * len(dupli) 
  #st.table(dupli)
if display_code == "Enviados":
  datan=pd.read_csv('https://docs.google.com/spreadsheets/d/1TlT34mRvnvhilrY1PfKt-K6tvhKtfdID0fTYJc3CuBw/export?format=csv&gid=70901914')
  #datan['fecha'] = pd.to_datetime(datan['fecha']).dt.strftime('%d/%m/%y')
  datan=datan.sort_values(by=['orden'],ascending=False)
  #buff1.markdown("<h5>Envio</h5>", unsafe_allow_html=True)
  countries = datan['fecha'].unique()
  country = buff1.selectbox('Envio Viernes:', countries)
  options = ['No enviada; mal nombre de dominio','No enviada; mal nombre en la cuenta'] 
  # selecting rows based on condition 
  datan = datan.loc[~datan['estado'].isin(options)]
  datan.index = [""] * len(datan)
  datanu=datan['fecha'] == country
  dupli=datan[datanu].drop_duplicates(subset = ['destinatario'])
  #dupli['fecha52'] = pd.to_datetime(dupli['fecha']).dt.strftime('%d/%m/%y')
  #dupli.index = [""] * len(dupli) 
  #st.markdown(datan.index.tolist())
  #st.dataframe(dupli)
  #st.table(dupli[['fecha','newsletter','destinatario','estado']])
  st.dataframe(dupli[['fecha','newsletter','base','destinatario','estado']])
  df5=pd.value_counts(dupli['destinatario']) 
  times3t=df5.index
  aulast=len(times3t) 
  st.sidebar.write('No enviados:',aulast) 
