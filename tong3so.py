def lonnhat(a,b,c,d):
    m=a
    if b>m:
        m=b
    if c>m:
        m=c
    if d>m:
        m=d
    return m
a=int(input("Nhap so thu nhat: "))
b=int(input("Nhap so thu hai: "))
c=int(input("Nhap so thu ba: "))
d=int(input("Nhap so thu tu: "))
print(lonnhat(a,b,c,d))
