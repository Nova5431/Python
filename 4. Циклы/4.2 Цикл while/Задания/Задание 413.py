max_1 = -float('inf')
a = 0
b = 0
counter = 0
while (n := int(input())) != 0:
    counter += 1
    if max_1 < n:
        max_1 = n
        b = counter
        a = counter
    elif max_1 == n:
        b = counter
print(a,b)
