from fastapi import APIRouter, status, HTTPException, Depends
from database import get_db
from app.services.book_services import update_book_service, delete_book_service, get_all_books_service, get_book_by_id_service, create_book_service
from app.schemas.book_schema import UpdateBook, BookResponse, CreateBook
from sqlalchemy.orm import Session

router = APIRouter(prefix='/books', tags=['Books'])

@router.put('/{id}')
def update_book(id: int, upd_book: UpdateBook, db: Session = Depends(get_db)):
    book = update_book_service(id, upd_book, db)
    
    if book == 'Not found':
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Sách không tồn tại trong hệ thống'
        )
        
    return book

@router.delete('/{id}')
def delete_book(id: int, db: Session = Depends(get_db)):
    book = delete_book_service(id, db)
        
    if book == 'Not found':
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Sách không tồn tại trong hệ thống'
        )
        
    return {"message": f"Đã xóa thành công sách ID {id}"}

@router.get('/', response_model=list[BookResponse])
def get_all_book(db: Session = Depends(get_db)):
    books = get_all_books_service(db)
    
    return books

@router.get('/{id}', response_model=BookResponse)
def get_book_by_id(id: int, db: Session = Depends(get_db)):
    book = get_book_by_id_service(id, db)
    
    if book == 'Not found':
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Sách không tồn tại trong hệ thống'
            )
            
    return book

@router.post('/', response_model=BookResponse)
def create_book(new_book: CreateBook, db: Session =Depends(get_db)):
    book = create_book_service(new_book, db)
    
    return book