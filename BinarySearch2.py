#BinarySearch example2 (if a element present in a list return index, if not insert that element in list then return index )

def s2(n, arr, tar):
    l, h = 0, len(arr)-1
    while l<=h:
        m =(l + h)//2
        if arr[m]== tar:
            return m
        if arr[m]>tar:
            h = m-1
        else:
            l = m+1
    return h +1

n = int(input())
arr = list(map(int, input().split()))
tar = int(input())
print(s2(n, arr, tar))