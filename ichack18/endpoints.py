from . import api

@api.route('/')
def root():
    return "Heeeeeeey"
