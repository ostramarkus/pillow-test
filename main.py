import glob
from PIL import Image, ImageOps

def resize_image(source_path, dest_path):
    with Image.open(source_path) as img:
        img = ImageOps.fit(img, (200, 200))
        img.save(dest_path)

paths = glob.glob("food_img/*.jpg")
for path in paths:
    filename = path.split('/')[-1]
    resize_image(path, 'food_proc/' + filename)