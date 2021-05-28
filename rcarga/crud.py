from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException, Request
from . import schemas
from . import models
from . import mosap
from login.models import User
import json
from datetime import datetime
from typing import List

""" Rcarga_Estatus """


def get_rcarga_estatus(db: Session, skip: int = 0, limit: int = 100):
    return db.crm.query(models.Rcarga_Estatus).offset(skip).limit(limit).all()


def get_rcarga_estatus_by_id(db: Session, rcarga_estatus_id: int):
    return db.crm.query(models.Rcarga_Estatus).filter(models.Rcarga_Estatus.id == rcarga_estatus_id).first()


def create_rcarga_estatus(db: Session, rcarga_estatus: schemas.Rcarga_Estatus):
    db_rcarga_estatus = models.Rcarga_Estatus(estatus=rcarga_estatus.estatus)
    db.crm.add(db_rcarga_estatus)
    db.crm.commit()
    db.crm.refresh(db_rcarga_estatus)
    return db_rcarga_estatus


def update_rcarga_estatus(db: Session, rcarga_estatus: schemas.Rcarga_Estatus, rcarga_estatus_id: int):
    db_rcarga_estatus = db.crm.query(models.Rcarga_Estatus).filter(
        models.Rcarga_Estatus.id == rcarga_estatus_id).first()
    db_rcarga_estatus.estatus = rcarga_estatus.estatus
    db.crm.commit()
    db.crm.refresh(db_rcarga_estatus)
    return {**rcarga_estatus.dict(), "id": rcarga_estatus_id}


def delete_rcarga_estatus(db: Session, rcarga_estatus_id: int):
    rcarga_estatus = db.crm.query(models.Rcarga_Estatus).filter(
        models.Rcarga_Estatus.id == rcarga_estatus_id).first()
    db.crm.delete(rcarga_estatus)
    db.crm.commit()


""" Rcarga_Ruta """


def get_rcarga_ruta(db: Session, skip: int = 0, limit: int = 100):
    return db.crm.query(models.Rcarga_Ruta).offset(skip).limit(limit).all()


def get_rcarga_ruta_by_id(db: Session, rcarga_ruta_id: int):
    return db.crm.query(models.Rcarga_Ruta).filter(models.Rcarga_Ruta.id == rcarga_ruta_id).first()


def create_rcarga_ruta(db: Session, rcarga_ruta: schemas.Rcarga_Ruta):
    db_rcarga_ruta = models.Rcarga_Ruta(ruta=rcarga_ruta.ruta,
                                        objetivo=rcarga_ruta.objetivo,
                                        division_id=rcarga_ruta.division_id)
    db.crm.add(db_rcarga_ruta)
    db.crm.commit()
    db.crm.refresh(db_rcarga_ruta)
    return db_rcarga_ruta


def update_rcarga_ruta(db: Session, rcarga_ruta: schemas.Rcarga_Ruta, rcarga_ruta_id: int):
    db_rcarga_ruta = db.crm.query(models.Rcarga_Ruta).filter(
        models.Rcarga_Ruta.id == rcarga_ruta_id).first()
    db_rcarga_ruta.ruta = rcarga_ruta.ruta
    db_rcarga_ruta.objectivo = rcarga_ruta.objetivo
    db_rcarga_ruta.division_id = rcarga_ruta.division_id
    db.crm.commit()
    db.crm.refresh(db_rcarga_ruta)
    return {**rcarga_ruta.dict(), "id": rcarga_ruta_id}


def delete_rcarga_ruta(db: Session, rcarga_ruta_id: int):
    rcarga_ruta = db.crm.query(models.Rcarga_Ruta).filter(
        models.Rcarga_Ruta.id == rcarga_ruta_id).first()
    db.crm.delete(rcarga_ruta)
    db.crm.commit()


"""Rcarga"""


def get_rcarga(db: Session, ):
    return db.crm.query(models.Rcarga).filter(models.Rcarga.estatus_id != 5).all()


def get_rcarga_by_id(db: Session, rcarga_id: int):
    return db.crm.query(models.Rcarga).filter(models.Rcarga.id == rcarga_id).first()


