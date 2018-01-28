from flask import render_template, request

from . import app
from . import data_codes
from .predictions import recomend


@app.route('/')
def root():
    return render_template("index.html",
        genders=data_codes.genders,
        group_types=data_codes.group_types,
        countries=data_codes.countries
    )


@app.route('/recomend')
def recomend_endpoint():
    age = int(request.args.get('age'))
    gender = request.args.get('gender')

    return recomend(age, gender)
