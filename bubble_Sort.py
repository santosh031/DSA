def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
arr = list(map(int, input().split()))
print(arr)
bubble(arr)
print(arr)