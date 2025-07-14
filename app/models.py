from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)
    watched = Column(Boolean, default=False)
    type = Column(String)  # "movie" ya da "series"
