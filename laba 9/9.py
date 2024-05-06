from PIL import Image, ImageFilter
from pathlib import Path
import os
from csv import DictReader

def task1():
    p = Path("/UserFolders/Desktop/Молькова Кения/kartinki")
    p2 = Path("/UserFolders/Desktop/Молькова Кения/New_Directory")
    p2.mkdir()

    for i in p.glob('*'):
        image = Image.open(i)
        img_effect = image.filter(ImageFilter.CONTOUR)
        a = os.path.basename(i)
        name = "filtr" + str(a)
        img_effect.save(f"D:\\UserFolders\\Desktop\\Молькова Кения\\New_Directory\\{name}")

def task2():
    p = Path("/UserFolders/Desktop/Молькова Кения/kartinki")
    p2 = Path("/UserFolders/Desktop/Молькова Кения/New_Directory2")
    p2.mkdir()

    for i in p.glob('*'):
        file_format = os.path.splitext(i)[1]
        if file_format == '.jpg' or file_format == '.png':
            image = Image.open(i)
            img_effect = image.filter(ImageFilter.CONTOUR)
            a = os.path.basename(i)
            name = "filtr" + str(a)
            img_effect.save(f"D:\\UserFolders\\Desktop\\Молькова Кения\\New_Directory2\\{name}")

def task3():
    with open('products.csv', 'r', encoding='utf-8') as f:
        data = DictReader(f)
        list_products = list(data)
    sum = 0
    for i in list_products:
        product = i.get(('Продукт'))
        quantity = i.get(('Количество'))
        price1 = i.get(('Цена'))
        price = int(quantity) * int(i.get(('Цена')))
        print(f'{product} - {quantity} шт. за {price1} руб.')
        sum = sum + int(price)

    print(f'Итоговая сумма: {sum} руб.')



task3()