#add elements in list simple
n= int(input())
a = list(map(int, input().split()))[:n]
print(a)

#adding elements in list using For Loop
l = int(input())
b = []
for i in range(0,l):
    n = int(input())
    b.append(n)
print(b)


#Adding elements in List usin Function
def li(p):
    l=[]
    for i in range(0,p):
        n= int(input().split())
        l.append(n)
    print(l)

p = int(input())
li(p)