from pydantic import BaseModel
from datetime import date, datetime
from typing import List
from crm.schemas import Crm


""" Rcarga Estatus """


class Rcarga_Estatus(BaseModel):
    id: int
    estatus: str

    class Config:
        orm_mode = True


class Rcarga_EstatusCreate(Rcarga_Estatus):
    pass


""" Rcarga Ruta """


class Rcarga_Ruta(BaseModel):
    id: int
    ruta: str
    objetivo: int
    division_id: int

    class Config:
        orm_mode = True


class Rcarga_RutaCreate(BaseModel):
    ruta: str
    objetivo: int
    division_id: int


""" Rcarga """


class Rcarga(BaseModel):
    id: int
    fecha: date
    total: float
    vol: float
    numero: int
    ruta_id: int
    estatus_id: int
    user_id: int
    division_id: int
    sede_id: int
    rcarga_ruta: Rcarga_Ruta
    rcarga_estatus: Rcarga_Estatus
    rcarga_division: Crm

    class Config:
        orm_mode = True


class RcargaCreate(BaseModel):
    total: float
    vol: float
    ruta_id: int
    estatus_id: int
    user_id: int
    division_id: int
    sede_id: int


""" Rcarga_Item """


class Rcarga_Item(BaseModel):
    id: int
    docnum: int
    cardname: str
    cajas: int
    unidad: int
    totalvalor: float
    rcarga_id: int
    sistema: str
    rcarga: Rcarga

    class Config:
        orm_mode = True


class Rcarga_ItemCreate(BaseModel):
    docnum: int
    cardname: str
    cajas: int
    unidad: int
    totalvalor: float
    rcarga_id: int
    sistema: str

    class Config:
        orm_mode = True


class Invoice(BaseModel):
    DocNum: int
    CardCode: str
    CardName: str
    Cajas: int
    Unidad: int
    TotalValor: float
