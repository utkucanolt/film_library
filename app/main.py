from fastapi import FastAPI
from .database import Base, engine
from .routers import movies

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Film Library API 🎬"}

Base.metadata.create_all(bind=engine)
app.include_router(movies.router)
