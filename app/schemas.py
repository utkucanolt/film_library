from pydantic import BaseModel
from typing import Optional

class MovieBase(BaseModel):
    title: str
    description: Optional[str] = None
    type: str  # "movie" or "series"

class MovieCreate(MovieBase):
    pass

class MovieUpdate(BaseModel):
    watched: bool

class MovieOut(MovieBase):
    id: int
    watched: bool

    class Config:
        orm_mode = True
