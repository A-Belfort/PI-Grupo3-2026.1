from app.extensions import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Coordenador(Base):
    __tablename__ = "coordenador"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False,
                                       unique=True)
    senhaHash: Mapped[str] = mapped_column(String(300), nullable=False)
    cursos: Mapped[list["CoordenadorCurso"]] = relationship(back_populates="coordenador")
    submissoes: Mapped[list["Submissao"]] = relationship(back_populates="coordenador")