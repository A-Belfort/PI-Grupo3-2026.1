from flask import Blueprint, request
from app.controllers import login_controller


bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        response, status = login_controller(data)
        return response, status

    except Exception as e:
        print(f"Erro ao efetuar login: {e}")
        return { 
            "success": False,
            "message": "Erro ao efetuar login."
        }, 500