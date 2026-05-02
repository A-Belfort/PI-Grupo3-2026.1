from app.extensions import db
from app.models import Usuario
from werkzeug.security import generate_password_hash

def cadastrar_usuario_controller(data):
    senha_hash = generate_password_hash(data["senha"])

    new_usuario = Usuario(
        nome=data["nome"],
        email=data["email"],
        senha=senha_hash,
        tipo=data["tipo"],
        matricula=data.get("matricula")
    )

    db.session.add(new_usuario)
    db.session.commit()

    return {
        "success": True,
        "message": "Cadastro efetuado com sucesso."
    }, 201
