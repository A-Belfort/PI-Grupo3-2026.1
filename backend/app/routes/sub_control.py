from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Submissao


bp = Blueprint('alunos',__name__, url_prefix='/api/submissoes')

@bp.route('/nova_submissao', methods=['POST'])
def criar_submissao():
    try:
        data = request.json
        return jsonify({"success": False, "message": "Submetido com sucesso"}), 201
    except Exception as e:
        print(f"Erro ao submeter certificado: {e}")
        return jsonify({"success": False, "message": "Erro ao submeter certificado."}), 500