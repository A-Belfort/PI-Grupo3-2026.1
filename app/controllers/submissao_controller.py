from app.extensions import db
from app.models import Submissao
from sqlalchemy import select


def criar_submissao_controller(id_aluno):
    nova_submissao = Submissao(
        id_aluno=id_aluno,
        status="rascunho"
    )

    db.session.add(nova_submissao)
    db.session.commit()

    return {
        "success": True,
        "message": "Submetido com sucesso."
    }, 201
    
    
def validar_submissao_controller(id_submissao, data):
    query = select(Submissao).where(Submissao.id == id_submissao)
    submissao = db.session.execute(query).scalar_one_or_none()
    
    if not submissao:
        return {
            "success": False,
            "message": "Submissão não encontrada."
        }, 404
        
    if data["status"] not in ("aprovado", "recusado"):
        return {
            "success": False,
            "message": "Status informado inválido."
        }, 400
        
    submissao.status = data["status"]
    submissao.id_coordenador = data["id_coordenador"]
    if data["status"] == "recusado":
        submissao.motivo_rejeicao = data.get("motivo_rejeicao")
        
    db.session.commit()
    
    return {
        "success": True,
        "message": "Submissão validada com sucesso."
    }, 200