import csv
import training

with open("./mnist_data/mnist_train.csv", "r") as mnist_data_file:
    csv_reader = csv.reader(mnist_data_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        training.train_model([row])
        line_count += 1

        if line_count == 30000:
            print("done")
            break

    training.save_json_model()