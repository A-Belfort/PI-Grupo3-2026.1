from app.extensions import db
from app.models import Submissao
from sqlalchemy import select
from flask_jwt_extended import get_jwt, get_jwt_identity


def criar_submissao_controller(data):
    id_aluno = int(get_jwt_identity())
    nova_submissao = Submissao(
        id_aluno=id_aluno,
        status="pendente",
        id_curso=data["id_curso"],
        id_atividade_complementar=data["id_atividade_complementar"],
        id_certificado=data.get("id_certificado")
    )

    db.session.add(nova_submissao)
    db.session.commit()

    return {
        "success": True,
        "message": "Submetido com sucesso."
    }, 201

    
def listar_submissoes_controller(id_curso=None):
    role = get_jwt().get("role")
    id_usuario = int(get_jwt_identity())
    query = select(Submissao)
    
    if role == "coordenador":
        query = query.where(Submissao.id_coordenador == id_usuario)
        
    elif role == "aluno":
        query = query.where(Submissao.id_aluno == id_usuario)
    
    if id_curso:
        query = query.where(Submissao.id_curso == id_curso)
        
    submissoes = db.session.execute(query).scalars().all()
    
    resultado = [
    {
        "id": submissao.id,
        "status": submissao.status,
        "id_aluno": submissao.id_aluno,
        "id_coordenador": submissao.id_coordenador,
        "motivo_rejeicao": submissao.motivo_rejeicao
    } 
        for submissao in submissoes]
    
    return {
        "success": True,
        "submissoes": resultado
    }, 200
    
    
def validar_submissao_controller(id_submissao, data):
    id_coordenador = int(get_jwt_identity())
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
    submissao.id_coordenador = id_coordenador
    if data["status"] == "recusado":
        submissao.motivo_rejeicao = data.get("motivo_rejeicao")
        
    db.session.commit()
    
    return {
        "success": True,
        "message": "Submissão validada com sucesso."
    }, 200