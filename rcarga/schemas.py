from pydantic import BaseModel
from datetime import date, datetime
from typing import List, Optional
from crm.schemas import Crm


""" Rcarga Estatus """


class Rcarga_Estatus(BaseModel):
    id: int
    estatus: str

    class Config:
        orm_mode = True


""" Rcarga_Despacho """


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


class Rcarga_Despacho(BaseModel):
    id: int
    chofer: str
    ayudante: str
    vehiculo: int
    rcarga_id: int

    class Config:
        orm_mode = True


class Rcarga_Despacho_Create(BaseModel):
    chofer: str
    ayudante: str
    vehiculo: int


""" Rcarga """


class Rcarga(BaseModel):
    id: int
    fecha: datetime
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


class Rcarga_View(BaseModel):
    id: int
    fecha: date
    total: float
    numero: int
    ruta: str
    estatus: str
    division: str
    estatus: str
    chofer: Optional[str]
    ayudante: Optional[str]
    placa: Optional[str]

    class Config:
        orm_mode = True


class Invoice(BaseModel):
    DocNum: int
    CardCode: str
    CardName: str
    Cajas: int
    Unidad: int
    TotalValor: float


class Grupos_View(BaseModel):
    id: int
    username: str
    nombre: Optional[str]
    cargo: Optional[str]
    grupo: Optional[str]

    class Config:
        orm_mode = True


class Rcarga_Liqui_View(BaseModel):
    docnum: int
    id: int
    itemsid: int
    totalvalor: float
    fecha: date
    division: str
    ruta: str
    estatus: str
    cardname: str
    fechare: Optional[date]
    docpago: Optional[str]
    documentos: Optional[str]
    reten: Optional[str]
    pago: Optional[float]

    class Config:
        orm_mode = True


class Rcarga_Liqui(BaseModel):
    id: int
    fechare: date
    docpago: str
    documentos: str
    reten: str
    pago: float
    rcarga_item_id: int
    rcarga_id: int

    class Config:
        orm_mode = True


class Rcarga_Liqui_Create(BaseModel):
    docpago: str
    documentos: str
    reten: str
    pago: float
    rcarga_item_id: int
    rcarga_id: int
    fechare: date


class DocNum(BaseModel):
    docnum: List[int]


class ItemsDetalle(BaseModel):
    DocNum: int
    ItemCode: str
    ItemName: str
    Cajas: int
    Und: int

    class Config:
        orm_mode = True


class ItemsDetalle2(BaseModel):

    ItemCode: str
    ItemName: str
    Cajas: int
    Und: int
    UxC: int

    class Config:
        orm_mode = True
