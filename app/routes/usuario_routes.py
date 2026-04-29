from flask import Blueprint, request, jsonify
from app.controllers import cadastrar_usuario_controller, login_controller


bp = Blueprint('usuario', __name__, url_prefix='/api/usuarios')


@bp.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    try:
        data = request.get_json()
        response, status = cadastrar_usuario_controller(data)
        return jsonify(response), status

    except Exception as e:
        print(f"Erro ao efetuar cadastro: {e}")
        return jsonify({
            "success": False,
            "message": "Erro ao efetuar cadastro."
        }), 500


@bp.route('/login', methods=['POST'])
def login_admin():
    try:
        data = request.get_json()
        response, status = login_controller(data)
        return jsonify(response), status

    except Exception as e:
        print(f"Erro ao efetuar login: {e}")
        return jsonify({ 
            "success": False,
            "message": "Erro ao efetuar login."
        }), 500
