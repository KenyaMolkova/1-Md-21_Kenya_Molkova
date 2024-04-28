color1 = input()

if color1 == 'красный':
    color2 = input()
    if color2 == 'желтый':
        print('оранжевый')
    elif color2 == 'синий':
        print('фиолетовый')
    else:
        print('ошибка')
elif color1 == 'желтый':
    color2 = input()
    if color2 == 'красный':
        print('оранжевый')
    elif color2 == 'синий':
        print('зеленый')
    else:
        print('ошибка')
elif color1 == 'синий':
    color2 = input()
    if color2 == 'красный':
        print('фиолетовый')
    elif color2 == 'желтый':
        print('зеленый')
    else:
        print('ошибка')
else:
    print('ошибка')
    ""
