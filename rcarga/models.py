
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DATETIME, Float
from database.crmbdd import Base
from sqlalchemy.orm import relationship
from login.models import User
from crm.models import Sede, Division, Cargo, Flota
from datetime import datetime


class Rcarga_Estatus(Base):
    __tablename__ = "rcarga_estatus"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    estatus = Column(String(30))

    rcarga = relationship("Rcarga", back_populates="rcarga_estatus")


class Rcarga_Ruta(Base):
    __tablename__ = "rcarga_ruta"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ruta = Column(String(50))
    objetivo = Column(Integer)
    division_id = Column(Integer, ForeignKey("division.id"))

    rcarga = relationship("Rcarga", back_populates="rcarga_ruta")


class Rcarga_Despacho(Base):
    __tablename__ = "rcarga_despacho"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    chofer = Column(String(50))
    ayudante = Column(String(50))
    vehiculo = Column(Integer)
    rcarga_id = Column(Integer, ForeignKey("rcarga.id"))

    rcarga = relationship("Rcarga", uselist=False,
                          back_populates="rcarga_despacho")


class Rcarga(Base):
    __tablename__ = "rcarga"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fecha = Column(DATETIME, default=datetime.now())
    total = Column(Float)
    vol = Column(Float)
    numero = Column(Integer)
    ruta_id = Column(Integer, ForeignKey("rcarga_ruta.id"))
    estatus_id = Column(Integer, ForeignKey("rcarga_estatus.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    division_id = Column(Integer, ForeignKey("division.id"))
    sede_id = Column(Integer, ForeignKey("sede.id"))

    rcarga_despacho = relationship(
        "Rcarga_Despacho",  back_populates="rcarga")
    rcarga_item = relationship("Rcarga_Item", back_populates="rcarga")
    rcarga_division = relationship("Division", back_populates="rcarga")
    rcarga_estatus = relationship("Rcarga_Estatus", back_populates="rcarga")
    rcarga_ruta = relationship("Rcarga_Ruta", back_populates="rcarga")


class Rcarga_Item(Base):
    __tablename__ = "rcarga_item"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    docnum = Column(Integer)
    cardname = Column(String)
    cajas = Column(Integer)
    unidad = Column(Integer)
    totalvalor = Column(Float)
    rcarga_id = Column(Integer, ForeignKey("rcarga.id"))
    sistema = Column(String(30))

    rcarga = relationship("Rcarga", back_populates="rcarga_item")
    rcarga_liqui = relationship("Rcarga_Liqui", back_populates="rcarga_item")


class Rcarga_Liqui(Base):
    __tablename__ = "rcarga_liqui"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    documentos = Column(String(100))
    reten = Column(String(50))
    docpago = Column(String)
    pago = Column(Float)
    fechare = Column(DATETIME)
    rcarga_item_id = Column(Integer, ForeignKey("rcarga_item.id"))

    rcarga_item = relationship("Rcarga_Item", back_populates="rcarga_liqui")


class RcargaView(Base):
    __tablename__ = "rcarga_view"

    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    fecha = Column(DATETIME)
    total = Column(Float)
    division = Column(String(50))
    ruta = Column(String(50))
    estatus = Column(String(50))
    chofer = Column(String(50))
    ayudante = Column(String(50))
    placa = Column(String(50))


class Grupos_View(Base):
    __tablename__ = "grupos_view"

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    nombre = Column(String(50))
    cargo = Column(String(50))
    grupo = Column(String(50))


class RcargaLiquiView(Base):
    __tablename__ = "rcarga_liqui_view"

    docnum = Column(Integer, primary_key=True)
    id = Column(Integer, primary_key=True)
    itemsid = Column(Integer)
    totalvalor = Column(Float)
    fecha = Column(DATETIME)
    division = Column(String(50))
    ruta = Column(String(50))
    estatus = Column(String(50))
    cardname = Column(String)
    fechare = Column(DATETIME)
    docpago = Column(String)
    documentos = Column(String)
    reten = Column(String)
    pago = Column(Float)
