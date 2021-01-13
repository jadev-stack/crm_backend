from fastapi import APIRouter, Depends, HTTPException
from login import login, schemas as schlogin
from sqlalchemy.orm import Session
from database.crmbdd import get_db, DbParams

from typing import List

from . import schemas
from . import models
from . import crud

router = APIRouter()


""" @router.get("/api/rcarga")
async def get_rcarga(current_user: schlogin.User = Depends(login.get_current_user)):
    return {"message": "API RCARGA"} """


@router.get("/api/rcarga/info")
async def get_rcarga():
    return {"message": "API RCARGA"}

""" Rcarga Estatus """


@router.get("/api/rcarga_estatus", response_model=List[schemas.Rcarga_Estatus])
def read_rcarga_estatus(skip: int = 0, limit: int = 100, db: DbParams = Depends(DbParams)):
    rcarga_estatus = crud.get_rcarga_estatus(db, skip=skip, limit=limit)
    return rcarga_estatus


@router.get("/api/rcarga_estatus/{rcarga_estatus_id}", response_model=schemas.Rcarga_Estatus)
def read_rcarga_estatus_by_id(rcarga_estatus_id: int, db: DbParams = Depends(DbParams)):
    db_rcarga_estatus = crud.get_rcarga_estatus_by_id(
        db, rcarga_estatus_id=rcarga_estatus_id)
    if db_rcarga_estatus is None:
        raise HTTPException(
            status_code=404, detail="Estatus de Relacion de Carga no Existe")
    return db_rcarga_estatus


@router.post("/api/rcarga_estatus", response_model=schemas.Rcarga_Estatus)
def create_rcarga_estatus(rcarga_estatus: schemas.Rcarga_EstatusCreate, db: DbParams = Depends(DbParams)):
    return crud.create_rcarga_estatus(db=db, rcarga_estatus=rcarga_estatus)


@router.put("/api/rcarga_estatus/{rcarga_estatus_id}", response_model=schemas.Rcarga_Estatus)
def update_rcarga_estatus(rcarga_estatus_id: int, rcarga_estatus: schemas.Rcarga_EstatusCreate, db: DbParams = Depends(DbParams)):
    db_rcarga_estatus = crud.get_rcarga_estatus_by_id(
        db, rcarga_estatus_id=rcarga_estatus_id)
    if db_rcarga_estatus is None:
        raise HTTPException(
            status_code=404, detail="Estatus de Relacion de Carga no Existe")
    return crud.update_rcarga_estatus(db=db, rcarga_estatus=rcarga_estatus, rcarga_estatus_id=rcarga_estatus_id)


@router.delete("/api/rcarga_estatus/{rcarga_estatus_id}")
def delete_a_rcarga_estatus(rcarga_estatus_id: int, db: DbParams = Depends(DbParams)):
    db_rcarga_estatus = crud.get_rcarga_estatus_by_id(
        db, rcarga_estatus_id=rcarga_estatus_id)
    if db_rcarga_estatus is None:
        raise HTTPException(
            status_code=404, detail="Estatus de Relacion de Carga no Existe")
    crud.delete_rcarga_estatus(db, rcarga_estatus_id)
    return {"detail": "Estatus de Relación de Carga Eliminado"}


""" Rcarga Ruta """


@router.get("/api/rcarga_ruta", response_model=List[schemas.Rcarga_Ruta])
def read_rcarga_ruta(skip: int = 0, limit: int = 100, db: DbParams = Depends(DbParams)):
    rcarga_ruta = crud.get_rcarga_ruta(db, skip=skip, limit=limit)
    return rcarga_ruta


@router.get("/api/rcarga_ruta/{rcarga_ruta_id}", response_model=schemas.Rcarga_Ruta)
def read_rcarga_ruta_by_id(rcarga_ruta_id: int, db: DbParams = Depends(DbParams)):
    db_rcarga_ruta = crud.get_rcarga_ruta_by_id(
        db, rcarga_ruta_id=rcarga_ruta_id)
    if db_rcarga_ruta is None:
        raise HTTPException(
            status_code=404, detail="Ruta de Relacion de Carga no Existe")
    return db_rcarga_ruta


@router.post("/api/rcarga_ruta", response_model=schemas.Rcarga_Ruta)
def create_rcarga_ruta(rcarga_ruta: schemas.Rcarga_RutaCreate, db: DbParams = Depends(DbParams)):
    return crud.create_rcarga_ruta(db=db, rcarga_ruta=rcarga_ruta)


@router.put("/api/rcarga_ruta/{rcarga_ruta_id}", response_model=schemas.Rcarga_Ruta)
def update_rcarga_ruta(rcarga_ruta_id: int, rcarga_ruta: schemas.Rcarga_RutaCreate, db: DbParams = Depends(DbParams)):
    db_rcarga_ruta = crud.get_rcarga_ruta_by_id(
        db, rcarga_ruta_id=rcarga_ruta_id)
    if db_rcarga_ruta is None:
        raise HTTPException(
            status_code=404, detail="Ruta de Relacion de Carga no Existe")
    return crud.update_rcarga_ruta(db=db, rcarga_ruta=rcarga_ruta, rcarga_ruta_id=rcarga_ruta_id)


