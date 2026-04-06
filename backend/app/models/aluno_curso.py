from app.extensions import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class AlunoCurso(Base):
    __tablename__ = "aluno_curso"
    id_aluno: Mapped[int] = mapped_column(ForeignKey("usuario.id"),
                                          primary_key=True)
    id_curso: Mapped[int] = mapped_column(ForeignKey("curso.id"),
                                          primary_key=True)
    aluno: Mapped["Usuario"] = relationship(back_populates="aluno_curso")
    curso: Mapped["Curso"] = relationship(back_populates="aluno_curso")
