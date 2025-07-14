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

def update_movie(db: Session, movie_id: int, movie_update: schemas.MovieUpdate):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not movie:
        return None
    update_data = movie_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(movie, key, value)
    db.commit()
    db.refresh(movie)
    return movie

def update_watch_status(db: Session, movie_id: int, watched: bool):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if movie:
        movie.watched = watched
        db.commit()
        db.refresh(movie)
    return movie

def delete_movie(db: Session, movie_id: int):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if movie:
        db.delete(movie)
        db.commit()
        return True
    return False
