from flask import Blueprint, request, jsonify
from app.controllers import criar_submissao_controller


bp = Blueprint('submissao', __name__, url_prefix='/api/submissoes')


@bp.route('/nova_submissao', methods=['POST'])
def criar_submissao():
    try:
        data = request.get_json()
        response, status = criar_submissao_controller(data)
        return jsonify(response), status

    except Exception as e:
        print(f"Erro ao submeter certificado: {e}")
        return jsonify({
            "success": False,
            "message": "Erro ao submeter certificado."
        }), 500