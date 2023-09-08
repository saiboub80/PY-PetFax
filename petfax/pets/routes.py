from flask import Blueprint, render_template
import json 

pets = json.load(open('pets.json',encoding='utf-8'))

pet = Blueprint('pet', __name__)

@pet.route('/')
def index(): 
    return render_template('pet/index.html', pets=pets)

@pet.route('/<int:id>')
def show(id): 
    pet = pets[id - 1]
    return render_template('pet/show.html', pet=pet)