from fastapi import FastAPI
from . import models
from .database import engine
from routers import authentication, user, blog


tags_metadata = [
    {
        "name": "Users",
        "description": "Operations with users.",
    },
    {
         "name": "Blogs",
        "description": "Operations with blogs.",
    },
    {
        "name": "Authentication",
        "description": "The **login** logic is here.",
    }
]


app = FastAPI(openapi_tags=tags_metadata)


models.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)
