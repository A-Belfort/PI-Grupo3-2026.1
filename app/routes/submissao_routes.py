from flask import Blueprint, request
from app.controllers import criar_submissao_controller, listar_submissoes_controller, validar_submissao_controller
from app.middlewares import verificar_role


bp = Blueprint("submissao", __name__, url_prefix="/api/submissoes")


@bp.route("/criar", methods=["POST"])
@verificar_role(["aluno"])
def criar_submissao():
    try:
        data = request.json()
        response, status = criar_submissao_controller(data)
        return response, status

    except Exception as e:
        print(f"Erro ao criar submissão: {e}")
        return {
            "success": False,
            "message": "Erro ao criar submissão."
        }, 500


@bp.route("/listar", methods=["GET"])
@verificar_role(["aluno", "coordenador", "super_admin"])
def listar_submissoes():
    try:
        id_curso = request.args.get("curso")
        response, status = listar_submissoes_controller(id_curso)
        return response, status
    
    except Exception as e:
        print(f"Erro ao listar submissões: {e}")
        return {
            "success": False,
            "message": "Erro ao listar submissões."
        }


@bp.route("/validar/<int:id_submissao>", methods=["PUT"])
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
        

