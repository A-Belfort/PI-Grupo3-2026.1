from flask import Flask
from .extensions import db, migrate, jwt
from app.models.aluno import Aluno


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql+pymysql://<YOUR_USERNAME>:<YOUR_PASSWORD>@localhost/sigac"
    )

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app import models

    return app
