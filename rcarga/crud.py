from sqlalchemy.orm import Session

from . import schemas
from . import models


""" Rcarga_Estatus """


def get_rcarga_estatus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Rcarga_Estatus).offset(skip).limit(limit).all()


def get_rcarga_estatus_by_id(db: Session, rcarga_estatus_id: int):
    return db.query(models.Rcarga_Estatus).filter(models.Rcarga_Estatus.id == rcarga_estatus_id).first()


def create_rcarga_estatus(db: Session, rcarga_estatus: schemas.Rcarga_Estatus):
    db_rcarga_estatus = models.Rcarga_Estatus(estatus=rcarga_estatus.estatus)
    db.add(db_rcarga_estatus)
    db.commit()
    db.refresh(db_rcarga_estatus)
    return db_rcarga_estatus


def update_rcarga_estatus(db: Session, rcarga_estatus: schemas.Rcarga_Estatus, rcarga_estatus_id: int):
    db_rcarga_estatus = db.query(models.Rcarga_Estatus).filter(
        models.Rcarga_Estatus.id == rcarga_estatus_id).first()
    db_rcarga_estatus.estatus = rcarga_estatus.estatus
    db.commit()
    db.refresh(db_rcarga_estatus)
    return {**rcarga_estatus.dict(), "id": rcarga_estatus_id}


def delete_rcarga_estatus(db: Session, rcarga_estatus_id: int):
    rcarga_estatus = db.query(models.Rcarga_Estatus).filter(
        models.Rcarga_Estatus.id == rcarga_estatus_id).first()
    db.delete(rcarga_estatus)
    db.commit()


""" Rcarga_Ruta """


def get_rcarga_ruta(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Rcarga_Ruta).offset(skip).limit(limit).all()


def get_rcarga_ruta_by_id(db: Session, rcarga_ruta_id: int):
    return db.query(models.Rcarga_Ruta).filter(models.Rcarga_Ruta.id == rcarga_ruta_id).first()


def create_rcarga_ruta(db: Session, rcarga_ruta: schemas.Rcarga_Ruta):
    db_rcarga_ruta = models.Rcarga_Ruta(ruta=rcarga_ruta.ruta,
                                        objetivo=rcarga_ruta.objetivo,
                                        division_id=rcarga_ruta.division_id)
    db.add(db_rcarga_ruta)
    db.commit()
    db.refresh(db_rcarga_ruta)
    return db_rcarga_ruta


def update_rcarga_ruta(db: Session, rcarga_ruta: schemas.Rcarga_Ruta, rcarga_ruta_id: int):
    db_rcarga_ruta = db.query(models.Rcarga_Ruta).filter(
        models.Rcarga_Ruta.id == rcarga_ruta_id).first()
    db_rcarga_ruta.ruta = rcarga_ruta.ruta
    db_rcarga_ruta.objectivo = rcarga_ruta.objetivo
    db_rcarga_ruta.division_id = rcarga_ruta.division_id
    db.commit()
    db.refresh(db_rcarga_ruta)
    return {**rcarga_ruta.dict(), "id": rcarga_ruta_id}


def delete_rcarga_ruta(db: Session, rcarga_ruta_id: int):
    rcarga_ruta = db.query(models.Rcarga_Ruta).filter(
        models.Rcarga_Ruta.id == rcarga_ruta_id).first()
    db.delete(rcarga_ruta)
    db.commit()


"""Rcarga"""


def get_rcarga(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Rcarga).offset(skip).limit(limit).all()


def get_rcarga_by_id(db: Session, rcarga_ruta_id: int):
    return db.query(models.Rcarga).filter(models.Rcarga.id == rcarga_id).first()


def create_rcarga(db: Session, rcarga: schemas.Rcarga):
    data = db.query(models.Rcarga).filter(models.Rcarga.division_id == rcarga.division_id).filter(
        models.Rcarga.sede_id == rcarga.sede_id).order_by(models.Rcarga.id.desc()).first()
    if data is None:
        docnum = 1
    else:
        docnum = data.numero + 1

    db_rcarga = models.Rcarga(total=rcarga.total,
                              vol=rcarga.vol,
                              numero=docnum,
                              ruta_id=rcarga.ruta_id,
                              estatus_id=rcarga.estatus_id,
                              user_id=rcarga.user_id,
                              division_id=rcarga.division_id,
                              sede_id=rcarga.sede_id)
    db.add(db_rcarga)
    db.commit()
    db.refresh(db_rcarga)
    return db_rcarga


def update_rcarga(db: Session, rcarga: schemas.Rcarga, rcarga_id: int):
    db_rcarga = db.query(models.Rcarga).filter(
        models.Rcarga.id == rcarga_id).first()
    db_rcarga.fecha = rcarga.fecha
    db_rcarga.total = rcarga.total
    db_rcarga.vol = rcarga.vol
    db_rcarga.numero = rcarga.numero
    db_rcarga.ruta_id = rcarga.ruta_id
    db_rcarga.estatus_id = rcarga.estatus_id
    db_rcarga.user_id = rcarga.user_id
    db_rcarga.division_id = rcarga.division_id
    db_rcarga.sede_id = rcarga.sede_id
    db.commit()
    db.refresh(db_rcarga)
    return {**rcarga.dict(), "id": rcarga_id}


def delete_rcarga(db: Session, rcarga_id: int):
    rcarga = db.query(models.Rcarga).filter(
        models.Rcarga.id == rcarga_id).first()
    db.delete(rcarga)
    db.commit()


"""Rcarga_Items"""


def get_rcarga_items_by_id(db: Session, rcarga_id: int):
    return db.query(models.Rcarga_Item).filter(models.Rcarga_Item.rcarga_id == rcarga_id).all()
