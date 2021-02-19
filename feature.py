#protocol - { 6:HTTP , 17:SMTP , 0:SSH }

import pandas as pd
import numpy as np
import socket
import struct
from sklearn import preprocessing

df = pd.read_csv("dataset.csv")
# le = preprocessing.LabelEncoder()

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


def totalBytes():
    df_new['TBT']=df['TotLen Fwd Pkts']+df['TotLen Bwd Pkts']

def iopr():
     df_new["IOPR"]=df["Tot Fwd Pkts"]/ df["Tot Bwd Pkts"]
     
def apl():
    df_new["APL"]=df["Pkt Len Mean"]
    
def avgpacket():
    df_new["SP"]=(df["Subflow Fwd Pkts"]+df["Subflow Bwd Pkts"])/2

def duration():
    df_new["DUR"]= df["Flow Duration"]/1000000

def reconnect():
    df_new["REC"]= ''
    for i in Sip:
        for j in Dip:
            df1 = df.loc[(df['Src IP']==i) & (df['Dst IP']==j)]
            df_new.loc[(df_new['Src IP']==i) & (df_new["Dst IP"]==j) , "REC"]=len(df1)-1

def avgHeaderByte():
    df_new["FPB"]=(df['Fwd Header Len']+df['Bwd Header Len'])/2
    
def fwin():
    df_new["FWIN"]=df['Init Fwd Win Byts']

def avgSubflowBytes():
    df_new['SB']= (df['Subflow Fwd Byts']+df['Subflow Bwd Byts'])/2

def bytesPerPacket():
    df_new['BPP'] = (df['Fwd Pkt Len Mean']+df['Bwd Pkt Len Mean'])/(df["Tot Fwd Pkts"]+df["Tot Bwd Pkts"])

def FPH():
    df_new['FPH']=''
    for i in Sip:
        l = len(df.loc[(df['Src IP']==i)]) / len(df)       
        df_new.loc[(df_new['Src IP']==i), "FPH"]= l

def AIT():
    df_new['AIT']=df["Flow IAT Mean"]/1000000

def bytsPerSec():
    df_new["BS"]=df['Flow Byts/s']

def packetPerSec():
    df_new["PPS"]=df['Flow Pkts/s']
        
def CDA():
    df_new['CDA']=''
    for i in Sip:
        l = len(df.loc[(df['Src IP']==i)]) / len(Dip)
        df_new.loc[(df_new['Src IP']==i), "CDA"]= l

def totalNullPackets():
    df_new["NNP"]=''
    for i in Sip:
        for j in Dip:
            df1 = df.loc[(df['Src IP']==i) & (df['Dst IP']==j)]
            # st = len(df1.loc[(df1['Tot Fwd Pkts']=='0') & (df1['Tot Bwd Pkts']=="0")])
            df_new.loc[(df_new['Src IP']==i) & (df_new["Dst IP"]==j) , "NNP"]=len(df1)-1
    
if __name__== "__main__":
    #Source Ip
    # df['Src IP'] = df['Src IP'].apply(convertIP)
    df_new['Src IP'] = df['Src IP']

    #Destination IP
    # df['Dst IP'] = df['Dst IP'].apply(convertIP)
    df_new['Dst IP'] = df['Dst IP']
    #source port
    df_new["Src Port"] = df["Src Port"]
    #destination port
    df_new["Dst Port"] = df["Dst Port"]
    #protocol
    df_new["Proto"] = df["Protocol"]
    #Number of packets with ACK
    df_new['ACK flg cnt'] = df['ACK Flag Cnt']
    #Number of packets with SYN
    df_new['SYN flag cnt'] = df['SYN Flag Cnt']
    #Number of packets with RST
    df_new['RST flag cnt']=df['RST Flag Cnt']

    print("Ratio b/w number of incoming packets over the number of outgoing packets")
    iopr()

    print("Average Packet Length")
    apl()

    print("Average number of packets in subflow")
    avgpacket()

    print("Total duration of the flow")
    duration()

    print("Numbers of times SrcIP connects to same DstIP")
    reconnect()
    
    print("Avg bytes used for headers")
    avgHeaderByte()

    print("total number of bytes sent in initial window")
    fwin()

    print("Bytes per packet")
    bytesPerPacket()

    print("Average number of bytes in sublfow")
    avgSubflowBytes()

    print("bytes per second")
    bytsPerSec()

    print("packet per second")
    packetPerSec()

    print("Averge inter arrival time of packets")
    AIT()

    print("Numner of flows from this address over total number of flows generated")
    FPH()

    print("The number of connections over the number of destination IP addresses")
    CDA()

    print(df_new)
    df_new.to_csv("trainData.csv",index=False)