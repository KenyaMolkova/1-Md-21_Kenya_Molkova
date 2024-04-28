
#1
import random
a = []
for i in range(5):
    a.append(random.randint(1, 10))
s = int(input('Введите число: '))
if s in a:
    print(a, s, "Поздравляю, Вы угадали число!" )
else:
    print(a, s, "Нет такого числа!")

#2
import random
a = []
for i in range(5):
    a.append(random.randint(1, 10))
s = {}.fromkeys(a)
b = list(s.keys())
if len(b) < len(a):
    print('Повторов: ', len(a)-len(b), a)
else:
    print('Повторов нет')


#3
