from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/movies", response_model=list[schemas.MovieOut])
def read_movies(db: Session = Depends(get_db)):
    return crud.get_movies(db)

@router.get("/movies/{movie_id}", response_model=schemas.MovieOut)  # response_model MovieOut olmalı
def read_movie_by_id(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id)  # crud'da fonksiyonun adı get_movie
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.post("/movies", response_model=schemas.MovieOut)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)

@router.put("/movies/{movie_id}", response_model=schemas.MovieOut)
def mark_as_watched(movie_id: int, update: schemas.MovieUpdate, db: Session = Depends(get_db)):
    movie = crud.update_watch_status(db, movie_id, update.watched)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    success = crud.delete_movie(db, movie_id)
    if not success:
        raise HTTPException(status_code=404, detail="Movie not found")
    return
