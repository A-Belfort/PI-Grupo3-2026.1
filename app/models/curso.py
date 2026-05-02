from app.extensions import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column


class Curso(Base):
    __tablename__ = "curso"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    carga_horaria: Mapped[int] = mapped_column(Integer, nullable=False)