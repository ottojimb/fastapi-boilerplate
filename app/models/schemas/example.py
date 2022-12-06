from datetime import datetime
from app.models.schemas.base import BaseSchema


class ExampleSchemaBase(BaseSchema):
    message: str | None = None


class InExampleSchema(ExampleSchemaBase):
    message: str


class EditExampleSchema(ExampleSchemaBase):
    ...


class ExampleSchema(InExampleSchema):
    id: int
    created_at: datetime
    updated_at: datetime
