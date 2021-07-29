from fastapi import APIRouter, Depends, HTTPException, Body, Request
from sqlalchemy.orm import Session
from database.crmbdd import get_db, DbParams

from typing import List

from . import schemas
from . import models
from . import crud
from login.schemas import User

router = APIRouter()


@router.get("/api/slp/{divi}", response_model=List[schemas.Oslp])
def read_oslp(divi: int, db: DbParams = Depends(DbParams)):
    oslp = crud.get_oslp(db, divi=divi)
    return oslp


@router.get("/api/sn/{divi}/{edv}", response_model=List[schemas.Maestra])
def read_sn(divi: int, edv: int, db: DbParams = Depends(DbParams)):
    sn = crud.get_maestra(db, divi=divi, edv=edv)
    return sn
