from flask import Flask
from app.config import Config


def create_app(config_class=Config):
    from app.components.staff import bp as staff_bp

    app = Flask(__name__, template_folder="/templates", static_folder="static")
    app.config.from_object(config_class)
    app.json.sor = False
    app.register_blueprint(staff_bp, url_prefix="/staff")

    return app


create_app().run(port=5000, host="0.0.0.0")

