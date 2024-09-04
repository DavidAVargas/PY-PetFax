from flask import Blueprint, render_template 

bp = Blueprint('pet', __name__, url_prefix="/pets")

import json

with open('pets.json') as f:  
    pets = json.load(f)

print(pets)

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