def create_rcarga(db: Session, rcarga: schemas.Rcarga):
    data = db.crm.query(models.Rcarga).filter(models.Rcarga.division_id == rcarga.division_id).filter(
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
    db.crm.add(db_rcarga)
    db.crm.commit()
    db.crm.refresh(db_rcarga)
    return db_rcarga


def update_rcarga(db: Session, rcarga: schemas.Rcarga, rcarga_id: int):
    db_rcarga = db.crm.query(models.Rcarga).filter(
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
    db.crm.commit()
    db.crm.refresh(db_rcarga)
    return {**rcarga.dict(), "id": rcarga_id}


def update_estatus_rcarga(db: Session, rcarga_id: int, estatus: int):
    db.crm.query(models.Rcarga).filter(models.Rcarga.id == rcarga_id).update(
        dict(estatus_id=estatus))
    db.crm.commit()
    rcarga = db.crm.query(models.Rcarga).filter(
        models.Rcarga.id == rcarga_id).first()
    return rcarga


def delete_rcarga(db: Session, rcarga_id: int):
    rcarga = db.crm.query(models.Rcarga).filter(
        models.Rcarga.id == rcarga_id).first()
    db.crm.delete(rcarga)
    db.crm.commit()


"""Rcarga_Items"""


def get_rcarga_items_by_id(db: Session, rcarga_id: int):
    return db.crm.query(models.Rcarga_Item).filter(models.Rcarga_Item.rcarga_id == rcarga_id).all()


def get_rcarga_item_by_id(db: Session, rcarga_id: int):
    return db.crm.query(models.Rcarga_Item).filter(models.Rcarga_Item.id == rcarga_id).first()


def get_invoice_items(db: Session, DocNum: int, divi: int):
    if divi == 1:
        return db.lico.query(mosap.ItemsDoc).filter(mosap.ItemsDoc.DocNum == DocNum).first()
    elif divi == 2:
        return db.distri.query(mosap.ItemsDoc).filter(mosap.ItemsDoc.DocNum == DocNum).first()
    elif divi == 3:
        return db.mobil.query(mosap.ItemsDoc).filter(mosap.ItemsDoc.DocNum == DocNum).first()
    else:
        raise HTTPException(
            status_code=404, detail="Division No Encontrada")


def create_rcarga_item(db: Session, rcarga_id: int, sis: str, invoice: schemas.Invoice):
    db_rcarga = db.crm.query(models.Rcarga).filter(
        models.Rcarga.id == rcarga_id).first()

    db.crm.query(models.Rcarga).filter(models.Rcarga.id == rcarga_id).update(
        dict(total=round(db_rcarga.total+invoice.TotalValor, 2)))
    db_rcarga_item = models.Rcarga_Item(docnum=invoice.DocNum,
                                        cardname=invoice.CardName,
                                        cajas=invoice.Cajas,
                                        unidad=invoice.Unidad,
                                        totalvalor=invoice.TotalValor,
                                        rcarga_id=rcarga_id,
                                        sistema=sis)
    db.crm.add(db_rcarga_item)
    db.crm.commit()
    db.crm.refresh(db_rcarga_item)
    return db_rcarga_item


def delete_rcarga_item(db: Session, rcarga_id: int):
    rcargaitem = db.crm.query(models.Rcarga_Item).filter(
        models.Rcarga_Item.id == rcarga_id).first()
    rcarga = db.crm.query(models.Rcarga).filter(
        models.Rcarga.id == rcargaitem.rcarga_id).first()

    db.crm.query(models.Rcarga).filter(models.Rcarga.id == rcargaitem.rcarga_id).update(
        dict(total=round(rcarga.total-rcargaitem.totalvalor, 2)))

    db.crm.delete(rcargaitem)
    db.crm.commit()


"""Rcarga_Despacho"""


def get_rcarga_despacho(db: Session):
    return db.crm.query(models.RcargaView).filter(models.RcargaView.estatus != 'ABIERTA').all()


def get_rcarga_despacho_by_id(db: Session, rcarga_id: int):
    return db.crm.query(models.Rcarga_Despacho).filter(models.Rcarga_Despacho.rcarga_id == rcarga_id).first()


def get_users_grupo(db: Session, grupo: str):
    return db.crm.query(models.Grupos_View).filter(models.Grupos_View.grupo == grupo).all()


def create_rcarga_despacho(db: Session, rcarga_id: str, rcarga_despacho: schemas.Rcarga_Despacho_Create):
    db_rcarga_despacho = models.Rcarga_Despacho(chofer=rcarga_despacho.chofer,
                                                ayudante=rcarga_despacho.ayudante,
                                                vehiculo=rcarga_despacho.vehiculo,
                                                rcarga_id=rcarga_id)
    db.crm.add(db_rcarga_despacho)
    db.crm.commit()
    return get_rcarga_despacho(db)


def update_rcarga_despacho(db: Session, rcarga_despacho: schemas.Rcarga_Despacho, rcarga_id: int, id: int):
    db_rcarga_despacho = db.crm.query(models.Rcarga_Despacho).filter(
        models.Rcarga_Despacho.id == id).first()
    db_rcarga_despacho.chofer = rcarga_despacho.chofer
    db_rcarga_despacho.ayudante = rcarga_despacho.ayudante
    db_rcarga_despacho.vehiculo = rcarga_despacho.vehiculo
    db_rcarga_despacho.rcarga_id = rcarga_id
    db.crm.commit()
    db.crm.refresh(db_rcarga_despacho)
    return get_rcarga_despacho(db)


""" Rcarga_Liquidacion """


def get_rcarga_liqui(db: Session, rcarga_id: int):
    return db.crm.query(models.RcargaLiquiView).filter(models.RcargaLiquiView.id == rcarga_id).all()


def get_rcarga_liqui_by_id(db: Session, rcarga_id: int):
    return db.crm.query(models.Rcarga_Liqui).filter(models.Rcarga_Liqui.rcarga_item_id == rcarga_id).first()


def create_rcarga_liqui(db: Session,  liqui: schemas.Rcarga_Liqui_Create):
    db_rcarga_liqui = models.Rcarga_Liqui(documentos=liqui.documentos,
                                          reten=liqui.reten,
                                          docpago=liqui.docpago,
                                          fechare=liqui.fechare,
                                          pago=liqui.pago,
                                          rcarga_item_id=liqui.rcarga_item_id)
    db.crm.add(db_rcarga_liqui)
    db.crm.commit()
    rcarga = db.crm.query(models.RcargaLiquiView).filter(
        models.RcargaLiquiView.id == liqui.rcarga_id).all()
    return rcarga


def update_rcarga_liqui(db: Session, liqui: schemas.Rcarga_Liqui):
    db_rcarga_liqui = db.crm.query(models.Rcarga_Liqui).filter(
        models.Rcarga_Liqui.rcarga_item_id == liqui.rcarga_item_id).first()
    db_rcarga_liqui.fechare = liqui.fechare
    db_rcarga_liqui.docpago = liqui.docpago
    db_rcarga_liqui.documentos = liqui.documentos
    db_rcarga_liqui.reten = liqui.reten
    db_rcarga_liqui.pago = liqui.pago
    db_rcarga_liqui.rcarga_id = liqui.rcarga_id
    db_rcarga_liqui.rcarga_item_id = liqui.rcarga_item_id
    db.crm.commit()
    db.crm.refresh(db_rcarga_liqui)
    return get_rcarga_liqui(db, liqui.rcarga_id)


""" Rcarga Detalle """


def get_items_detalle(db: Session, DocNum: schemas.DocNum, divi: int):
    if divi == 1:
        return db.lico.query(func.sum(mosap.ItemsDetalle.Cajas).label("Cajas"),
                             func.sum(mosap.ItemsDetalle.Und).label(
                                 "Und"), mosap.ItemsDetalle.ItemCode, mosap.ItemsDetalle.UxC,
                             mosap.ItemsDetalle.ItemName).filter(mosap.ItemsDetalle.DocNum.in_(DocNum.docnum)).group_by(mosap.ItemsDetalle.ItemCode, mosap.ItemsDetalle.ItemName, mosap.ItemsDetalle.UxC).all()
    elif divi == 2:
        return db.distri.query(func.sum(mosap.ItemsDetalle.Cajas).label("Cajas"),
                               func.sum(mosap.ItemsDetalle.Und).label(
            "Und"), mosap.ItemsDetalle.ItemCode, mosap.ItemsDetalle.UxC,
            mosap.ItemsDetalle.ItemName).filter(mosap.ItemsDetalle.DocNum.in_(DocNum.docnum)).group_by(mosap.ItemsDetalle.ItemCode, mosap.ItemsDetalle.ItemName, mosap.ItemsDetalle.UxC).all()
    elif divi == 3:
        return db.mobil.query(func.sum(mosap.ItemsDetalle.Cajas).label("Cajas"),
                              func.sum(mosap.ItemsDetalle.Und).label(
            "Und"), mosap.ItemsDetalle.ItemCode, mosap.ItemsDetalle.UxC,
            mosap.ItemsDetalle.ItemName).filter(mosap.ItemsDetalle.DocNum.in_(DocNum.docnum)).group_by(mosap.ItemsDetalle.ItemCode, mosap.ItemsDetalle.ItemName, mosap.ItemsDetalle.UxC).all()
    else:
        raise HTTPException(
            status_code=404, detail="Division No Encontrada")
