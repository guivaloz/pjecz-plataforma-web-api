"""
Peritos, modelos
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Perito(Base, UniversalMixin):
    """Perito"""

    # Nombre de la tabla
    __tablename__ = "peritos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    distrito_id = Column(Integer, ForeignKey("distritos.id"), index=True, nullable=False)
    distrito = relationship("Distrito", back_populates="peritos")

    # Clave foránea
    perito_tipo_id = Column(Integer, ForeignKey("peritos_tipos.id"), index=True, nullable=False)
    perito_tipo = relationship("PeritoTipo", back_populates="peritos")

    # Columnas
    nombre = Column(String(256), nullable=False)
    domicilio = Column(String(256), nullable=False)
    telefono_fijo = Column(String(64))
    telefono_celular = Column(String(64))
    email = Column(String(256))
    notas = Column(String(256))
