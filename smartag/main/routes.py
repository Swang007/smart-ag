from flask import render_template, request, Blueprint
from smartag.plants.models import PlantType, Plant
# from smartag.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    plant_types = PlantType.query.all()
    print(plant_types)
    return render_template('charts.html', plant_types=plant_types)

@main.route("/type/<string:ptype>")
def type_details(ptype):
    print(ptype)
    plants = Plant.query.filter(Plant.name == ptype).order_by(Plant.uid).all()

    unique_plants = []
    for plant in plants:
        if len(unique_plants) == 0:
            unique_plants.append(plant)
        else:
            add = True
            for up in unique_plants:
                if up.uid == plant.uid:
                    add = False
            if add:
                unique_plants.append(plant)
    
    return render_template('typeDetail.html', plants=unique_plants)