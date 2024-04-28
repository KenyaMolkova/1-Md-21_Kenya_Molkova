from PIL import Image, ImageFilter

kartinki = ["1.jpg", "2.jpg","3.jpg","4.jpg","5.jpg"]

for i in kartinki:
    image = Image.open(i)
    img_effect = image.filter(ImageFilter.CONTOUR)
    img_effect.save('filtr' + str(i))
