def f2(x):
    try:
        print((100 / int(x)))
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    except ValueError:
        return 'строковый формат'

print(f2(input('Введите число: ')))
