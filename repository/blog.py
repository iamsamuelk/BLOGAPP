from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from blog import schemas, models
from datetime import datetime



def get_all(db : Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.BlogCreate, db : Session):
    current_time = datetime.now()
    new_blog = models.Blog(title=request.title, body=request.body, user_id=request.user_id, created_at=current_time, updated_at= current_time)
    user = db.query(models.User).filter(models.User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with the id {request.user_id} is not available")
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def show(id:int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog with the id {id} is not available")
    return blog


def update(id:int, request: schemas.BlogBase, db: Session):
    current_time = datetime.now()
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.update({'title': request.title, 'body': request.body, 'updated_at': current_time})
    db.commit()
    return 'updated'


def destroy(id:int, db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'