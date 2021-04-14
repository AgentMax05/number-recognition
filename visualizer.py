

# shows images in ml_model.json converted from array to image
# a random number is chosen every time the program is run

import json
from PIL import Image
import numpy as np
import random

with open("ml_model.json", "r") as json_file:
    json_data = json.load(json_file)

for i in json_data[str(random.randint(0, 9))]:
    array = np.array(i)
    array = np.reshape(array, (28, 28))

    img = Image.fromarray(array)
    img.show()
    input()