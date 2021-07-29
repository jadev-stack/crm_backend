from pydantic import BaseModel
from datetime import date, datetime
from typing import List, Optional
from crm.schemas import Crm


class Oslp(BaseModel):
    SlpCode: int
    SlpName: str
    U_Estatus: str

    class Config:
        orm_mode = True


class Maestra(BaseModel):
    CardCode: str
    Address: str
    CardName: str
    SlpCode: int
    U_NTX_Comercial: Optional[str]
    RIF: str
    Estado: Optional[str]
    Ciudad: Optional[str]
    Municipio: Optional[str]
    E_mail: Optional[str]
    Fiscal: Optional[str]
    Envio: Optional[str]
    Latitud: Optional[str]
    Longitud: Optional[str]
    Frecuencia: Optional[str]
    EDV: Optional[str]
    CondPagos: Optional[str]
    Secuencia: Optional[int]
    Despacho: Optional[str]
    Dia: Optional[str]
    Correo: Optional[str]
    Tlf: Optional[str]
    LimiteC: Optional[str]
    OCS: Optional[str]
    Capital: Optional[str]
    Canal: Optional[str]
    Formato: Optional[str]
    Relevancia: Optional[str]

    class Config:
        orm_mode = True
