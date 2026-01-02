fi=open("TANG_2.INP","r")
fo=open("TANG_2.OUT","w")
n=int(fi.readline())
line2=fi.readline().split()
# Sử dụng thuật toán sắp xếp tăng dần
for i in range(0,n):
    for j in range(1+i,n):
        if line2[i]>line2[j]:
            tam=line2[i]
            line2[i]=line2[j]
            line2[j]=tam
for i in range(0,n):
    fo.write(str(line2[i])+" ")
    
fo.write("\n")
# Sử dụng thuật toán sắp xếp giảm dần
for i in range(0,n):
    for j in range(1+i,n):
        if line2[i]<line2[j]:
            tam=line2[i]
            line2[i]=line2[j]
            line2[j]=tam
for i in range(0,n):
    fo.write(str(line2[i])+" ")
    
fi.close()
fo.close()
