def hoandoi(a,b):
    tam=a
    a=b
    b=tam
    return a,b
so1=int(input("Nhap so thu nhat: "))
so2=int(input("Nhap so thu hai: "))
so1, so2 = hoandoi(so1,so2)
print("So thu nhat sau khi hoan doi",so1)
print("So thu hai sau khi hoan doi",so2)
