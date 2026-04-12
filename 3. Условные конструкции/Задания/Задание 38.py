a = int(input())
b = int(input())
c = int(input())
'''a <= b <= c'''
if a > c:
    a, c = c, a
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
print(a, b, c)