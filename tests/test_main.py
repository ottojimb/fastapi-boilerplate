import pytest

pytestmark = pytest.mark.asyncio


async def test_read_root(async_client):
    response = await async_client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": """Please take a look to the /docs endpoint"""
    }


async def test_create_example(async_client):
    payload = {"message": "this is the payload"}
    response = await async_client.post("/examples", json=payload)
    assert response.json()["message"] == "this is the payload"
    assert "id" in response.json()
    assert "created_at" in response.json()
    assert "updated_at" in response.json()


async def test_get_examples(async_client):
    payload = {"message": "this is the payload"}
    await async_client.post("/examples", json=payload)
    response = await async_client.get("/examples")
    assert len(response.json()) == 1


async def test_get_one_example(async_client):
    payload = {"message": "this is the payload"}
    example = await async_client.post("/examples", json=payload)
    response = await async_client.get(f"/examples/{example.json()['id']}")
    assert response.json()["id"] == example.json()["id"]


async def test_example_deletion(async_client):
    payload = {"message": "this is the payload"}
    example = await async_client.post("/examples", json=payload)
