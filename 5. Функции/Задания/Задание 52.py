def is_perfect(n):
    sum = 0
    for div in range(1, n):
        if n % div == 0:
            sum += div
    return n == sum




num = 1
counter = 0
n = int(input())
while counter != n:
    num += 1
    if is_perfect(num):
       print(num, end=' ')
       counter +=1


