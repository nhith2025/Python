#Su dung ham de tach so co 3 chu so
def tach(n):
    donvi=n%10
    n=n//10
    chuc=n%10
    tram=n//10
    return donvi, chuc, tram
n=int(input())
dv, ch, tr = tach(n) #dv luu hang don vi, ch luu hang chuc, tr luu hang tram
lonnhat=dv
if ch>lonnhat:
    lonnhat=ch
if tr>lonnhat:
    lonnhat=tr
print(lonnhat)
