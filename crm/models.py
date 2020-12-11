from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DATETIME, Float
from database.crmbdd import Base
from sqlalchemy.orm import relationship


class Sede(Base):
    __tablename__ = "sede"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30))

    rcarga = relationship("Rcarga")


class Division(Base):
    __tablename__ = "division"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30))

    rcarga_ruta = relationship("Rcarga_Ruta")
    rcarga = relationship("Rcarga", back_populates="rcarga_division")


class Cargo(Base):
    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30))
