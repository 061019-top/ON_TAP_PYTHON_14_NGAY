from fastapi import FastAPI
from app.routers.book_routers import router as book_router
from database import Base, engine


app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(book_router)