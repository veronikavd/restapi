import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_create_and_get_book():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        payload = {
            "title": "Tigers",
            "author": "Ivan Bahrianyi",
            "year": 1944,
            "status": "наявна"
        }
        post_res = await ac.post("/books/", json=payload)
        assert post_res.status_code == 201
        book_id = post_res.json()["id"]

        get_res = await ac.get(f"/books/{book_id}")
        assert get_res.status_code == 200
        assert get_res.json()["title"] == "Tigers"

@pytest.mark.asyncio
async def test_delete_book_idempotent():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        fake_id = "550e8400-e29b-41d4-a716-446655440000"
        res1 = await ac.delete(f"/books/{fake_id}")
        res2 = await ac.delete(f"/books/{fake_id}")
        
        assert res1.status_code == 204
        assert res2.status_code == 204