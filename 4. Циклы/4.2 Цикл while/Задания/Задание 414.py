old_n = 0
b = 0
c = 0
while (n := int(input())) != 0:
    if old_n == n:
        b += 1

    if old_n != n :
        c = b
        b = 0
        old_n = n

print(c)



