#zip ->  print the values of similar index of each list.

a= list(map(int, input().split()))
b= list(map(int, input().split()))
c= list(map(int, input().split()))

for x,y,z in zip(a,b,c):
    print(x,y,z)
