def f3(x):
    date = x.split('.')
    year = date[2]
    if int(date[0]) * int(date[1]) == int(year) % 100:
        return 'True'
    else:
        return 'False'

print(f3(input('Введите дату: ')))
