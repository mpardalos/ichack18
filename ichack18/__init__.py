import sys
from pathlib import Path

from flask import Flask

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
    app.config.update(
        DEBUG=True,
        SECRET_KEY='DevKey',
    )


from . import endpoints
