from fastapi import APIRouter, Depends, status
from app.database.repositories.examples import ExampleRepository
from app.models.schemas.example import ExampleSchema, InExampleSchema
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.database import get_session

router = APIRouter()


@router.get("/examples", tags=["Examples"])
async def examples(
    db: AsyncSession = Depends(get_session),
):
    example_repository = ExampleRepository(db)
    examples = await example_repository.get()
    return examples


@router.post(
    "/examples",
    tags=["Examples"],
    response_model=ExampleSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_example(
    example: InExampleSchema,
    db: AsyncSession = Depends(get_session),
):
    example_repository = ExampleRepository(db)
    examples = await example_repository.create(example)
    return examples


@router.get("/examples/{example_id}", tags=["Examples"])
async def example_by_id(
    example_id: int,
    db: AsyncSession = Depends(get_session),
):
    example_repository = ExampleRepository(db)
    example = await example_repository.get_by_id(example_id)
    return example
