from flask import Blueprint, request
from app.controllers import cadastrar_usuario_controller
from middlewares import verificar_role


bp = Blueprint("usuario", __name__, url_prefix="/api/usuarios")


@bp.route("/cadastrar", methods=["POST"])
@verificar_role(["super_admin", "coordenador"])
def cadastrar_usuario():
    try:
        data = request.get_json()
        response, status = cadastrar_usuario_controller(data)
        return response, status

    except Exception as e:
        print(f"Erro ao efetuar cadastro: {e}")
        return {
            "success": False,
            "message": "Erro ao efetuar cadastro."
        }, 500

