def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
dayso=[]
n=int(input())
for i in range(n+1):
    dayso.append(str(fibonacci(i)))
print(" ".join(dayso))
