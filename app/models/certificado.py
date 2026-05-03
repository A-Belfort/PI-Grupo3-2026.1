from app.extensions import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Certificado(Base):
    __tablename__ = "certificado"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome_arquivo: Mapped[str] = mapped_column(String(100), nullable=False)
    url_arquivo: Mapped[str] = mapped_column(String(300), nullable=False)