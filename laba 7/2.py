from PIL import Image
kartinka = Image.open('ну я.jpg')

res_kartinka = kartinka.reduce(3)
res_kartinka.save('novayakartinka.png')

vert_kartinka = kartinka.transpose(Image.FLIP_TOP_BOTTOM)
horizon_kartinka = kartinka.transpose(Image.FLIP_LEFT_RIGHT)

vert_kartinka.save('vertkartinka.png')
horizon_kartinka.save('horizonkartinka.png')

vert_kartinka.show()
horizon_kartinka.show()
