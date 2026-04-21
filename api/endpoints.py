from fastapi import APIRouter, HTTPException, status, Query
from schemas.book import Book, BookCreate, BookStatus
from services.book_service import BookService
from uuid import UUID
from typing import List, Optional

router = APIRouter()
service = BookService()

@router.get("/", response_model=List[Book])
async def read_books(
    status: Optional[BookStatus] = None,
    author: Optional[str] = None,
    sort_by: Optional[str] = Query(None, pattern="^(title|year)$")
):
    return await service.get_books(status, author, sort_by)

@router.get("/{book_id}", response_model=Book)
async def read_book(book_id: UUID):
    book = await service.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книгу не знайдено")
    return book

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book: BookCreate):
    return await service.create_book(book)

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: UUID):
    await service.delete_book(book_id)
    return None 