@router.delete("/api/rcarga_ruta/{rcarga_ruta_id}")
def delete_a_rcarga_ruta(rcarga_ruta_id: int, db: DbParams = Depends(DbParams)):
    db_rcarga_ruta = crud.get_rcarga_ruta_by_id(
        db, rcarga_ruta_id=rcarga_ruta_id)
    if db_rcarga_ruta is None:
        raise HTTPException(
            status_code=404, detail="Estatus de Relacion de Carga no Existe")
    crud.delete_rcarga_ruta(db, rcarga_ruta_id)
    return {"detail": "Ruta de Relación de Carga Eliminado"}


""" Rcarga """


@router.get("/api/rcarga", response_model=List[schemas.Rcarga])
def read_rcarga(skip: int = 0, limit: int = 100, db: DbParams = Depends(DbParams)):
    rcarga = crud.get_rcarga(db, skip=skip, limit=limit)
    return rcarga


@router.get("/api/rcarga/{rcarga_id}", response_model=schemas.Rcarga)
def read_rcarga_by_id(rcarga_id: int, db: DbParams = Depends(DbParams)):
    db_rcarga = crud.get_rcarga_by_id(
        db, rcarga_id=rcarga_id)
    if db_rcarga is None:
        raise HTTPException(
            status_code=404, detail="Relacion de Carga no Existe")
    return db_rcarga


@router.post("/api/rcarga", response_model=schemas.Rcarga)
def create_rcarga(rcarga: schemas.RcargaCreate, db: DbParams = Depends(DbParams)):
    return crud.create_rcarga(db=db, rcarga=rcarga)


@router.put("/api/rcarga/{rcarga_id}", response_model=schemas.Rcarga)
def update_rcarga(rcarga_id: int, rcarga: schemas.RcargaCreate, db: DbParams = Depends(DbParams)):
    db_rcarga = crud.get_rcarga_by_id(
        db, rcarga_id=rcarga_id)
    if db_rcarga is None:
        raise HTTPException(
            status_code=404, detail="Relacion de Carga no Existe")
    return crud.update_rcarga(db=db, rcarga=rcarga_ruta, rcarga_id=rcarga_id)


@router.delete("/api/rcarga/{rcarga_id}")
def delete_a_rcarga(rcarga_id: int, db: DbParams = Depends(DbParams)):
    db_rcarga = crud.get_rcarga_by_id(
        db, rcarga_id=rcarga_id)
    if db_rcarga is None:
        raise HTTPException(
            status_code=404, detail="Estatus de Relacion de Carga no Existe")
    crud.delete_rcarga(db, rcarga_id)
    return {"detail": "Relación de Carga Eliminado"}


""" Rcarga_Items """


@router.get("/api/rcarga_item/{rcarga_id}", response_model=List[schemas.Rcarga_Item])
def read_rcarga_items_by_id(rcarga_id: int, db: DbParams = Depends(DbParams)):
    db_rcarga = crud.get_rcarga_items_by_id(
        db, rcarga_id=rcarga_id)
    if db_rcarga is None:
        raise HTTPException(
            status_code=404, detail="Relacion de Carga No Posee Documentos")
    return db_rcarga


@router.post("/api/rcarga_item/{rcarga_id}/{DocNum}/{sis}", response_model=schemas.Rcarga_Item)
def create_rcarga_item(rcarga_id: int, DocNum: int, sis: str, db: DbParams = Depends(DbParams)):
    rcarga = crud.get_rcarga_by_id(db, rcarga_id)
    invoice = crud.get_invoice_items(db, DocNum, rcarga.division_id)
    if invoice is None:
        raise HTTPException(
            status_code=404, detail="Documentos No Encontrado")
    return crud.create_rcarga_item(db=db, rcarga_id=rcarga_id, sis=sis, invoice=invoice)


@router.delete("/api/rcarga_item/{rcarga_id}")
def delete_a_rcarga_item(rcarga_id: int, db: DbParams = Depends(DbParams)):
    db_rcargaitem = crud.get_rcarga_item_by_id(
        db, rcarga_id=rcarga_id)
    if db_rcargaitem is None:
        raise HTTPException(
            status_code=404, detail="Estatus de Relacion de Carga no Existe")
    crud.delete_rcarga_item(db, rcarga_id)
    return {"detail": "Documento de Relación de Carga Eliminado"}


@router.get("/api/rcarga/rcarga_item/{rcarga_id}", response_model=schemas.Rcarga_Item)
def read_rcarga_by_id(rcarga_id: int, db: DbParams = Depends(DbParams)):
    db_rcarga = crud.get_rcarga_item_by_id(
        db, rcarga_id=rcarga_id)
    if db_rcarga is None:
        raise HTTPException(
            status_code=404, detail="Item de Relacion de Carga no Existe")
    return db_rcarga
