import json

def task1():
    with open('list.json', 'r', encoding='utf-8') as file:
        d = json.load(file)
        
    for p in d['products']:
        print(f'Название: {p["name"]}')
        print(f'Цена: {p["price"]}')
        print(f'Вес: {p["weight"]}')
        
        if p['available']:
            print('В Наличии\n')
        else:
            print('Нет в наличии\n')

def task2():
    with open('list.json', 'r', encoding='utf-8') as file:
        d = json.load(file)

    new = {
        "name": input("Товар: "),
        "price": input("Стоимость товара: "),
        "weight": int(input("Вес товара: ")),
        "available": input("Товар в наличии?: "),
    }
    
    d["products"].append(new)
    
    with open('list1.json', 'w', encoding='utf-8') as file:
        json.dump(d, file, indent=4)
        
    with open('list1.json', 'r', encoding='utf-8') as file:
        new_data = json.load(file)

    for p in new_data['products']:
        print(f'Название: {p["name"]}')
        print(f'Цена: {p["price"]}')
        print(f'Вес: {p["weight"]}')
        
        if p['available']:
            print('В Наличии\n')
        else:
            print('Нет в наличии\n')
            
def task3():
    d = {}
    file = open("new.txt")
    list1 = file.read().split("\n")
    print(list1)
    for i in list1:
        value, key = i.split('-')
        d[key] = value

    new_file = open("DictFile.txt", "w+")

    d = dict(sorted(d.items()))

    for i, k in d.items():
        new_file.write(f'{i} - {k}\n')
    new_file.close()
