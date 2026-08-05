from typing import List
from fastapi import FastAPI, Depends, status, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "mysql+pymysql://root:minhhaycuoi2006@localhost:3306/library_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    price = Column(Numeric(10, 2), nullable=False, default=0)
    pages = Column(Integer, nullable=False, default=0)

Base.metadata.create_all(bind=engine)

class BookCreate(BaseModel):
    code: str
    title: str
    price: float
    pages: int

class BookResponse(BookCreate):
    id: int

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    existing_book = db.query(BookModel).filter(BookModel.code == book.code).first()
    if existing_book:
        raise HTTPException(status_code=400, detail="Mã sách đã tồn tại trong hệ thống!")
    
    new_book = BookModel(
        code=book.code,
        title=book.title,
        price=book.price,
        pages=book.pages
    )
    
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    
    return new_book

@app.get("/books", response_model=List[BookResponse], status_code=status.HTTP_200_OK)
def get_books(db: Session = Depends(get_db)):
    books = db.query(BookModel).all()
    return books