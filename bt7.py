from fastapi import FastAPI

app = FastAPI()

danh_sach_sach = [
    {
        "id": 1,
        "ten_sach": "Nhà Giả Kim",
        "tac_gia": "Paulo Coelho",
        "nam_xuat_ban": 1988,
        "so_luong": 5
    },
    {
        "id": 2,
        "ten_sach": "Clean Code",
        "tac_gia": "Robert C. Martin",
        "nam_xuat_ban": 2008,
        "so_luong": 3
    }
]

@app.post("/api/v1/books")
def create_book(book: dict):
    danh_sach_sach.append(book)
    return book

@app.get("/api/v1/books")
def get_all_books():
    return danh_sach_sach

@app.get("/api/v1/books/{book_id}")
def get_book_by_id(book_id: int):
    for book in danh_sach_sach:
        if book["id"] == book_id:
            return book
    return {"detail": f"Không tìm thấy sách với id: {book_id}"}, 404

@app.put("/api/v1/books/{book_id}")
def update_book(book_id: int, updated_book: dict):
    for index, book in enumerate(danh_sach_sach):
        if book["id"] == book_id:
            updated_book["id"] = book_id
            danh_sach_sach[index] = updated_book
            return updated_book
    return {"detail": f"Không tìm thấy sách với id: {book_id}"}, 404

@app.delete("/api/v1/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(danh_sach_sach):
        if book["id"] == book_id:
            deleted_book = danh_sach_sach.pop(index)
            return {"message": f"Đã xóa thành công sách với id: {book_id}", "book": deleted_book}
    return {"detail": f"Không tìm thấy sách với id: {book_id}"}, 404