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

@router.post("/movies", response_model=schemas.MovieOut)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)

@router.put("/movies/{movie_id}", response_model=schemas.MovieOut)
def mark_as_watched(movie_id: int, update: schemas.MovieUpdate, db: Session = Depends(get_db)):
    movie = crud.update_watch_status(db, movie_id, update.watched)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie
