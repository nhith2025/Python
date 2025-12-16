fi = open("VTNHO.INP","r")
fo = open("VTNHO.OUT","w")
n = int(fi.readline())
ln = fi.readline()
a = ln.split(" ")
for i in range(1,n):
    if a[i]==min(a):
        fo.write(str(i+1)+" ")
fi.close()
fo.close()
