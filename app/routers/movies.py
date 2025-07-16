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

@router.get("/movies/watched", response_model=list[schemas.WatchedMovie])
def read_watched_movies(db: Session = Depends(get_db)):
    return crud.get_watched_movies(db)

@router.get("/movies/{movie_id}", response_model=schemas.MovieOut)  # response_model MovieOut olmalı
def read_movie_by_id(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id)  # crud'da fonksiyonun adı get_movie
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.post("/movies", response_model=schemas.MovieOut, status_code=201)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)

# 🎯 Genel film güncelleme endpoint
@router.put("/movies/{movie_id}", response_model=schemas.MovieOut)
def update_movie(movie_id: int, movie_update: schemas.MovieUpdate, db: Session = Depends(get_db)):
    updated_movie = crud.update_movie(db, movie_id, movie_update)
    if not updated_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return updated_movie

# ✅ Sadece izlenme durumu güncelleme endpoint (ayrı olarak gösterilecek)
@router.put("/movies/{movie_id}/watched", response_model=schemas.MovieOut)
def mark_as_watched(movie_id: int, update: schemas.WatchStatusUpdate, db: Session = Depends(get_db)):
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
