from flask import Blueprint, request, jsonify
from app.extensions import db
from sqlalchemy import select
from app.models import Usuario
from werkzeug.security import generate_password_hash, check_password_hash


bp = Blueprint('usuario',__name__, url_prefix='/')

def crypto_senha(senha):
    pass_hash = generate_password_hash(senha)
    return pass_hash

def decrypto_senha(email_usuario,senha):
    senha_hash = db.session.execute(select(Usuario.senhaHash).filter_by(email=email_usuario)).scalar_one_or_none()
    result = check_password_hash(senha_hash,senha)
    return result

@bp.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    try:
        data = request.json
        senha = crypto_senha(data['senha'])
        new_usuario = Usuario(nome=data['nome'],
                              email=data['email'],
                              senhaHash=senha,
                              tipo=data['tipo'],
                              matricula=data['matricula'])
        db.session.add(new_usuario)
        db.session.commit()
        return jsonify({"success": False, "message": "Cadastro efetuado com sucesso."}), 201
    except Exception as e:
        print(f"Erro ao efetuar cadastro: {e}")
        return jsonify({"success": False, "message": "Erro ao efetuar cadastro."}), 500
    
@bp.route('/login', methods=['POST'])
def login_admin():
    try:
        data = request.get_json()
        result = decrypto_senha(data['email'],data['senha'])
        if result: 
            return jsonify({"success": True, "message": "Login efetuado com sucesso!"})
        else:
            raise Exception
    except Exception as e:
        print(f"Erro ao efetuar login: {e}")
        return jsonify({"success": False, "message": "Erro ao efetuar login."}), 500
