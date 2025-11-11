import math
a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(s)
else:
    print("-1")
