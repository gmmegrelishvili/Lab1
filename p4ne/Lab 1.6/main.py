import re
import ipaddress
import glob


a=[]
L=glob.glob("C:\\Users\\gm.megrelishvili\\Downloads\\Seafile\\Seafile\\Моя библиотека\\08. Configurations\\config_files\\*.txt")
for book in L:
    x=open(book)
    lines = x.readlines()
    for c in  lines:
     r=re.match("^ ip address ([0-9.]+) ([0-9.]+)$", c)
     if r:
         #print(r.group(1), r.group(2))
         ip1 = ipaddress.IPv4Interface((r.group(1), r.group(2)))
         a.append(ip1)

print(list(set(a)))