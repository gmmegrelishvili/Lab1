import glob
a=[]
L=glob.glob("C:\\Users\\gm.megrelishvili\\Downloads\\Seafile\\Seafile\\Моя библиотека\\08. Configurations\\config_files\\*.txt")
for book in L:
    x=open(book)
    lines = x.readlines()
    for c in  lines:
     ip = ' ip address'
     if ip in c:
        pos=c.replace(ip, "")

        a.append(pos)

print(list(set(a)))
