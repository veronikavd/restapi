from repository.book_repo import BookRepository
from schemas.book import BookCreate, BookStatus
from uuid import UUID, uuid4

class BookService:
    def __init__(self):
        self.repo = BookRepository()

    async def get_books(self, status: BookStatus = None, author: str = None, sort_by: str = None):
        books = await self.repo.get_all()
        
        if status:
            books = [b for b in books if b["status"] == status]
        if author:
            books = [b for b in books if author.lower() in b["author"].lower()]
            
        if sort_by:
            books = sorted(books, key=lambda x: x.get(sort_by))
            
        return books

    async def get_book_by_id(self, book_id: UUID):
        return await self.repo.get_by_id(book_id)

    async def create_book(self, book_in: BookCreate):
        new_book = book_in.model_dump()
        new_book["id"] = uuid4()
        return await self.repo.add(new_book)

    async def delete_book(self, book_id: UUID):
        await self.repo.delete(book_id)