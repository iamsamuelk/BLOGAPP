from fastapi import APIRouter, Depends, status
import schemas, oauth2
from database import get_db
from typing import List
from sqlalchemy.orm import Session
from repository import blog


router = APIRouter(
    prefix='/blog',
    tags=['Blogs'],
)



@router.get('/', response_model=List[schemas.ShowBlog])
def all(db : Session = Depends(get_db)):
    return blog.get_all(db)


@router.post('/', response_model=schemas.ShowBlog, status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.get('/{id}', response_model=schemas.ShowBlog, status_code=status.HTTP_200_OK)
def show(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)
  
    
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)