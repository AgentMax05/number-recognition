from PIL import Image
import numpy as np
import json

json_data = {str(i): [] for i in range(10)}

def train_model(image_list):
    for image in image_list:
        real_num = image[0]
        image = image[1:]

        image_array = np.array(image)
        image_array = np.reshape(image_array, (28, 28))

        pil_image = Image.fromarray(image_array.astype(np.uint8))
        pil_image = pil_image.convert("1")

        image_data = pil_image.getdata()

        json_data[real_num].append(tuple(image_data))

def save_json_model():
    with open("ml_model.json", "w") as json_file:
        json.dump(json_data, json_file)