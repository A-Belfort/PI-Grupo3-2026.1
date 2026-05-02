from flask import Blueprint, request
from middlewares import verificar_role
from app.controllers import cadastrar_curso_controller


bp = Blueprint("curso", __name__, url_prefix="/api/cursos")


@bp.route("/cadastrar", methods=["POST"])
@verificar_role(["super_admin"])
def cadastrar_usuario():
    try:
        data = request.get_json()
        response, status = cadastrar_curso_controller(data)
        return response, status

    except Exception as e:
        print(f"Erro ao cadastrar curso: {e}")
        return {
            "success": False,
            "message": "Erro ao cadastrar curso."
        }, 500
