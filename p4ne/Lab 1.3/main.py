from pysnmp.hlapi import * # Импортировать только High-level API

result = getCmd(SnmpEngine(),CommunityData("public", mpModel=0),UdpTransportTarget(("10.31.70.107", 161)),ContextData(),ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

for r in result:
	for s in r[3]:
		print(s)
result = nextCmd(SnmpEngine(),CommunityData("public", mpModel=0),UdpTransportTarget(("10.31.70.107", 161)),ContextData(),ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')), lexicographicMode=False)
for r in result:
	for s in r[3]:
		print(s)


