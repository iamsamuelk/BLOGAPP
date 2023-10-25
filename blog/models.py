from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from .database import Base
from sqlalchemy.orm import relationship




class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer,primary_key=True,index=True)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    password = Column(String)
    
    blogs = relationship("Blog", back_populates="author")



class Blog(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    body = Column(String)
    created_at= Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    user_id = Column(Integer, ForeignKey('users.id'))
    
    author = relationship("User", back_populates="blogs")