from app.extensions import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CoordenadorCurso(Base):
    __tablename__ = "coordenador_curso"

    id_coordenador: Mapped[int] = mapped_column(ForeignKey("usuario.id"),
                                                primary_key=True)
    id_curso: Mapped[int] = mapped_column(ForeignKey("curso.id"),
                                          primary_key=True)
    aluno: Mapped["Usuario"] = relationship(back_populates="coordenador_curso")
    curso: Mapped["Curso"] = relationship(back_populates="coordenador_curso")
