from flask import Blueprint, jsonify, request


from app.models import Staff, StaffModel
from app.extensions import db
from app.extensions.orm import Error
from app.extensions.orm import ConditionType
from app.extensions.orm import JoinType

bp = Blueprint(
    "staff",
    __name__,
    static_folder="static",
    template_folder="templates",
    static_url_path="/static/staff",
)

model = StaffModel(db)


@bp.route("/", methods=["GET"])
def staffs():
    limit = request.args.get("limit", type=int)
    if limit:
        values = model.limit(limit).select()
        return jsonify({"limit": limit, "data": [x.to_dict() for x in values]})
    res: tuple[Staff] = model.select(lambda x: (x,))[0]

    new_res = []
    for s in res:
        new_res.append(s.to_dict())
    return jsonify(new_res)


@bp.route("/<int:id>", methods=["GET"])
def get_city_by_id(id: int):
    staff = model.where(lambda s: s.staff_id == id, id=id).select()[0]

    if staff:
        return jsonify(staff.to_dict())
    return jsonify({"error": "Staff not found"}), 404


@bp.route("/<int:id>", methods=["PUT", "PATCH"])
def put_staff_id(id: int):
    try:
        staff = model.where(lambda s: s.staff_id == id, id=id).select()

        if not staff:
            return jsonify({"error": "Staff does not exist"}), 404

        staff = staff[0]
        for key, value in request.json.items():
            setattr(staff, key, value)
        model.upsert(staff)
    except Error as err:
        return jsonify({"error": err.msg}), 409
    except Exception:
        return jsonify({"error": "Internal Error"}), 500
    else:
        return jsonify(staff.to_dict()), 201


@bp.route("/", methods=["POST"])
def post_staff_id():
    try:
        staff = Staff(**request.get_json())
        model.insert(staff)
    except Error as err:
        return jsonify({"error": err.msg}), 409
    except Exception:
        return jsonify({"error": "Internal Error"}), 500
    else:
        return jsonify(staff.to_dict()), 201


@bp.route("/<int:id>", methods=["DELETE"])
def delete_staff_id(id: int):
    try:
        model.where(lambda s: s.staff_id == id, id=id).delete()
        return "", 204
    except Error as err:
        return jsonify({"error": err.msg}), 409
    except Exception:
        return jsonify({"error": "Staff not found"}), 404
