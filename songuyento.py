n=int(input())
if n<=1:
    dungsai=False
else:
    dungsai=True
    for i in range(2,n):
        if n%i==0:
            dungsai=False
if dungsai==True:
    print("La so nguyen to")
else:
    print("Khong phai la so nguyen to")
