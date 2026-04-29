from app.extensions import db
from app.models import Submissao


def criar_submissao_controller(data):
    nova_submissao = Submissao(
        titulo=data["titulo"],
        descricao=data["descricao"]
    )

    db.session.add(nova_submissao)
    db.session.commit()

    return {
        "success": True,
        "message": "Submetido com sucesso"
    }, 201