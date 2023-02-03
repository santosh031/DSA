#enumerate -> which print the element along with index value 

b = list(map(int, input().split()))
 
#method1
print(list(enumerate(b)))


#method2
for x in enumerate(b):
    print(x)


#method3
for i, el in enumerate(b):
    print(i, el)


#all the method give diffrent style of output but same output