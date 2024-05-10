from flask import ( Blueprint, render_template )
bp = Blueprint('pet', __name__, url_prefix='/pets')

import json
pets = json.load(open('pets.json'))
print(pets)


@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

# @bp.route('/<int:id>')
# def show(id): 
#     pet = pets[id - 1]
#     return render_template('pets/show.html', pet=pet)

@bp.route('/<pet_name>')
def pet_show(pet_name):
    pet = next((pet for pet in pets if pet['pet_name'] == pet_name), None)
    return render_template('pets/show.html', pet=pet)