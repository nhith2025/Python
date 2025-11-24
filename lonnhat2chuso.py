n=int(input())
donvi=n%10
n=n//10
chuc=n%10
tram=n//10
so1=tram*10+chuc
so2=tram*10+donvi
so3=chuc*10+tram
so4=chuc*10+donvi
so5=donvi*10+tram
so6=donvi*10+chuc
lonnhat=so1
if lonnhat<so2:
    lonnhat=so2
if lonnhat<so3:
    lonnhat=so3
if lonnhat<so4:
    lonnhat=so4
if lonnhat<so5:
    lonnhat=so5
if lonnhat<so6:
    lonnhat=so6
print(lonnhat)
