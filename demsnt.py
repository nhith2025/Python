def snt(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
dem=0
i=2
while dem<a:
    if snt(i)==True:
        dem=dem+1
        print(i,end=" ")
    i=i+1
