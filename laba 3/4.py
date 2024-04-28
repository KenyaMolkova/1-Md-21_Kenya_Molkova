import random
t = 0
f = 0
while f<3:
    random_number1 = random.randint(0, 10)
    random_number2 = random.randint(0, 10)
    print(random_number1 , '+' , random_number2)
    a = int(input())
    if a == random_number1 + random_number2:
        print('Правильно!')
        t += 1
    else:
        print('Ответ неверный')
        f+=1
print('Игра окончена, правильных ответов:' , t)
