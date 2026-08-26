start_sum = int(input())
target_sum = int(input())
percent = int(input())
percent /= 12
i = 0
while start_sum <= target_sum:
    start_sum += start_sum * percent/100
    i += 1
    print(f'{i} - {start_sum:.2f}')