from fastapi import APIRouter, Depends, HTTPException
from login import login, schemas as schlogin
from sqlalchemy.orm import Session
from database.crmbdd import SessionLocal, engine, get_db

from typing import List

from . import schemas
from . import models
from . import crud

router = APIRouter()


""" @router.get("/api/rcarga")
async def get_rcarga(current_user: schlogin.User = Depends(login.get_current_user)):
    return {"message": "API RCARGA"} """


@router.get("/api/crm")
async def get_rcarga():
    return {"message": "API CRM"}

""" Cargos """


@router.get("/api/cargos", response_model=List[schemas.Crm])
def read_cargos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cargos = crud.get_cargos(db, skip=skip, limit=limit)
    return cargos


@router.get("/api/cargos/{cargo_id}", response_model=schemas.Crm)
def read_cargos_by_id(cargo_id: int, db: Session = Depends(get_db)):
    db_cargo = crud.get_cargo_by_id(db, cargo_id=cargo_id)
    if db_cargo is None:
        raise HTTPException(status_code=404, detail="Cargo no Existe")
    return db_cargo


@router.post("/api/cargos", response_model=schemas.Crm)
def create_cargo(cargo: schemas.CrmCreate, db: Session = Depends(get_db)):
    return crud.create_cargo(db=db, cargo=cargo)


@router.put("/api/cargos/{cargo_id}", response_model=schemas.CrmCreate)
def update_cargo(cargo_id: int, cargo: schemas.CrmCreate, db: Session = Depends(get_db)):
    db_cargo = crud.get_cargo_by_id(db, cargo_id=cargo_id)
    if db_cargo is None:
        raise HTTPException(status_code=404, detail="Cargo no Existe")
    return crud.update_cargo(db=db, cargo=cargo, cargo_id=cargo_id)


@router.delete("/api/cargos/{cargo_id}")
def delete_a_cargo(cargo_id: int, db: Session = Depends(get_db)):
    db_cargo = crud.get_cargo_by_id(db, cargo_id=cargo_id)
    if db_cargo is None:
        raise HTTPException(status_code=404, detail="Cargo no Existe")
    crud.delete_cargo(db, cargo_id)
    return {"detail": "Cargo Eliminado"}


""" Sedes """


@router.get("/api/sedes", response_model=List[schemas.Crm])
def read_sedes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sedes = crud.get_sedes(db, skip=skip, limit=limit)
    return sedes


@router.get("/api/sedes/{sede_id}", response_model=schemas.Crm)
def read_sedes_by_id(sede_id: int, db: Session = Depends(get_db)):
    db_sede = crud.get_sede_by_id(db, sede_id=sede_id)
    if db_sede is None:
        raise HTTPException(status_code=404, detail="Sede no Existe")
    return db_sede


@router.post("/api/sedes", response_model=schemas.Crm)
def create_sede(sede: schemas.CrmCreate, db: Session = Depends(get_db)):
    return crud.create_sede(db=db, sede=sede)


@router.put("/api/sedes/{sede_id}", response_model=schemas.CrmCreate)
def update_sede(sede_id: int, sede: schemas.CrmCreate, db: Session = Depends(get_db)):
    db_sede = crud.get_sede_by_id(db, sede_id=sede_id)
    if db_sede is None:
        raise HTTPException(status_code=404, detail="Sede no Existe")
    return crud.update_sede(db=db, sede=sede, sede_id=sede_id)


@router.delete("/api/sedes/{sede_id}")
def delete_a_sede(sede_id: int, db: Session = Depends(get_db)):
    db_sede = crud.get_sede_by_id(db, sede_id=sede_id)
    if db_sede is None:
        raise HTTPException(status_code=404, detail="Sede no Existe")
    crud.delete_sede(db, sede_id)
    return {"detail": "Sede Eliminado"}


""" Division """


@router.get("/api/division", response_model=List[schemas.Crm])
def read_division(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    division = crud.get_division(db, skip=skip, limit=limit)
    return division


@router.get("/api/division/{division_id}", response_model=schemas.Crm)
def read_division_by_id(division_id: int, db: Session = Depends(get_db)):
    db_division = crud.get_division_by_id(db, division_id=division_id)
    if db_division is None:
        raise HTTPException(status_code=404, detail="Division no Existe")
    return db_division


@router.post("/api/division", response_model=schemas.Crm)
def create_user(division: schemas.CrmCreate, db: Session = Depends(get_db)):
    return crud.create_division(db=db, division=division)


@router.put("/api/division/{division_id}", response_model=schemas.CrmCreate)
def update_division(division_id: int, division: schemas.CrmCreate, db: Session = Depends(get_db)):
    db_division = crud.get_division_by_id(db, division_id=division_id)
    if db_division is None:
        raise HTTPException(status_code=404, detail="Division no Existe")
    return crud.update_division(db=db, division=division, division_id=division_id)


@router.delete("/api/division/{division_id}")
def delete_a_sede(division_id: int, db: Session = Depends(get_db)):
    db_division = crud.get_division_by_id(db, division_id=division_id)
    if db_division is None:
        raise HTTPException(status_code=404, detail="Division no Existe")
    crud.delete_division(db, division_id)
    return {"detail": "Division Eliminado"}
