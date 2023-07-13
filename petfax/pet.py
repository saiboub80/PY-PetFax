import json
pets=json.load(open('pets.json'))
from flask import (Blueprint, render_template)
print(pets)
bp= Blueprint('pet', __name__, url_prefix="/pets" )

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)
