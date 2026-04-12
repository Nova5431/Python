a = int(input())
b = int(input())
c = int(input())

'''if c <= a >= b:
    print(a)

elif c <= b >= a:
    print(b)

else:
    print(c)'''

if a > b:
    m = a
else:
    m = b

if m > c:
    print(m)
else:
    print(c)

