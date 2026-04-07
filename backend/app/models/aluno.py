from app.extensions import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Aluno(Base):
    __tablename__ = "aluno"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False,
                                       unique=True)
    senhaHash: Mapped[str] = mapped_column(String(300), nullable=False)
    matricula: Mapped[str] = mapped_column(String(100), unique=True)
    cursos: Mapped[list["AlunoCurso"]] = relationship(back_populates="aluno")
    submissoes: Mapped[list["Submissao"]] = relationship(back_populates="aluno")
