from fastapi import APIRouter, Depends, HTTPException, Body, Request
from sqlalchemy.orm import Session
from database.crmbdd import get_db, DbParams

from typing import List

from . import schemas
from . import models
from . import crud
from login.schemas import User

router = APIRouter()


""" @router.get("/api/rcarga")
async def get_rcarga(current_user: schlogin.User = Depends(login.get_current_user)):
    return {"message": "API RCARGA"} """


@router.get("/api/rcarga/info")
async def get_rcarga():
    return {"message": "API RCARGA"}

""" Rcarga Estatus """


@router.get("/api/rcarga_estatus", response_model=List[schemas.Rcarga_Estatus])
def read_rcarga_estatus(db: DbParams = Depends(DbParams)):
    rcarga_estatus = crud.get_rcarga_estatus(db)
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
def read_rcarga_ruta(db: DbParams = Depends(DbParams)):
    rcarga_ruta = crud.get_rcarga_ruta(db)
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
def read_rcarga(db: DbParams = Depends(DbParams)):
    rcarga = crud.get_rcarga(db)
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
    return crud.update_rcarga(db=db, rcarga=rcarga, rcarga_id=rcarga_id)


@router.put("/api/rcarga_update/{rcarga_id}/{estatus}", response_model=schemas.Rcarga)
def update_rcarga(rcarga_id: int, estatus: int, db: DbParams = Depends(DbParams)):
    db_rcarga = crud.get_rcarga_by_id(
        db, rcarga_id=rcarga_id)
    if db_rcarga is None:
        raise HTTPException(
            status_code=404, detail="Relacion de Carga no Existe")
    return crud.update_estatus_rcarga(db=db, rcarga_id=rcarga_id, estatus=estatus,)


@router.delete("/api/rcarga/{rcarga_id}")
def delete_a_rcarga(rcarga_id: int, db: DbParams = Depends(DbParams)):
    db_rcarga = crud.get_rcarga_by_id(
        db, rcarga_id=rcarga_id)
    if db_rcarga is None:
        raise HTTPException(
            status_code=404, detail="Estatus de Relacion de Carga no Existe")
    crud.delete_rcarga(db, rcarga_id)
    return {"detail": "Relación de Carga Eliminado"}


@router.get("/api/rcarga_detalle", response_model=List[schemas.Rcarga])
def read_rcarga(db: DbParams = Depends(DbParams)):
    rcarga = crud.get_rcarga_detalle(db)
    return rcarga


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


""" Rcarga_Despacho """


@router.get("/api/rcarga_despacho/", response_model=List[schemas.Rcarga_View])
def read_rcarga_despacho(db: DbParams = Depends(DbParams)):
    rcarga_despacho = crud.get_rcarga_despacho(db)
    return rcarga_despacho


@router.get("/api/rcarga_despacho/{rcarga_id}", response_model=schemas.Rcarga_Despacho)
def read_rcarga_despacho(rcarga_id: int, db: DbParams = Depends(DbParams)):
    rcarga_despacho = crud.get_rcarga_despacho_by_id(db, rcarga_id=rcarga_id)
    return rcarga_despacho


@router.get("/api/chofer", response_model=List[schemas.Grupos_View])
def read_chofer(db: DbParams = Depends(DbParams), grupo: str = 'CHOFER'):
    users_grupo = crud.get_users_grupo(db, grupo=grupo)
    return users_grupo


@router.get("/api/ayudante", response_model=List[schemas.Grupos_View])
def read_ayudante(db: DbParams = Depends(DbParams),  grupo: str = 'AYUDATES'):
    rcarga_despacho = crud.get_users_grupo(db, grupo=grupo)
    return rcarga_despacho


@router.post("/api/despacho/{rcarga_id}", response_model=List[schemas.Rcarga_View])
async def create_rcarga_depacho(rcarga_id: int, rcarga_despacho: schemas.Rcarga_Despacho_Create, db: DbParams = Depends(DbParams)):
    rcarga = crud.get_rcarga_despacho_by_id(db, rcarga_id)

    if rcarga is None:
        return crud.create_rcarga_despacho(db=db, rcarga_despacho=rcarga_despacho, rcarga_id=rcarga_id)
    else:
        return crud.update_rcarga_despacho(db=db, rcarga_despacho=rcarga_despacho, rcarga_id=rcarga_id, id=rcarga.id)


""" Rcarga_Liquidacion """


@router.get("/api/rcarga_liqui/{rcarga_id}", response_model=List[schemas.Rcarga_Liqui_View])
def read_rcarga_liqui(rcarga_id: int, db: DbParams = Depends(DbParams)):
    rcarga_liqui = crud.get_rcarga_liqui(db,  rcarga_id=rcarga_id)
    return rcarga_liqui


@router.post("/api/rcarga_liqui/", response_model=List[schemas.Rcarga_Liqui_View])
def create_rcarga_liqui(liqui: schemas.Rcarga_Liqui_Create, db: DbParams = Depends(DbParams)):
    rcarga = crud.get_rcarga_liqui_by_id(db, liqui.rcarga_item_id)
    if rcarga is None:
        return crud.create_rcarga_liqui(db=db, liqui=liqui)
    else:
        return crud.update_rcarga_liqui(db=db, liqui=liqui)


""" Rcarga Detalle """


@router.post("/api/rcarga_detalle/{divi}", response_model=List[schemas.ItemsDetalle2])
def read_rcarga(DocNum: schemas.DocNum, divi: int, db: DbParams = Depends(DbParams)):
    rcarga = crud.get_items_detalle(db, DocNum=DocNum, divi=divi)
    return rcarga
