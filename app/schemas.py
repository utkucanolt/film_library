from pydantic import BaseModel
from typing import Optional

class MovieBase(BaseModel):
    title: str
    description: Optional[str] = None
    type: str  # "movie" or "series"

class MovieCreate(MovieBase):
    pass

class MovieUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    watched: Optional[bool] = None

class WatchStatusUpdate(BaseModel):
    watched: bool

class MovieOut(MovieBase):
    id: int
    watched: bool

    class Config:
        orm_mode = True
