from scapy.all import *
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

net = '185.143.233.238'
ans , uans = sr(IP(dst=net)/ICMP(),timeout=1,verbose=0)
for send,recv in ans:
    print(f'HOST is up{recv[IP].src}')

