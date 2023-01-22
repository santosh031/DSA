#binary search example (if a element in list print element's index if element not present return -1)

def s(n, arr, tar):
    l, h = 0, len(arr)-1
    while l<= h:
        m = (l+h)//2
        if arr[m] == tar:
            return m
        if arr[m]>tar:
            h = m-1
        else:
            l = m+1
    return -1


n = int(input())
arr = list(map(int, input().split()))[:n]
tar = int(input())
print(s(n,arr,tar))