import csv
import random
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

test_data = np.array([['40', 'Other']])

print(test_data)

ageLower = 0
ageUpper = 60
genderDict = {'Male': 0, 'Female': 1, 'Other': 0.5}
movies = ['Inception', 'The Matrix', 'Star Wars', 'Twilight', 'The Godfather', 'Harry Potter', 'Lord of the Rings',
          'Die Hard', 'The Fault in our Stars', 'Deadpool', 'IT', 'Alien', 'Saw', "Shawshank Redmemption",
          "The Hunger Games", "12 Angry Men", "Inside Out", "The Incredibles", "The Dark Knight", "Despicable Me",
          "Inside Out", "Hot Fuzz", "Rush Hour", "Shaun of the dead", "Pitch Perfect"]

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model.h5")
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

raw_input = [[int(x[0]) / (ageUpper - ageLower), genderDict[x[1]]] for x in test_data]
training_set_raw_inputs = np.array(raw_input).astype(float)


output = model.predict(training_set_raw_inputs, batch_size=1)
outputIndex = [np.argmax(x) for x in output]

result = movies[outputIndex[0]]

print(result)
