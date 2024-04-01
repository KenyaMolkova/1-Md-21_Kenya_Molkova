d = {1:'АВЕИНОРСТ',
     2:'ДКЛМПУ',
     3:'БГЁЬЯ',
     4:'ЙЫ',
     5:'ЖЗХЦЧ',
     8:'ШЭЮ',
     10:'ФШЪ'}

word = input('Введите слово: ').upper()

#print(sum([k for i in word for k, v in d.items() if i in v]))

summa = 0
for v in word:
    for i in d.values():
        for k in d.keys():
            if v in i:
                print('da')



