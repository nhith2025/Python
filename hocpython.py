a=int(input())
b=int(input())
if a%2==0:
    a=a/2
    b=b*2
else:
    a=a+1
    b=b+a
print(a," ",b)
