def insertion(arr):
    n = len(arr)
    for wall in range(1,n):
        curr = arr[wall]
        postion_pointer = wall-1
        while postion_pointer >=0 and curr <arr[postion_pointer]:
            arr[postion_pointer+1]= arr[postion_pointer]
            postion_pointer = postion_pointer - 1 

        arr[postion_pointer +1]= curr



arr = list(map(int, input().split()))
insertion(arr)
print(arr)