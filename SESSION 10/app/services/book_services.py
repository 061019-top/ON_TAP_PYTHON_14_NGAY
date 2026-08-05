from sqlalchemy.orm import Session
from app.schemas.book_schema import UpdateBook, CreateBook
from app.models.book_model import BookModel

def update_book_service(id: int, upd_book: UpdateBook, db: Session):
    book = db.query(BookModel).filter(BookModel.id == id).first()
    
    if not book:
        return 'Not found'
    
    for key, value in upd_book.model_dump().items():
        setattr(book, key, value)
    
    db.commit()
    db.refresh(book)
    
    return book

def delete_book_service(id: int, db: Session):
    book = db.query(BookModel).filter(BookModel.id == id).first()

    if not book:
            return 'Not found'
        
    db.delete(book)
    db.commit()
    
    return book

def get_all_books_service( db: Session):
    books = db.query(BookModel).all()
    
    return books

def get_book_by_id_service(id: int, db: Session):
    book = db.query(BookModel).filter(BookModel.id == id).first()
        
    if not book:
        return 'Not found'
    
    return book

def create_book_service(new_book: CreateBook, db: Session):
    book = BookModel(**new_book.model_dump())
    
    db.add(book)
    db.commit()
    db.refresh(book)
    
    return book