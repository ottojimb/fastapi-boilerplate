from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/example")
async def example():
    return {"data": {"message": "this is a short message"}}
