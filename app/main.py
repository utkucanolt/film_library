from fastapi import FastAPI
from app.database import Base, engine
from app.routers.movies import router as movies_router

app = FastAPI(title="Film Library API 🎬")

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

@app.get("/", tags=["root"])
def read_root():
    return {"message": "Welcome to the Film Library API 🎬"}

# /movies endpoint’lerini ekliyoruz
app.include_router(movies_router, prefix="/movies", tags=["movies"])
