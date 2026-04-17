from ninja import Schema
from typing import Optional

class UserInfoSchema(Schema):
    id: int
    username: str

class PostSchema(Schema):
    id: str
    name: str
    author: UserInfoSchema
    description: Optional[str] = None

class PostCreateSchema(Schema):
    name: str
    description: Optional[str] = None