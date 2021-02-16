# Neural-Network-Based-Botnet-Detection
Creating a Deep Learning Model to detect Botnet using mulitple features.

# Features

## General Features 
|Feature|Deails| 
|-------|------|
|SrcIP | Source IP|
|DstIP | Destination IP|
|Protocol|Types of protocol TCP/UDP|
|SrcPort|Source Port|
|DstPort|Destination Port|
|TCP flags| tcp flags type(SYN/FIN/ACK)|

## Byte Based Feature
|Feature|Deails| 
|-------|------|
|TBT|Total Number of Bytes|
|DPL|total number of packets with same length over total number of packets|
|PL|The total number of bytes of all the packets over the total number of packets in the same flow|
|BPP|Average Bytes per packet|
|SB|Average number of bytes in sublfow|
|PV|| -----> payload
|APL|| -----> payload

## Packet Based Feature
|Feature|Deails| 
|-------|------|
|PX|Total number of Packet Exchanged|
|NNP|Number of Null Packets Exchanged|
|IOPR|Ratio b/w number of incoming packets over the number of outgoing packets|
|APL|Average Packet Length|
|SP |Average number of packets in subflow|

## Time Based Feature
|Feature|Deails| 
|-------|------|
|BS|Average bits/sec|
|PPS|Average Packet/Sec|
|AIT|Averge inter arrival time of packets|
|FPH|Numner of flows from this address over total number of flows generated per hour|

## BehaviourBased
|Feature|Deails| 
|-------|------|
|Duration|Total duration of the flow|
|Reconnect|NUmbers of times SrcIP connects to same DstIP|
|FPS|length of first packet|
|FWIN|total number of bytes sent in initial window|
|CDA|The number of connections over the number of destination IP addresses|