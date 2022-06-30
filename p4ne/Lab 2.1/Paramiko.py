import paramiko,time
import pprint
import re
import ssl
import requests
import urllib3

from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter

class Ssl1HttpAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block, ssl_version=ssl.PROTOCOL_TLSv1)

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'
s = requests.Session()
s.mount("https://10.31.70.210:55443", Ssl1HttpAdapter())
BUF_SIZE = 20000
TIMEOUT = 1

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_connection.connect("10.31.70.209", username="restapi", password="j0sg1280-7@", look_for_keys=False, allow_agent=False)
session = ssh_connection.invoke_shell()
print(session.send("\n\n"))
print(session.recv(10000))
print(session.send('terminal length 0\n'))
time.sleep(500)
session.send("\n")
session.recv(10000)
print(session.send("show run\n"))
session.send("\nshow interface\n")
ans=session.recv(1000)
ans.decode()
L=ans.decode().split('\r\n')
print(L)
for line in L:
    r=re.match('^(.+?[0-9]+)) is .+', line)
    if r:
        print(r.group(1))
for line in L:
    r=re.match('.+([0-9]+)packets input, ([0-9]+) bytes',line)
    if r:print('Packets',r.group(1),"bytes",r.group(2))
time.sleep(500*2)
s = session.recv(10000).decode()
session.close()