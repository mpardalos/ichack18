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

outputIndex = [np.argmax(x) for x in output]
print(outputIndex)
