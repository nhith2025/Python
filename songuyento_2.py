def songuyento(n):
    if n<=1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
    return True
n=int(input())
if songuyento(n)==True:
    print("La so nguyen to")
else:
    print("Khong phai la so nguyen to")
