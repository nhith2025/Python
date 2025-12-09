fin=open("TONGTB.INP","r")
fout=open("TONGTB.OUT","w")
dong1=int(fin.readline())
dong2=fin.readline()
a=dong2.split(" ")
tong=0
dem=0
for i in range(0,dong1):
    tong=tong+int(a[i])
tbc=tong/dong1
fout.write(str(tong)+"\n")
fout.write(str(tbc))
fin.close()
fout.close()
