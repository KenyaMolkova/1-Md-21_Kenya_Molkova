from PIL import Image
kartinka = Image.open('ну я.jpg')
kartinka.show()
print('Размер изображения: ', kartinka.size)
print('Формат изображения: ', kartinka.format)
print('Режим изображения: ', kartinka.mode)
