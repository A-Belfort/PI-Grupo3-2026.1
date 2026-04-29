from app.extensions import db
from sqlalchemy import select
from app.models import Usuario
from werkzeug.security import generate_password_hash, check_password_hash


def crypto_senha(senha):
    pass_hash = generate_password_hash(senha)
    return pass_hash


def decrypto_senha(email_usuario, senha):
    senha_hash = db.session.execute(
        select(Usuario.senhaHash).filter_by(email=email_usuario)
    ).scalar_one_or_none()

    result = check_password_hash(senha_hash, senha)
    return result


def cadastrar_usuario_controller(data):
    senha = crypto_senha(data['senha'])

    new_usuario = Usuario(
        nome=data['nome'],
        email=data['email'],
        senhaHash=senha,
        tipo=data['tipo'],
        matricula=data['matricula']
    )

    db.session.add(new_usuario)
    db.session.commit()

    return {
        "success": True,
        "message": "Cadastro efetuado com sucesso."
    }, 201


def login_controller(data):
    result = decrypto_senha(data['email'], data['senha'])

    if result:
        return {
            "success": True,
            "message": "Login efetuado com sucesso!"
        }, 200

    return {
        "success": False,
        "message": "Erro ao efetuar login."
    }, 401