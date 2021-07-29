from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException, Request
from . import schemas
from . import models
from login.models import User
import json
from datetime import datetime
from typing import List


""" Oslp """


def get_oslp(db: Session, divi: int):
    if divi == 1:
        return db.lico.query(models.OSLP).filter(models.OSLP.U_Estatus == 'A').order_by(models.OSLP.SlpName).all()
    elif divi == 2:
        return db.distri.query(models.OSLP).filter(models.OSLP.U_Estatus == 'A').order_by(models.OSLP.SlpName).all()
    elif divi == 3:
        return db.mobil.query(models.OSLP).filter(models.OSLP.U_Estatus == 'A').order_by(models.OSLP.SlpName).all()


""" Maestra """


def get_maestra(db: Session, divi: int, edv: int):
    if divi == 1:
        return db.lico.query(models.Maestra).filter(models.Maestra.SlpCode == edv).all()
    elif divi == 2:
        return db.distri.query(models.Maestra).filter(models.Maestra.SlpCode == edv).all()
    elif divi == 3:
        return db.mobil.query(models.Maestra).filter(models.Maestra.SlpCode == edv).all()
