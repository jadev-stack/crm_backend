from fastapi import APIRouter, Depends, HTTPException
from login import login, schemas as schlogin
router = APIRouter()


""" @router.get("/api/rcarga")
async def get_rcarga(current_user: schlogin.User = Depends(login.get_current_user)):
    return {"message": "API RCARGA"} """


@router.get("/api/rcarga")
async def get_rcarga():
    return {"message": "API RCARGA"}
