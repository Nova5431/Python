max_num = -float('inf')
counter = 0
while (n := int(input())) != 0:
    if max_num < n:
        max_num = n
        counter = 1
    elif max_num == n:
        counter += 1
print(counter)










