from flask import Blueprint, jsonify, request


from app.models import CityModel
from app.extensions import db

bp = Blueprint(
    "city",
    __name__,
    static_folder="static",
    template_folder="templates",
    static_url_path="/static/city",
)


@bp.route("/", methods=["GET"])
def index():
    return jsonify({"message":"Welcome to the city API"}), 200

@bp.route("/cities", methods=["GET"])
def cities():
    model = CityModel(db)
    limit = request.args.get("limit",type=int)
    if limit:
        values = model.limit(limit).select(flavour=dict)
        return jsonify({"limit":limit,"model": model._model.__table_name__,"data":values}) 
    return jsonify(model.select(flavour=dict))

@bp.route("/cities/<int:id>", methods=["GET"])
def get_city_by_id(id:int):
    city = CityModel(db).where(lambda c: c.city_id == id, id = id).select(flavour=dict)

    if city:
        return jsonify(city)
    return jsonify({"error":"City not found"}), 404