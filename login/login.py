from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import List
from sqlalchemy.orm import Session
from database.crmbdd import SessionLocal, engine, get_db
from jwt import PyJWTError

from . import schemas
from . import models
from . import crud

router = APIRouter()


ACCESS_TOKEN_EXPIRE_MINUTES = 10
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth")


@router.get("/api/info")
async def get_info():
    return {"message": "API EUROGROUP"}


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="No se pudo Validar Credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        from .utils import decode_access_token
        payload = decode_access_token(data=token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except PyJWTError:
        raise credentials_exception
    user = crud.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


@router.get("/api/users/", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.post("/api/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Usuario ya está Registrado")
    return crud.create_user(db=db, user=user)


@router.get("/api/user/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no Existe")
    return db_user


@router.post("/api/auth", response_model=schemas.Token)
async def authenticate_user(user: schemas.UserAuthenticate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Usuario no Existe")
    else:
        is_password_correct = crud.check_username_password(db, user)
        if is_password_correct is False:
            raise HTTPException(
                status_code=400, detail="Contraseña Invalida")
        else:
            from datetime import timedelta
            access_token_expires = timedelta(
                minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            from .utils import create_access_token
            access_token = create_access_token(
                data={"sub": user.username}, expires_delta=access_token_expires)
            return {"access_token": access_token, "token_type": "Bearer"}
