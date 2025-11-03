n=int(input())
donvi=n%10 #Lay hang don vi
n=n//10 #Xoa hang don vi, con 2 chu so
chuc=n%10 #Lay hang chuc
tram=n//10 #Lay hang tram
lonnhat=donvi #Gan so dau tien cho bien lonnhat de so sanh voi cac so con lai
if chuc>lonnhat: #Neu bien chuc lon hon bien lonnhat thi gán chuc la so lon nhat
    lonnhat=chuc
if tram>lonnhat: #Neu bien tram lon hon bien lonnhat thi gán tram la so lon nhat
    lonnhat=tram
print(lonnhat)
