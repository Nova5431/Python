old_n = 0
count = 1
max_len = 0
while (n := int(input())) != 0:
    if old_n == n:
        count += 1

    else:
        max_len = max(count, max_len)
        count = 1
    old_n = n

print(max_len if max_len > count else count)



