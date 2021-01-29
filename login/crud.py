from sqlalchemy.orm import Session
import bcrypt

from . import schemas
from . import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 500):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = bcrypt.hashpw(
        user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.User(
        email=user.email, username=user.username, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_username_password(db: Session, user: schemas.UserAuthenticate):
    db_user_info: models.User = get_user_by_username(
        db, username=user.username)
    return bcrypt.checkpw(user.hashed_password.encode('utf-8'), db_user_info.hashed_password.encode('utf-8'))


def get_user_data(db: Session, user_id: int):
    return db.query(models.User_Data).filter(models.User_Data.user_id == user_id).first()


def get_user_cargo(db: Session, user_id: int):
    return db.query(models.User_Cargo).filter(models.User_Cargo.user_id == user_id).first()


def get_user_group(db: Session, user_id: int):
    return db.query(models.User_Group).filter(models.User_Group.user_id == user_id).first()
