n = int(input())
count = 0
'''
for i in range(1, n + 1):
    if count >= n:
        break
    for j in range(i):
        if count >= n:
            break
        print(i, end=' ')
        count += 1
'''
x = 1
for i in range(n):
    count += 1
    if count > x:
        x += 1
        count = 1
    print(x, end=' ')


