from flask import Flask
from .extensions import db, migrate, jwt
from app.models.aluno import Aluno
from dotenv import load_dotenv
import os

def create_app() -> Flask:
    app = Flask(__name__)

    load_dotenv()
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("MYSQL_URI")

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app import routes
    app.register_blueprint(routes.auth_bp, url_prefix='/api/usuario')

    return app
