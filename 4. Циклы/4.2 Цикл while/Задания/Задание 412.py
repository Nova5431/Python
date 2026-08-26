max_1 = -float('inf')
max_2 = -float('inf')
while (n := int(input())) != 0:
    if max_1 < n:
        max_2 = max_1
        max_1 = n
    elif n > max_2:
        max_2 = n



print(max_2)
