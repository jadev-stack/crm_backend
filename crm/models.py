from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DATETIME, Float
from database.crmbdd import Base
from sqlalchemy.orm import relationship
from login.models import *


class Sede(Base):
    __tablename__ = "sede"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30))

    rcarga = relationship("Rcarga")
    user_data = relationship("User_Data")


class Flota(Base):
    __tablename__ = "flota"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    placa = Column(String(30))


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

    user_cargo = relationship("User_Cargo")
