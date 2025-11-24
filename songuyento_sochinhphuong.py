import math
def snt(n):
    if n<=1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
    return True
def scp(n):
    if math.sqrt(n)==int(math.sqrt(n)):
        return True
    else:
        return False
n=int(input())
if snt(n)==True:
    if n%4==1:
        a=1
        while not(scp(a)) or not(scp(n-a)):
            a=a+1
        print(a,n-a)
    else:
        print("So nguyen to khong phai tong hai so chinh phuong")
else:
    print(-1)
        
