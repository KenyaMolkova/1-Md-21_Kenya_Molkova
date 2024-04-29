from PIL import Image

image = Image.open('kotik.jpg')

image_crop = image.crop((500,500,1500,1800))
image_crop.show()
image_crop.save('croppedcat.jpg')
