import pickle
from pathlib import Path

from keras.models import model_from_json
import numpy as np

from . import genders, models_dir, age_range, movies


def recomend(age: int, gender: str):
    if gender not in genders:
        raise ValueError("Gender must be one of {}".format(', '.join(genders)))

    # Model has to be loaded every time it's used FOR SOME FUCKING REASON
    with open(str(models_dir / 'model.json'), 'r') as json_file:
        loaded_model_json = json_file.read()
        model = model_from_json(loaded_model_json)
    model.load_weights(str(models_dir / "model.h5"))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    data = np.array([[age / age_range, genders[gender]]])

    output = model.predict(data, batch_size=1)
    outputIndex = np.argmax(output[0])

    return movies[outputIndex]

