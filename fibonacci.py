def fi(n):
    if n <= 1:
        return n
    return fi(n - 1) + fi(n - 2)
dayso = []
n=int(input())
for i in range(n):
    dayso.append(str(fi(i)))
print(" ".join(dayso))
