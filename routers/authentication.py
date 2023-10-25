from fastapi import APIRouter, Depends,status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from blog import models, JWTtoken
from blog.database import get_db
from sqlalchemy.orm import Session
from blog.hashing import Hash




router = APIRouter(
    prefix='/login',
    tags=['Authentication'],
)

@router.post('/')
def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Username not available")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Incorrect password")
    # generate a jwt token and return
    access_token = JWTtoken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}