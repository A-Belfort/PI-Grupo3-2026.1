from app.extensions import db
from app.models import Curso



def cadastrar_curso_controller(data):
    new_curso = Curso(
        nome=data["nome"],
        carga_horaria=data["carga_horaria"]
    )
    
    db.session.add(new_curso)
    db.session.commit()
    
    return {
        "success": True,
        "message": "Curso cadastrado com sucesso."
    }, 201