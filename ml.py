import json
import math

with open("ml_model.json", "r") as json_file:
    json_data = json.load(json_file)

def predict_num(image_data):

    closest = [(math.inf, None) for i in range(7)]

    for num in range(10):
        num = str(num)

        for image_index, pixels in enumerate(json_data[num]):
            distance = find_distance(pixels, image_data)
            for index, obj in enumerate(closest):
                if distance < obj[0]:
                    closest.insert(index, (distance, num))
                    closest.pop(-1)
                    break

    counters = {str(i): 0 for i in range(10)}
    for index, i in enumerate(closest):
        counters[i[1]] += 1 / ((index + 1) * 0.8)

    largest = (-math.inf, None)
    for key in counters.keys():
        if counters[key] > largest[0]:
            largest = (counters[key], key)

    each_prob = {str(i): 0 for i in range(10)}
    for num in range(10):
        for obj in closest:
            if obj[1] == str(num):
                each_prob[str(num)] += 1

    print(each_prob)

    return (largest[1], round(each_prob[largest[1]] / 7 * 100, 2))
    return f"Guess: {largest[1]}, Confidence: {round((each_prob[largest[1]] / 7) * 100, 2)}%"

def find_distance(image1, image2):
    return math.dist((i / 255 for i in image1), (i / 255 for i in image2))