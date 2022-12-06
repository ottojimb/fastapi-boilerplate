from fastapi import HTTPException, status


class DoesNotExist(Exception):
    """Raised when entity was not found in database."""

    def __init__(self, message: str):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)
