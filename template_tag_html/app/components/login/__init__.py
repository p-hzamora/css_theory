from flask import Blueprint, jsonify, request

from app.utils.security import Auth

from app.models.user import User, UserModel
from app.extensions import db
from app.extensions.orm.orm.databases.my_sql import Error

bp = Blueprint(
    "login",
    __name__,
    static_folder="static",
    template_folder="templates",
    static_url_path="/static/login",
)

model = UserModel(db)


@bp.route("/", methods=["POST"])
def login():
    try:
        email = request.json.get("email", None)
        password = request.json.get("password", None)

        if not all([email, password]):
            return jsonify({"success": False, "msg": "you must specified 'email' and 'password' attributes in body"})

        user = model.where(lambda u: u.email == email, email=email).where(lambda u: u.password == password, password=password).select_one()

        if not user:
            return jsonify({"success": False, "msg": "email or password not valid"})

        token = Auth.generate_token(user)
        return jsonify({"success": True, "token": token})

    except Exception as e:
        return jsonify(
            {
                "success": False,
                "type": "Program Execution",
                "error": "Internal Error",
                "traceback": str(e),
            }
        ), 500


@bp.route("/register", methods=["POST"])
def register():
    try:
        user = User(**request.json)
        model.insert(user)

    except Error as err:
        return jsonify({"type": "database", "error": err.msg}), 409

    except Exception as e:
        return jsonify({"type": "Program Execution", "error": "Internal Error", "traceback": str(e)}), 500

    else:
        return "", 204
