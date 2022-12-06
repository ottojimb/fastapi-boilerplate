import abc
from typing import Any, Generic, List, Optional, Type, TypeVar

from sqlalchemy import and_, asc, desc, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.exceptions import DoesNotExist
from app.models.schemas.base import BaseSchema

IN_SCHEMA = TypeVar("IN_SCHEMA", bound=BaseSchema)
EDIT_SCHEMA = TypeVar("EDIT_SCHEMA", bound=BaseSchema)
SCHEMA = TypeVar("SCHEMA", bound=BaseSchema)
TABLE = TypeVar("TABLE")


class BaseRepository(
    Generic[IN_SCHEMA, EDIT_SCHEMA, SCHEMA, TABLE], metaclass=abc.ABCMeta
):
    def __init__(self, db_session: AsyncSession, *args, **kwargs) -> None:
        self._db_session: AsyncSession = db_session

    @property
    @abc.abstractmethod
    def _table(self) -> Type[TABLE]:
        ...

    @property
    @abc.abstractmethod
    def _schema(self) -> Type[SCHEMA]:
        ...

    def parse_params(self, params: dict) -> list[Any]:
        parsed = []
        for key, value in params.items():
            if not hasattr(self._table, key):
                continue

            if type(value) is str:
                parsed.append(getattr(self._table, key).ilike(value))
            elif type(value) in [int, float, bool]:
                parsed.append(getattr(self._table, key) == value)

        return parsed

    async def create(self, in_schema: IN_SCHEMA) -> SCHEMA:
        entry = self._table(**in_schema.dict(exclude_unset=True, exclude_none=True))
        self._db_session.add(entry)
        await self._db_session.flush()
        return self._schema.from_orm(entry)

    async def get_by_id(self, entry_id: int) -> SCHEMA:
        entry = await self._db_session.get(self._table, entry_id)
        if not entry:
            raise DoesNotExist(f"{self._table.__name__}<id:{entry_id}> does not exist")
        return self._schema.from_orm(entry)

    async def get_ordered(self, order: str, value: str):
        order_fx = asc if (order == "ascend") else desc
        query = select(self._table).order_by(order_fx(getattr(self._table, value)))
        q = await self._db_session.execute(query)
        return q.scalars().all()

    async def get(self, *, method=and_, params: Optional[dict] = None) -> List[SCHEMA]:
        if params:
            filters = self.parse_params(params)
            query = (
                select(self._table)
                .filter(method(*filters))
                .order_by(getattr(self._table, "id"))
            )
        else:
            query = select(self._table).order_by(desc(getattr(self._table, "id")))

        q = await self._db_session.execute(query)

        return q.scalars().all()

    async def put(self, id: int, values: EDIT_SCHEMA) -> int:
        query = (
            update(self._table)
            .where(getattr(self._table, "id") == id)
            .values(
                **values.dict(
                    exclude_unset=True,
                    exclude_none=True,
                )
            )
        )
        q = await self._db_session.execute(query)
        return q.rowcount
