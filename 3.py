n = int(input())
if n % 4 == 0 and n % 100 != 0:
    print(n, ' - Високосный год')
elif n % 400 == 0:
    print(n, '- Високосный год ')
else:
    print(n, ' - Этот год не високосный')