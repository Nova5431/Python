def is_prime(n):
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            return False
    return True


num = 1
counter = 0
n = int(input())
while counter != n:

    num += 1

    if is_prime(num):

        print(num, end=' ')
        counter += 1























