import ipaddress
from ipaddress import IPv4Network
import random
class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        IPv4Network.__init__(self,(random.randint(0x0B000000, 0xDF000000), random.randint(8, 24)), strict=False)


    def regular(self):
        if self.is_multicast and not self.is_multicast or self.is_private or  self.is_loopback  or self.is_reserved or self.is_unspecified:
            return self


    def key_value(self):
        return self.network_address+self.netmask

def sortfunc(x):
        return x.key_value()

networklist=[]
for i in range (50):
    rn = IPv4RandomNetwork()
    if rn.regular(): networklist.append(rn)
print(networklist)

for x in sorted(networklist, key=sortfunc):
        print(x)


