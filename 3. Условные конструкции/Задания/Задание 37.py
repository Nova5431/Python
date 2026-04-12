mashrooms = int(input())

if mashrooms % 10 == 1 and mashrooms % 100 != 11:
    print('гриб')

elif 2 <= mashrooms % 10 <= 4 and not (12 <= mashrooms % 100 <= 14):
    print('гриба')

else:
    print('грибов')
