from os import getenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.routes import (
    example_router,
)
from app.core.config import settings

app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    debug=settings.DEBUG,
)

app.mount(
    "/static",
    StaticFiles(directory=getenv("STATIC_FILES_PATH", "app/static")),
    name="static",
)

app.include_router(example_router.router)

origins = [
    "http://locahost:3000",
    "https://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"message": """Please take a look to the /docs endpoint"""}
