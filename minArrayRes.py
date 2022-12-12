def Rmin(A,l):
    if(l == 1):
        return A[0]
    return min(A[l-1], Rmin(A, l-1))
    

A = [1,4,45,-50,6,10,2]
l = len(A)
print(Rmin(A,l))