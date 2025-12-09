fi = open("MINMAX.INP","r")
fo = open("MINMAX.OUT","w")
n = int(fi.readline())
ln = fi.readline()
a = ln.split(" ")
nhonhat=int(a[0])
lonnhat=int(a[0])
for i in range(1,n):
    if nhonhat>int(a[i]):
        nhonhat=int(a[i])
for i in range(1,n):
    if lonnhat<int(a[i]):
        lonnhat=int(a[i])
fo.write(str(nhonhat)+"\n")
fo.write(str(lonnhat))
fi.close()
fo.close()
