def select(arr):
    n = len(arr)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if arr[j]<arr[m]:
                m = j
        arr[m],arr[i] = arr[i], arr[m]

arr = list(map(int,input().split()))
select(arr)
print(arr)