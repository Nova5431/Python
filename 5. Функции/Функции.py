def sum_sequence(a, b):
    total = 0
    for i in range(a, b + 1):
        total += i
    return total

begin = 5
end = 20
print(sum_sequence(begin, end))
print(sum_sequence(45, 100))
print(sum_sequence(45, 1000))

# Моменты
# 1. Переменные, передаваемые в функцию не обязаны
#    совпадать по имени с параметрами функции
# 2. Очень не рекомендуется использовать глобальные переменные