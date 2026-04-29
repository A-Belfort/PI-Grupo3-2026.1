from app.extensions import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CoordenadorCurso(Base):
    __tablename__ = "coordenador_curso"

    id_coordenador: Mapped[int] = mapped_column(ForeignKey("coordenador.id"),
                                                primary_key=True)
    id_curso: Mapped[int] = mapped_column(ForeignKey("curso.id"),
                                          primary_key=True)
    coordenador: Mapped["Coordenador"] = relationship(back_populates="cursos")
    curso: Mapped["Curso"] = relationship(back_populates="coordenadores")
