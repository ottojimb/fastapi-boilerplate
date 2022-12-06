from sqlalchemy import Text, Column, DateTime, Integer
from sqlalchemy.sql import func

from app.database.session import Base


class Examples(Base):
    """Model for the Example Definition."""

    __tablename__ = "examples"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(Text, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    __mapper_args__ = {"eager_defaults": True}
