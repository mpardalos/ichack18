import csv
import random
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

random.seed(0)

ageLower = 0
ageUpper = 60
genderDict = {'Male': 0, 'Female': 1, 'Other': 0.5}
movies = ['Inception', 'The Matrix', 'Star Wars', 'Twilight', 'The Godfather', 'Harry Potter', 'Lord of the Rings',
          'Die Hard', 'The Fault in our Stars', 'Deadpool', 'IT', 'Alien', 'Saw', "Shawshank Redmemption",
          "The Hunger Games", "12 Angry Men", "Inside Out", "The Incredibles", "The Dark Knight", "Despicable Me",
          "Inside Out", "Hot Fuzz", "Rush Hour", "Shaun of the dead", "Pitch Perfect"]

with open('extrapolateTestData.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    raw_data = [r for r in reader if r != []]
    raw_data.pop(0)

    print(raw_data)

    raw_input = [[int(x[0]) / (ageUpper - ageLower), genderDict[x[1]]] for x in raw_data]
    print(raw_input)

    raw_output = [[] * len(movies)] * len(raw_data)
    for x in range(len(raw_data)):
        raw_output[x] = [0] * len(movies)
        raw_output[x][movies.index(raw_data[x][2])] += 1
    print(raw_output)

    training_set_raw_inputs = np.array(raw_input).astype(float)
    training_set_raw_outputs = np.array(raw_output).astype(float)

    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights("model.h5")
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    output = model.predict(training_set_raw_inputs, batch_size=10)

    outputIndex = [np.argmax(x) for x in output]
    rawOutputIndex = [np.argmax(x) for x in training_set_raw_outputs]
    print(outputIndex)
    print(rawOutputIndex)

    print(sum([(x - y) ** 2 for x, y in zip(outputIndex, rawOutputIndex)]))
