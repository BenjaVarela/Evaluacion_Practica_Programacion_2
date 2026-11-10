from typing import List
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Equipo(Base):
    __tablename__ = "equipo"
    equipo_id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    tipo: Mapped[str] = mapped_column(String(50), nullable=False)
    stock_disponible: Mapped[int] = mapped_column(nullable=False)
    prestamos: Mapped[List["Prestamo"]] = relationship(back_populates="equipo")

class Estudiante(Base):
    __tablename__ = "estudiante"
    estudiante_id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    correo: Mapped[str] = mapped_column(String(100), nullable=False)
    prestamos: Mapped[List["Prestamo"]] = relationship(back_populates="estudiante")

class Prestamo(Base):
    __tablename__ = "prestamo"
    prestamo_id: Mapped[int] = mapped_column(primary_key=True)
    estudiante_id: Mapped[int] = mapped_column(ForeignKey('estudiante.estudiante_id'), nullable=False)
    equipo_id: Mapped[int] = mapped_column(ForeignKey('equipo.equipo_id'), nullable=False)
    fecha_prestamo: Mapped[str] = mapped_column(nullable=False)
    cantidad: Mapped[int] = mapped_column(nullable=False)
    estado: Mapped[str] = mapped_column(String(20), nullable=False)
    estudiante: Mapped["Estudiante"] = relationship(back_populates="prestamos")
    equipo: Mapped["Equipo"] = relationship(back_populates="prestamos")