from sqlalchemy.orm import Session


from . import schemas
from . import models


""" Cargos """


def get_cargos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cargo).offset(skip).limit(limit).all()


def get_cargo_by_id(db: Session, cargo_id: int):
    return db.query(models.Cargo).filter(models.Cargo.id == cargo_id).first()


def create_cargo(db: Session, cargo: schemas.Crm):
    db_cargo = models.Cargo(name=cargo.name)
    db.add(db_cargo)
    db.commit()
    db.refresh(db_cargo)
    return db_cargo


def update_cargo(db: Session, cargo: schemas.Crm, cargo_id: int):
    db_cargo = db.query(models.Cargo).filter(
        models.Cargo.id == cargo_id).first()
    db_cargo.name = cargo.name
    db.commit()
    db.refresh(db_cargo)
    return {**cargo.dict(), "id": cargo_id}


def delete_cargo(db: Session, cargo_id: int):
    cargo = db.query(models.Cargo).filter(models.Cargo.id == cargo_id).first()
    db.delete(cargo)
    db.commit()


""" Sedes """


def get_sedes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Sede).offset(skip).limit(limit).all()


def get_sede_by_id(db: Session, sede_id: int):
    return db.query(models.Sede).filter(models.Sede.id == sede_id).first()


def create_sede(db: Session, sede: schemas.Crm):
    db_sede = models.Sede(name=sede.name)
    db.add(db_sede)
    db.commit()
    db.refresh(db_sede)
    return db_sede


def update_sede(db: Session, sede: schemas.Crm, sede_id: int):
    db_sede = db.query(models.Sede).filter(
        models.Sede.id == sede_id).first()
    db_sede.name = sede.name
    db.commit()
    db.refresh(db_sede)
    return {**sede.dict(), "id": sede_id}


def delete_sede(db: Session, sede_id: int):
    sede = db.query(models.Sede).filter(models.Sede.id == sede_id).first()
    db.delete(sede)
    db.commit()


""" Division """


def get_division(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Division).offset(skip).limit(limit).all()


def create_division(db: Session, division: schemas.Crm):
    db_division = models.Division(name=division.name)
    db.add(db_division)
    db.commit()
    db.refresh(db_division)
    return db_division


def get_division_by_id(db: Session, division_id: int):
    return db.query(models.Division).filter(models.Division.id == division_id).first()


def update_division(db: Session, division: schemas.Crm, division_id: int):
    db_division = db.query(models.Division).filter(
        models.Division.id == division_id).first()
    db_division.name = division.name
    db.commit()
    db.refresh(db_division)
    return {**division.dict(), "id": division_id}


def delete_division(db: Session, division_id: int):
    division = db.query(models.Division).filter(
        models.Division.id == division_id).first()
    db.delete(division)
    db.commit()


""" Flota """


def get_flota(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Flota).offset(skip).limit(limit).all()
