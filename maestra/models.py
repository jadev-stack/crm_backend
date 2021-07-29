from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DATETIME, Float
from database.crmbdd import Base
from sqlalchemy.orm import relationship
from login.models import User
from datetime import datetime


class OSLP(Base):
    __tablename__ = "OSLP"
    SlpCode = Column(Integer, primary_key=True, index=True)
    SlpName = Column(String(160))
    U_Estatus = Column(String(10))


class Maestra(Base):
    __tablename__ = "Maestra"
    CardCode = Column(Integer,  primary_key=True)
    Address = Column(String(40),  primary_key=True)
    CardName = Column(String(160))
    SlpCode = Column(Integer)
    U_NTX_Comercial = Column(String(60))
    RIF = Column(String(60))
    Estado = Column(String(60))
    Ciudad = Column(String(60))
    Municipio = Column(String(60))
    E_mail = Column(String(60))
    Fiscal = Column(String(60))
    Envio = Column(String(60))
    Latitud = Column(String(60))
    Longitud = Column(String(60))
    Frecuencia = Column(String(60))
    EDV = Column(String(60))
    CondPagos = Column(String(60))
    Secuencia = Column(Integer)
    Despacho = Column(String(60))
    Dia = Column(String(60))
    RIF = Column(String(60))
    Correo = Column(String(60))
    Tlf = Column(String(60))
    LimiteC = Column(String(60))
    OCS = Column(String(60))
    Capital = Column(String(60))
    Canal = Column(String(60))
    Formato = Column(String(60))
    Relevancia = Column(String(60))
