from pydantic import BaseModel


class Crm(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CrmCreate(BaseModel):
    name: str
