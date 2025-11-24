def sht(n):
    tong=0
    for i in range(1,n+1):
        if n%i==0:
            tong=tong+i
    if tong!=2*n:
        return False
    return True
n=int(input())
if sht(n)==True:
    print(1)
else:
    print(0)
for i in range(1,n+1):
    if sht(i)==True:
        print(i,end=" ")
m=int(input())
while m>n:
    m=int(input("n phai nho hon n "))
for i in range(m,n+1):
    if sht(i)==True:
        print(i,end=" ")
