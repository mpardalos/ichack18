import sys

from flask import Flask

app = Flask(__name__)

if 'dev' in sys.argv:
    app.config.update(
        DEBUG=True,
        SECRET_KEY='DevKey',
    )

from . import endpoints
