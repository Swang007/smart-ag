from flask import render_template, request, Blueprint
from smartag import db
from smartag.plants.models import PlantType, Plant
from sqlalchemy import desc
# from smartag.models import Post

plants = Blueprint('plants', __name__)

@plants.route("/type/<string:ptype>/<int:uid>")
def plant_details(ptype, uid):
    print(ptype, uid)
    plant = Plant.query.filter(Plant.name == ptype, Plant.uid == uid).order_by(Plant.timestamp.desc()).first()
    print(plant)
    return render_template('plantDetail.html', plant=plant)