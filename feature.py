#protocol - { 6:HTTP , 17:SMTP , 0:SSH }


import pandas as pd
import numpy as np
import socket
import struct
from sklearn import preprocessing

df = pd.read_csv("botnetDataset.csv")
le = preprocessing.LabelEncoder()

Sip = df["Src IP"].unique()
Dip = df["Dst IP"].unique()

df_new = pd.DataFrame()

def convertIP(ip):
    ip = socket.inet_aton(ip)
    ip = struct.unpack("!L", ip)[0]
    return ip

# def encodingLabel(st):
#     le.fit(df[st])
#     df[st] = le.transform(df[st])
#     df_new[st]=df[st]


def packetExchanged(src,dst):
    df_new['PX'] = df[src]+df[dst]

def bytesExchanged(src,dst):
    df_new['TBT'] = df[src]+df[dst]

def totalBytesOverTotalPacket():

def totalNullPackets():
    df_new["NNP"]=''
    for i in Sip:
        for j in Dip:
            df1 = df.loc[(df['Src IP']==i) & (df['Dst IP']==j)]
            st = len(df1.loc[(df1['Tot Fwd Pkts']=='0') & (df1['Tot Bwd Pkts']=="0")])
            df_new.loc[(df_new['Src IP']==i) & (df_new["Dst IP"]==j) , "NNP"]=st
    
    
    


    
    
if __name__== "__main__":

    #Source Ip
    # df['Src IP'] = df['Src IP'].apply(convertIP)
    df_new['Src IP'] = df['Src IP']

    #Destination IP
    # df['Dst IP'] = df['Dst IP'].apply(convertIP)
    df_new['Dst IP'] = df['Dst IP']

    

    #Total Packet Exchanged
    packetExchanged('spkts','dpkts')

    #Total Number of Bytes
    bytesExchanged('sbytes','dbytes')

    print(df_new)