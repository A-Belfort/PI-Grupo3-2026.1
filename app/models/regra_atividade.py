from app.extensions import Base
from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column


class RegraAtividade(Base):
    __tablename__ = "regra_atividade"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    area: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(String(300), nullable=False)
    limite_horas: Mapped[int] = mapped_column(Integer, nullable=False)
    requisito: Mapped[str] = mapped_column(String(100), nullable=False)
    exige_certificado: Mapped[int] = mapped_column(Boolean, nullable=False)
    
    