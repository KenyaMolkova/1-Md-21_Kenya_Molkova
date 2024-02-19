
#1 - 36 - купе
#37 - 54 - плацкарт
#четные нижние, нечетные - верхние

n = int(input())
if n >= 1 and n <= 36:
    print('купе')
    if n % 2 == 0:
        print('нижнее')
    else:
        print('верхнее')
elif n >= 37 and n <= 54:
    print('плацкарт')
    if n % 2 == 0:
        print('нижнее')
    else:
        print('верхнее')
