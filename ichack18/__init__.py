import os
import sys
from pathlib import Path

from flask import Flask, Blueprint

app = Flask(__name__)

api = Blueprint("api", __name__)

if 'dev' in sys.argv:
    app.config.update(
        DEBUG=True,
        SECRET_KEY='DevKey',
    )

# noinspection PyPep8
from . import endpoints

app.register_blueprint(api, url_prefix="/api")
