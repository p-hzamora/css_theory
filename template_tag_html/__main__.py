from flask import Flask
from app.config import Config


def create_app(config_class=Config):
    from app.components.home import bp as home_bp
    from app.components.staff import bp as staff_bp
    from app.components.login import bp as login_bp

    app = Flask(__name__, template_folder="/templates", static_folder="static")
    app.config.from_object(config_class)
    app.json.sort_keys = False

    app.register_blueprint(home_bp)
    app.register_blueprint(staff_bp, url_prefix="/staffs")
    app.register_blueprint(login_bp, url_prefix="/login")

    return app


create_app().run(port=5555, host="0.0.0.0")
