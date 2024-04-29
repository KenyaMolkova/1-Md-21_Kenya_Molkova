from PIL import Image

d = {'День Рождения': 'birthday.jpg',
     'Пасха': 'easter.jpg',
     '8 марта': 'march8.jpg',
     'Новый Год': 'new year.jpg',
     'День космонавтики': 'space day.jpg'}

holiday = input('Введите ваш праздник: ')

print(d[holiday])


image = Image.open(d[holiday])
image.show()
