from sqlalchemy.orm import Session
from . import models, schemas

def get_movies(db: Session):
    return db.query(models.Movie).all()

def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def update_watch_status(db: Session, movie_id: int, watched: bool):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if movie:
        movie.watched = watched
        db.commit()
        db.refresh(movie)
    return movie
