from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DATETIME, Float
from database.crmbdd import Base as Eurolicores
from sqlalchemy.orm import relationship
from datetime import datetime


class ItemsDoc(Eurolicores):
    __tablename__ = "ItemsFactura"

    DocNum = Column(Integer, primary_key=True)
    CardCode = Column(String(30))
    CardName = Column(String(50))
    TotalValor = Column(Float)
    Cajas = Column(Integer)
    Unidad = Column(Integer)


class ItemsDetalle(Eurolicores):
    __tablename__ = "items_detalle_view"

    DocNum = Column(Integer, primary_key=True)
    ItemCode = Column(String(30))
    ItemName = Column(String(50))
    Cajas = Column(Integer)
    Und = Column(Integer)
    UxC = Column(Integer)
