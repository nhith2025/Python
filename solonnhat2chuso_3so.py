n=int(input())
a=n%10
n=n//10
b=n%10
c=n//10
so1=10*a+b
so2=10*a+c
so3=10*b+a
so4=10*b+c
so5=10*c+a
so6=10*c+b
lonnhat=so1
if so2>lonnhat:
    lonnhat=so2
if so3>lonnhat:
    lonnhat=so3
if so4>lonnhat:
    lonnhat=so4
if so5>lonnhat:
    lonnhat=so5
if so6>lonnhat:
    lonnhat=so6
print(lonnhat)
