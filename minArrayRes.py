def Rmin(a,l):
    if(l == 1):
        return a[0]
    return min(a[l-1], Rmin(a, l-1))
    

a = [1,4,45,-50,6,10,2]
l = len(a)
print(Rmin(a,l))