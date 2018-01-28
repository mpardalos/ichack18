import csv
import random
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

batchSize = 100

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model.h5")
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

output = model.predict(training_set_raw_inputs, batch_size=batchSize)

<<<<<<< HEAD
outputIndex = [np.argmax(x) for x in output]
print(outputIndex)
=======
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
>>>>>>> 471d63ecaff517dd71a68015ed420cf4161506de
