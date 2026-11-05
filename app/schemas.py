from pydantic import BaseModel
from typing import Optional


class TodCreate(BaseModel):
    title:str
    description:Optional[str]= None
    completed:bool = False

class TodoUpdate(BaseModel):
    title:str
    description:Optional[str]= None
    completed:Optional[bool] = False

class TodoResponse(BaseModel):
    id:int
    title:str
    description:Optional[str] = None
    completed:bool

    class config:
        from_attributes = True

        