def f(p):
    return p[1]

a = [[1,3],
     [4,7],
     [-1,8],
     [3,5],
     [2,1]
    ]

#default sort with index 0
x= sorted(a)
print(x)

#secifies the sort with fuction using key
y = sorted(a, key=f)
print(y)

def g(q):
    return len(q)

b = ['abc',
     'xy',
     'deff',
     '11111111'
    ]

#default sort with index 0
i= sorted(b)
print(i)

#secifies the sort with fuction using key
j = sorted(b, key=g)
print(j)