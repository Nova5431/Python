max_num = -float('inf')

while (n := int(input())) != 0:
    if max_num < n:
        max_num = n
print(max_num)
