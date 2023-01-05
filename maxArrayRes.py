def rmax(A,l):
    if(l==1):
        return A[0]
    return max(A[l-1], rmax(A,l-1))

A = [1,4,45,-50,6,10,2]
l = len(A)
print(rmax(A,l))
