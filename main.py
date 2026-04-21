from fastapi import FastAPI
from api.endpoints import router as book_router

app = FastAPI(title="Library API")

app.include_router(book_router, prefix="/books", tags=["Books"])

@app.get("/")
def root():
    return {"message": "Welcome to Library API. Go to /docs for Swagger."}