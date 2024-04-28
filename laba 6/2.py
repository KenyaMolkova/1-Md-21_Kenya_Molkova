d = {1:'АВЕИНОРСТ',
     2:'ДКЛМПУ',
     3:'БГЁЬЯ',
     4:'ЙЫ',
     5:'ЖЗХЦЧ',
     8:'ШЭЮ',
     10:'ФШЪ'}

word = input('Введите слово: ').upper()

summa = 0
for i in word:
    for k, v in d.items():
        if i in v:
            summa = summa + k
    
print(summa)


print(sum([k for i in word for k, v in d.items() if i in v]))

