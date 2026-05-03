from app.extensions import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class CoordenadorCurso(Base):
    __tablename__ = "coordenador_curso"
    
    id_coordenador: Mapped[int] = mapped_column(ForeignKey("usuario.id"), primary_key=True)
    id_curso: Mapped[int] = mapped_column(ForeignKey("curso.id"), primary_key=True)
