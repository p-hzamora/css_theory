from collections import defaultdict
from flask import Blueprint, jsonify, request
from functools import wraps

from app.models.staff import Staff, StaffModel, StaffValidator
from app.extensions import db
from app.extensions.orm import Error
from app.utils.security import Auth

bp = Blueprint(
    "staff",
    __name__,
    static_folder="static",
    template_folder="templates",
    static_url_path="/static/staff",
)

model = StaffModel(db)


def jwt_required(foo: object):
    @wraps(foo)
    def wrapped(*args, **kwargs):
        print(request.headers)
        if Auth.verify_token(request.headers):
            return foo(*args, **kwargs)
        
        return jsonify({"success": False, "msg": "invalid token"}), 400
    return wrapped


def validate_model(instance: Staff) -> tuple[bool, dict[str, str]]:
    validate = StaffValidator().validate(instance)
    serialize: dict[str, list[str, str]] = defaultdict(list)

    if not validate.is_valid:
        for err in validate.errors:
            serialize[err.PropertyName].append(err.ErrorMessage)
    return tuple([validate.is_valid, serialize])


@bp.route("/", methods=["GET"])
@jwt_required
def staffs():
    limit = request.args.get("limit", type=int)
    if limit:
        values = model.limit(limit).select()[0]
        return jsonify({"limit": limit, "data": [x.to_dict() for x in values]})
    res: tuple[Staff] = model.select(lambda x: (x,))[0]

    new_res = []
    for s in res:
        new_res.append(s.to_dict())
    return jsonify(new_res)


@bp.route("/<int:id>", methods=["GET"])
@jwt_required
def get_city_by_id(id: int):
    try:
        staff = model.where(lambda s: s.staff_id == id, id=id).select_one()

        if not staff:
            return jsonify({"type": "database", "error": "Staff not found"}), 404
        return jsonify(staff.to_dict())
    except Exception as e:
        return jsonify({"type": "database", "error": "Internal Error", "traceback": str(e)}), 500


@bp.route("/<int:id>", methods=["PUT"])
@jwt_required
def put_staff_id(id: int):
    try:
        staff: Staff = Staff(**request.json)
        staff.staff_id = id

        is_valid, err_msg = validate_model(staff)
        if not is_valid:
            return jsonify({"type": "fluent_validation", "error": err_msg}), 409

        model.upsert(staff)
    except Error as err:
        return jsonify({"type": "database", "error": err.msg}), 409
    except Exception as e:
        return jsonify({"type": "Program Execution", "error": "Internal Error", "traceback": str(e)}), 500
    else:
        return jsonify(staff.to_dict()), 201


@bp.route("/<int:id>", methods=["PATCH"])
@jwt_required
def patch_staff_id(id: int):
    try:
        model.where(lambda s: s.staff_id == id, id=id).update(request.json)
    except Error as err:
        return jsonify({"type": "database", "error": err.msg}), 409
    except Exception as e:
        return jsonify({"type": "Program Execution", "error": "Internal Error", "traceback": str(e)}), 500
    else:
        return "", 204


@bp.route("/", methods=["POST"])
@jwt_required
def post_staff_id():
    try:
        staff = Staff(**request.get_json())
        is_valid, err_msg = validate_model(staff)
        if not is_valid:
            return jsonify({"type": "fluent_validation", "error": err_msg}), 409
        model.insert(staff)

    except Error as err:
        return jsonify({"type": "database", "error": err.msg}), 409
    except Exception as e:
        return jsonify({"type": "Program Execution", "error": "Internal Error", "traceback": str(e)}), 500
    else:
        return jsonify(staff.to_dict()), 201


@bp.route("/<int:id>", methods=["DELETE"])
@jwt_required
def delete_staff_id(id: int):
    try:
        staff = model.where(lambda s: s.staff_id == id, id=id).select_one()
        if not staff:
            return jsonify({"type": "database", "error": "Staff not found"}), 404

        model.delete(staff)
        return "", 204
    except Error as err:
        return jsonify({"type": "database", "error": err.msg}), 409
    except Exception as e:
        return jsonify({"type": "Program Execution", "error": "Internal Error", "traceback": str(e)}), 500
