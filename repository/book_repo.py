from models.book_db import books_storage
from uuid import UUID
from typing import List, Optional

class BookRepository:
    async def get_all(self) -> List[dict]:
        return books_storage

    async def get_by_id(self, book_id: UUID) -> Optional[dict]:
        return next((b for b in books_storage if b["id"] == book_id), None)

    async def add(self, book_data: dict) -> dict:
        books_storage.append(book_data)
        return book_data

    async def delete(self, book_id: UUID) -> bool:
        for i, book in enumerate(books_storage):
            if book["id"] == book_id:
                books_storage.pop(i)
                return True
        return False