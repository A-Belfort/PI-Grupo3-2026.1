from flask import Blueprint, request
from app.controllers import criar_submissao_controller, validar_submissao_controller
from middlewares import verificar_role


bp = Blueprint("submissao", __name__, url_prefix="/api/submissoes")


@bp.route("/criar/<int:id_aluno>", methods=["POST"])
@verificar_role(["aluno"])
def criar_submissao(id_aluno):
    try:
        response, status = criar_submissao_controller(id_aluno)
        return response, status

    except Exception as e:
        print(f"Erro ao criar submissão: {e}")
        return {
            "success": False,
            "message": "Erro ao criar submissão."
        }, 500


bp.route("/validar/<int:id_submissao>", methods=["PUT"])
@verificar_role(["coordenador"])
def validar_submissao(id_submissao):
    try:
        data = request.get_json()
        response, status = validar_submissao_controller(id_submissao, data)
        return response, status
    except Exception as e:
        print(f"Erro ao validar submissão: {e}")
        return {
            "sucess": False,
            "message": "Erro ao validar submissão."
        }, 500
        