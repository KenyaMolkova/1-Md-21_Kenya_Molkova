from PIL import Image, ImageDraw, ImageFont

kartinki = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
watermark = "Water Mark"

for i in kartinki:
    image = Image.open(i)

    drawing = ImageDraw.Draw(image)

    colour = (255, 255, 255)
    font = ImageFont.truetype("arial.ttf", 36)
    drawing.text((0,0), watermark, fill=colour, font=font)

    image.save("watrmarkd" + i)
