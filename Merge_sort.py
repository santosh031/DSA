def merge(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge(left)
        merge(right)
        l = r = a = 0
        while l< len(left) and r < len(right):
            if left[l]< right[r]:
                arr[a] = left[l]
                l += 1
            else:
                arr[a] = right[r]
                r += 1
            a+= 1
        while l<len(left):
            arr[a]= left[l]
            l +=1
            a +=1
        while r<len(right):
            arr[a] = right[r]
            r +=1
            a +=1


arr =list(map(int,input().split()))
merge(arr)
print(arr)