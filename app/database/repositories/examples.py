from typing import Type

from app.database.repositories.base import BaseRepository
from app.database.tables.examples import Examples
from app.models.schemas.example import ExampleSchema, EditExampleSchema, InExampleSchema


class ExampleRepository(
    BaseRepository[InExampleSchema, EditExampleSchema, ExampleSchema, Examples]
):
    @property
    def _in_schema(self) -> Type[InExampleSchema]:
        return InExampleSchema

    @property
    def _schema(self) -> Type[ExampleSchema]:
        return ExampleSchema

    @property
    def _table(self) -> Type[Examples]:
        return Examples
