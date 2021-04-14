import csv
from PIL import Image
import numpy as np

import ml


def get_data(image_pixels):

    label = image_pixels[0]
    image_pixels = image_pixels[1:]
    array = np.array(image_pixels)
    array = np.reshape(array, (28, 28))

    image = Image.fromarray(array.astype(np.uint8))
    image_data = image.getdata()
    image.convert("1")
    return (label, image_data)

def print_results(tests, wrong):
    print(f"Correct: {tests - wrong}, Wrong: {wrong}, success percentage: {((tests - wrong) / tests) * 100}%")

with open("./mnist_data/mnist_test.csv", "r") as mnist_test:
    csv_reader = csv.reader(mnist_test, delimiter=",")
    line_count = 0
    wrong = 0
    lines_skipped = 0
    for row in csv_reader:

        if lines_skipped < 100:
            lines_skipped += 1
            continue

        label, image_data = get_data(row)
        guess = ml.predict_num(image_data)
        correct = str(guess[0]) == str(label)
        print(f"Guess: {guess[0]}, Confidence: {guess[1]}%, Correct Label: {label}, Correct: {correct}")
        if not correct:
            wrong += 1
        line_count += 1

        if line_count == 300:
            print_results(300, wrong)
            break
        # print(f"{guess}; correct label: {label}")
