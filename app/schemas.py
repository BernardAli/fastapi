from datetime import datetime

from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True  # Default
    # rating: Optional[int] = None    # Optional


class PostCreate(PostBase):
    pass


# class CreatePost(BaseModel):
#     title: str
#     content: str
#     published: bool = True  # Default
#     # rating: Optional[int] = None    # Optional
#
#
# class UpdatePost(BaseModel):
#     title: str
#     content: str
#     published: bool


# Response schemas
class Post(PostBase):
    id: int
    created: datetime

    class Config:
       orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


# Response schemas
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created: datetime

    class Config:
       orm_mode = True