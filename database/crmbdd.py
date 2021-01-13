from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends


import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SQLALCHEMY_DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URL")
EUROLICORES_DATABASE_URL = os.environ.get("DATABASE_URL_EUROLICORES")
EURODISTRIBUTION_DATABASE_URL = os.environ.get("DATABASE_URL_EURODISTRIBUTION")
EUROMOBIL_DATABASE_URL = os.environ.get("DATABASE_URL_EUROMOBIL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
eurolicores = create_engine(EUROLICORES_DATABASE_URL)
eurodistribution = create_engine(EURODISTRIBUTION_DATABASE_URL)
euromobil = create_engine(EUROMOBIL_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLicores = sessionmaker(
    autocommit=False, autoflush=False, bind=eurolicores)
SessionDistribution = sessionmaker(
    autocommit=False, autoflush=False, bind=eurodistribution)

SessionMobil = sessionmaker(
    autocommit=False, autoflush=False, bind=euromobil)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_db2():
    db = SessionLicores()
    try:
        yield db
    finally:
        db.close()


def get_db3():
    db = SessionDistribution()
    try:
        yield db
    finally:
        db.close()


def get_db4():
    db = SessionMobil()
    try:
        yield db
    finally:
        db.close()


class DbParams:
    def __init__(self,  crm: Session = Depends(get_db), lico: Session = Depends(get_db2),
                 distri: Session = Depends(get_db3), mobil: Session = Depends(get_db4)):
        self.crm = crm
        self.lico = lico
        self.distri = distri
        self.mobil = mobil
