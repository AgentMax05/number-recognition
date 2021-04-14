from PIL import Image
from PIL import ImageOps
import os

import ml

def bw(pixel):
    if pixel > 160:
        return 255
    else:
        return 0

files = os.listdir("./mnist_data")

for file in files:
    if not file.endswith(".jpg"):
        continue

    image = Image.open(f"./mnist_data/{file}")
    image = image.resize((28, 28))
    image = ImageOps.invert(image)
    image = image.convert("L")
    image = image.point(lambda x: bw(x) , "1")
    image.show()
    image_data = image.getdata()
    print(ml.predict_num(image_data))
