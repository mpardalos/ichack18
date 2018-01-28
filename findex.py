import sys
from pathlib import Path

from flask import Flask, request, jsonify, Response
from keras.models import model_from_json
import numpy as np

app = Flask(__name__)

age_lower = 0
age_upper = 60
age_range = age_upper - age_lower
genders = {'Male': 0, 'Female': 1, 'Other': 0.5}
movies = ['Inception', 'The Matrix', 'Star Wars', 'Twilight', 'The Godfather', 'Harry Potter', 'Lord of the Rings',
          'Die Hard', 'The Fault in our Stars', 'Deadpool', 'IT', 'Alien', 'Saw', "Shawshank Redmemption",
          "The Hunger Games", "12 Angry Men", "Inside Out", "The Incredibles", "The Dark Knight", "Despicable Me",
          "Inside Out", "Hot Fuzz", "Rush Hour", "Shaun of the dead", "Pitch Perfect"]
models_dir = Path(__file__).parent / 'models'


if 'dev' in sys.argv:
    app.config.update(DEBUG=True)


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

@app.route('/recomend')
def recomend_endpoint():
    age = int(request.args.get('age'))
    gender = request.args.get('gender')

    resp = jsonify({'recomendation': recomend(age, gender)})
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp
