from PIL import Image, ImageDraw, ImageFont

kartinka = ['croppedcat.jpg']
name = input()


image = Image.open('croppedcat.jpg')

drawing = ImageDraw.Draw(image)

colour = (8, 34, 12)

font = ImageFont.truetype("timesbd.ttf", 90)

drawing.text((100,0), 'Поздравляю, ', fill='red',  font=font)
drawing.text((650,0), name, fill='blue',  font=font)

image.show()

