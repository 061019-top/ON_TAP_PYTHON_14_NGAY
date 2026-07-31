from fastapi import FastAPI

app = FastAPI()

books_db = []
book_id_counter = 1

@app.post("/books")
def create_book(book: dict):
    global book_id_counter
    
    new_book = {
        "id": book_id_counter,
        "title": book.get("title"),
        "author": book.get("author"),
        "price": book.get("price"),
        "pages": book.get("pages")
    }
    
    books_db.append(new_book)
    book_id_counter += 1
    
    return new_book

@app.get("/books/{id}")
def get_book_by_id(id: int):
    for book in books_db:
        if book["id"] == id:
            return book
            
    return {"detail": "Book not found"}, 404