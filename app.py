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
        for info in addrinfos:
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
#df['Marca temporal'] = pd.to_datetime(df['Marca temporal']).dt.strftime('%d/%m/%y')
    df['timestamp']=pd.to_datetime(df['timestamp'],unit='s')
    df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%d/%m/%y')

#lst = re.findall('\S+@\S+', s) 
    
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
