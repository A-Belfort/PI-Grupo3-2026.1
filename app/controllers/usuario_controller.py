from app.extensions import db
from app.models import Usuario
from werkzeug.security import generate_password_hash
from flask_jwt_extended import get_jwt


def cadastrar_usuario_controller(data):
    role = get_jwt().get("role")

    tipo_novo_usuario = data["tipo"]

    if role == "coordenador" and tipo_novo_usuario != "aluno":
        return {
            "success": False,
            "message": "Coordenador só pode cadastrar alunos."
        }, 403
        
    if role == "super_admin" and tipo_novo_usuario not in ("aluno", "coordenador"):
        return {
            "success": False,
            "message": "Tipo de usuário inválido."
        }, 400
        
    if tipo_novo_usuario == "aluno" and not data.get("matricula"):
        return {
            "success": False,
            "message": "Aluno precisa de matrícula."
        }, 400    
    
    senha_hash = generate_password_hash(data["senha"])

    novo_usuario = Usuario(
        nome=data["nome"],
        email=data["email"],
        senha=senha_hash,
        tipo=data["tipo"],
        matricula=data.get("matricula")
    )

    db.session.add(novo_usuario)
    db.session.commit()

    return {
        "success": True,
        "message": "Cadastro efetuado com sucesso."
    }, 201
