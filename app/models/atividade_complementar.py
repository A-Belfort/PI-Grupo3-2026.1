from app.extensions import Base
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional


class AtividadeComplementar(Base):
    __tablename__ = "atividade_complementar"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str] = mapped_column(String(300), nullable=False)
    carga_horaria_solicitada: Mapped[int] = mapped_column(Integer, nullable=False)
    carga_horaria_aprovada: Mapped[Optional[int]] = mapped_column(Integer)
    id_regra_atividade: Mapped[int] = mapped_column(ForeignKey("regra_atividade.id"))
    
    