from pydantic import BaseModel


""" Shemas for CRM Objects """


class Crm(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CrmCreate(BaseModel):
    name: str


class Flota(BaseModel):
    id: int
    placa: str

    class Config:
        orm_mode = True
