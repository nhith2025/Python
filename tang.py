fi=open("TANG.INP","r")
fo=open("TANG.OUT","w")
n=int(fi.readline())
line2=fi.readline().split()
line2.sort()
for i in range(0,n):
    fo.write(str(line2[i])+ " ")
fo.write("\n") 
line2.sort(reverse=True)
for i in range(0,n):
    fo.write(str(line2[i])+ " ")
fi.close()
fo.close()
