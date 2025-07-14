from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    description: str | None = None
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
