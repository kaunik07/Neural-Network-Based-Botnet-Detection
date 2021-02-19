import pandas as pd
import numpy as np
import socket
import struct
from sklearn import preprocessing

df = pd.read_csv("botnetDataset.csv")
le = preprocessing.LabelEncoder()


def convertIP(ip):
    ip = socket.inet_aton(ip)
    ip = struct.unpack("!L", ip)[0]
    return ip

def encodingLabel(st):
    le.fit(df[st])
    df[st] = le.transform(df[st])
    
if __name__== "__main__":
    df['srcip'] = df['srcip'].apply(convertIP)
    df['dstsip'] = df['dstsip'].apply(convertIP)
    encodingLabel('state')
    encodingLabel('proto')
    encodingLabel('service')
    encodingLabel('attack_cat')
    print(df)


# protocol = {'tcp':0, 'udp':1, 'arp':2, 'icmp':3, 'ospf':4, 'udt':5, 'sctp':6, 'igmp':7, 'gre':8,
#        'sep':9, 'swipe':10, 'mobile':11, 'sun-nd':12, 'pim':13, 'rtp':14, 'ip':15, 'ggp':16,
#        'ipnip':17, 'st2':18, 'cbt':19, 'argus':20, 'bbn-rcc':21, 'chaos':22, 'egp':23, 'emcon':24,
#        'igp':25, 'nvp':26, 'pup':27, 'xnet':28, 'mux':29, 'dcn':30, 'hmp':31, 'prm':32, 'trunk-1':33,
#        'trunk-2':34, 'xns-idp':35, 'irtp':36, 'leaf-1':37, 'leaf-2':38, 'rdp':39, 'iso-tp4':40,
#        'netblt':41, 'merit-inp':42, 'mfe-nsp':43, '3pc':44, 'idpr':45, 'xtp':46, 'ddp':47,
#        'idpr-cmtp':48, 'tp++':49, 'il':50, 'ipv6':51, 'ipv6-route':52, 'sdrp':53,
#        'ipv6-frag':54, 'idrp':55, 'rsvp':56, 'bna':57, 'mhrp':58, 'i-nlsp':59, 'narp':60,
#        'tlsp':61, 'skip':62, 'ipv6-no':63, 'ipv6-opts':64, 'any':65, 'cftp':66, 'sat-expak':67,
#        'kryptolan':68, 'ippc':69, 'rvd':70, 'sat-mon':71, 'cpnx':72, 'ipcv':73, 'visa':74,
#        'cphb':75, 'wsn':76, 'br-sat-mon':77, 'pvp':78, 'wb-mon':79, 'iso-ip':80, 'wb-expak':81,
#        'secure-vmtp':82, 'vmtp':83, 'ttp':84, 'vines':85, 'nsfnet-igp':86, 'dgp':87,
#        'eigrp':88, 'tcf':89, 'larp':90, 'sprite-rpc':91, 'ax.25':92, 'ipip':93, 'mtp':94,
#        'aes-sp3-d':95, 'etherip':96, 'micp':97, 'encap':98, 'pri-enc':99, 'gmtp':100, 'ifmp':101,
#        'pnni':102, 'aris':103, 'scps':104, 'a/n':105, 'qnx':106, 'ipcomp':107, 'snp':108,
#        'compaq-peer':109, 'ipx-n-ip':110, 'vrrp':111, 'pgm':112, 'l2tp':113, 'zero':114, 'ddx':115,
#        'iatp':116, 'srp':117, 'stp':118, 'uti':119, 'smp':120, 'sm':121, 'ptp':122, 'fire':123, 'isis':124,
#        'crtp':125, 'crudp':126, 'sccopmce':127, 'iplt':128, 'pipe':129, 'sps':130, 'fc':131, 'unas':132,
#        'ib':133}

# state ={'FIN':1, 'INT':2, 'CON':3, 'REQ':4, 'ECO':5, 'PAR':6, 'ACC':7, 'RST':8, 'TST':9,
#        'ECR':10, 'TXD':11, 'no':12, 'URN':13, 'MAS':14, 'CLO':15}