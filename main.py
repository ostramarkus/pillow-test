from PIL import Image, ImageOps, ImageEnhance

with Image.open('img/monalisa.webp') as mona:
    mona = ImageOps.solarize(mona)    
    mona = ImageEnhance.Brightness(mona).enhance(1.5)
    mona.save('processed/monalisa.jpg')





    # mona = ImageOps.expand(mona, 10, (255, 255, 255))
    # mona = ImageOps.posterize(mona, 2)
    # mona = ImageOps.scale(mona, 0.6)    
    # mona = ImageOps.flip(mona)
    # mona = ImageOps.mirror(mona)