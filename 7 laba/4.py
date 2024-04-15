from PIL import Image, ImageDraw, ImageFont



text = 'Водяной знак'
font = ImageFont.truetype('arial.ttf', 36)

kartinki = ["1.jpg", "2.jpg","3.jpg","4.jpg","5.jpg"]

for i in kartinki:
    image = Image.open(i)
    margin = 10
    width, height = image.size
    draw = ImageDraw.Draw(image)
    textwidth, textheight = draw.textsize(text, font)
    x = width - textwidth - margin
    y = height - textheight - margin
    draw.text((x,y), text, font = font)
    image.show()