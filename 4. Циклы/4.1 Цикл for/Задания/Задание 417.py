n = int(input())

zero = 0
negative = 0
positive = 0
x = 0




for i in range(n):
    m = int(input())

    if m == 0:
        zero += 1
    elif m < 0:
        negative += 1
    elif m > 0:
        positive += 1
        x += m
l = x/positive

print(f'Нулей: {zero}\nOтрицательных: {negative}\nСреднее положительных: {l:.2f}')

