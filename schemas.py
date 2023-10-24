from pydantic import BaseModel
from typing import List


class BlogBase(BaseModel):
    title: str
    body: str
    
class Blog(BlogBase):
    class Config():
        from_attributes = True


class User(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str

class CreateUser(BaseModel):
    firstName: str
    lastName: str
    email: str
    class Config():
        from_attributes = True
    
class ShowUser(BaseModel):
    firstName: str
    lastName: str
    email: str
    blogs: List[Blog] =[]
    class Config():
        from_attributes = True
        
        
    
class ShowBlog(BaseModel):
    title: str
    body: str
    author: CreateUser
    class Config():
        from_attributes = True
        
        

class Login(BaseModel):
    username: str
    password: str
    
    
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None    