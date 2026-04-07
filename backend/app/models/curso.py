from app.extensions import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Curso(Base):
    __tablename__ = "curso"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    carga_horaria_minima: Mapped[int] = mapped_column(nullable=False)
    alunos: Mapped[list["AlunoCurso"]] = relationship(back_populates="curso")
    coordenadores: Mapped[list["CoordenadorCurso"]] = relationship(back_populates="curso")
