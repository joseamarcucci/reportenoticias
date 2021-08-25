import streamlit as st
import smtplib
import altair as alt
from altair import *
import streamlit.components.v1 as components
import requests
import re
from bs4 import BeautifulSoup
import urllib.request
import urllib.request as url
import gspread
import pandas as pd
#from mailjet_rest import Client
import os 
import IPython
from oauth2client.service_account import ServiceAccountCredentials
urllib.request.urlretrieve('https://entendiste.ar/mail/service_account.json',"service_account.json")
from gspread import authorize
from oauth2client.service_account import ServiceAccountCredentials

scopes = ["https://spreadsheets.google.com/feeds",
                  "https://www.googleapis.com/auth/spreadsheets",
                  "https://www.googleapis.com/auth/drive",
                  "https://www.googleapis.com/auth/drive"]
cred = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scopes)
gclient = authorize(cred)


data = data=pd.read_csv('https://docs.google.com/spreadsheets/d/1TlT34mRvnvhilrY1PfKt-K6tvhKtfdID0fTYJc3CuBw/export?format=csv&gid=1224603731')
df0 = pd.DataFrame(data, columns=['nombre', 'base'])
df0=df0.sort_values(by=['nombre'],ascending=True)
values = df0['nombre'].tolist()
options = df0['base'].tolist()
dic = dict(zip(options, values))
#a = st.sidebar.selectbox('Seleccionar base:', options, format_func=lambda x: dic[x])
a='datos'
sheet = gclient.open('noticiasclayssf').worksheet(a)
row_values_list = sheet.get_all_records()
sentence = st.text_input('Boletín:')
if sentence:

    data = requests.get("https://noticias.clayss.org")
    soup = BeautifulSoup(data.content, 'html5lib')


    html = str(soup.find_all('a', attrs = {'href':re.compile(r'^.*\bsend\b.*$')}))
    href_start = [s.start() for s in re.finditer('href="',html)] 
    urls = []
    for start in href_start:
      url = html[start+6:]
      url = url[:url.find('"')]
      url=url.replace("//send?text=", "")
      #st.write(url)
      # remove all urls containing special characters we don't want
      if not any(c in '#?^%*()=' for c in url):
          urls.append(url)

    entradas = soup.find_all('div', {'class': 'col-lg-4'})


    previews = []
    for i, entrada in enumerate(entradas):
      
      #data = requests.get(article)

      title = entrada.find('div', {'class': 'post-title'}).getText()
      subtitle = entrada.find('div', {'class': 'post-body-term'}).getText()
      fecha = entrada.find('span', {'class': 'post-created'}).getText()
      html = str(entrada.find('a', attrs = {'href':re.compile(r'^.*\bsend\b.*$')}))
      
      url = html[start+6:]
      url = url[:url.find('"')]
      url=html.replace('/modules/share_everywhere/img/whatsapp.svg', "")
      url1=url.replace('<a data-action="share/whatsapp/share" href="//send?text=', "")
      url2=url1.replace('"><img alt="Compartir via WhatsApp"', "")
      url3=url2.replace('src=""', "")
      url4=url3.replace('title=', "")
      url4=url4.replace('"Compartir via WhatsApp"', "")
      url4=url4.replace('/>', "")
      url4=url4.replace('</a>', "")

      
      #st.write(url4)
          # remove all urls containing special characters we don't want
      if not any(c in '#?^%*()=' for c in html):
          html.append(html)
      #subtitle0 = entrada.find('div', {'class': 'v1fecha'}).contents[0]
      
      image=entrada.find('img')
      image = str(image.attrs['src']).split(" ")[0]
      image='https://noticias.clayss.org'+image

          
      entrada_preview = {
          'title': str(title),
          'subtitle': str(subtitle),
          'titulo': str(sentence),
          'boletin': url4,
          'image': str(image)
      
      }
      previews.append(entrada_preview)
    #st.write(previews)
    template = open('email_claysss_22.html')
    soup = BeautifulSoup(template.read(), "html.parser")
    article_template = soup.find('table', attrs={'class':'tablat'})
    for i,article in enumerate(previews):
      titulo = article_template.find('div', attrs={'class':'titulo'})
      titulo.string = article['titulo'][:300]
    article_template00 = soup.find_all('div', attrs={'class':'row'})
    #for i,article in enumerate(previews):
      #titulo = article_template.find('div', attrs={'class':'titulo'})
      #titulo.string = article['titulo'][:300]


    newsletter_content = ""

    for i,article_template0 in enumerate(article_template00):
    
      for i,article in enumerate(previews):
                  if i<=21:
                            
                    article_template1 = article_template0.find('div', attrs={'class':'column'+str(i)})
                    article_template = article_template1.find('div', attrs={'class':'card'})
                    html_start = str(soup)[:str(soup).find(str(article_template))]
                    html_end = str(soup)[str(soup).find(str(article_template))+len(str(article_template)):]
                    html_start = html_start.replace('\n','')
                    html_end = html_end.replace('\n','')
                    #boletin = st.text_input('Boletín?:') 
                    
                    try:
                        img = article_template.img
                        img['src'] = article['image']
                        article_template.img.replace_with(img)
                    except:
                        pass
                    
                    title = article_template.h4
                    title.string = article['title'][:300]
                    subtitle = article_template.find('div', attrs={'class':'cuerpo'})
                    subtitle.string = article['subtitle'][:100]
                  


                    #link = article_template.find('a', attrs={'class':'linko'})
                    #link['href'] = urls[i] 
                    #link.string = urls[i]
                    #link.string = article['boletin'][:300]
                    #article_template.a.replace_with(link)
                    link = article_template.find('a', attrs={'class':'linko'})
                    link['href'] = article['boletin'][:300]
                    link2 = article_template.find('a', attrs={'class':'linko2'})
                    link2['href'] = article['boletin'][:300]
                    #link.string = article['boletin'][:300]
                    #article_template.a.replace_with(link)
                    
                    newsletter_content += str(article_template).replace('\n','')
            
    

    email_content = html_start+ newsletter_content + html_end

    soup1=(BeautifulSoup(email_content).prettify())   
    components.html(soup1, width=1000, height=8500) 



    from ElasticEmailClient import ApiClient, Email

    ApiClient.apiKey = 'A0CCC58335D084934248934191EA04B70CA97E4133E1C2BC8A425E5436A34E1B6CE5A1C467D7C0B8B9968912D7043015'

    subject = 'Your subject'
    fromEmail = 'jose@entendiste.com.ar'
    fromName = 'Your Company Name'
    to='jmarcucci@usal.edu.ar'
    bodyText = 'Text body'
    bodyHtml = '<h1>Hello, {username}.</h1>'
    #files = { 'C:/Users/recipients.csv' }
    #filenameWithRecipients = 'recipients.csv' # same as the file above

    emailResponse = Email.Send(subject, fromEmail, fromName, bodyText = bodyText, bodyHtml = bodyHtml, to=to)


    try:
        st.write ('MsgID to store locally: ', emailResponse['messageid'], end='\n') # Available only if sent to a single recipient
        st.write ('TransactionID to store locally: ', emailResponse['transactionid'])
    except TypeError:
        st.write ('Server returned an error: ', emailResponse)
