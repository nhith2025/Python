def tong2chuso(n):
    donvi=n%10
    chuc=n//10
    return donvi, chuc
n=int(input("Nhap mot so = "))
a, b = tong2chuso(n)
print("Tong 1 so co 2 chu so la:",a+b)
