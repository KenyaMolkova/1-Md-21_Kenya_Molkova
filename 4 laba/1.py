def f(x):
    if x % 3 == 0:
        return 'Делится'
    else:
        return 'Не делится'
print(f(int(input('Введите число: '))))
