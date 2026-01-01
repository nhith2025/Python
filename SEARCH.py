fi=open("SEARCH.INP","r")
fo=open("SEARCH.OUT","w")
dong1=fi.readline()
a=dong1.split(" ")
n=int(a[0])
x=int(a[1])
dong2=fi.readline()
b=dong2.split(" ")
dem=0
for i in range(0,n):
    if int(b[i])==x:
        dem=dem+1
if dem>0:
    fo.write(str(dem))
else:
    fo.write("-1")
fi.close()
fo.close()
