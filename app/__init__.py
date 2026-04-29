from flask import Flask
from .extensions import db, migrate, jwt
from dotenv import load_dotenv
import os
from flask_cors import CORS

def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)

    load_dotenv()
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("MYSQL_URI")

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.routes import bp_usuario, bp_submissao
    app.register_blueprint(bp_usuario)
    app.register_blueprint(bp_submissao)

    return app
