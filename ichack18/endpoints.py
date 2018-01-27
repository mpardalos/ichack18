from flask import render_template

from . import app
from . import data_codes


@app.route('/')
def root():
    return render_template("index.html", 
        genders=data_codes.genders,
        group_types=data_codes.group_types,
        countries=data_codes.countries
    )



