from app.extensions import Base
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Usuario(Base):
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False,
                                       unique=True)
    senhaHash: Mapped[str] = mapped_column(String(300), nullable=False)
    tipo: Mapped[str] = mapped_column(String(100), nullable=False)
    matricula: Mapped[Optional[str]] = mapped_column(String(100), unique=True)
    cursos: Mapped[list["AlunoCurso"]] = relationship(back_populates="usuario")
    submissoes: Mapped[Optional[list["Submissao"]]] = relationship(back_populates="usuario")
