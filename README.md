# FastAPI Boilerplate

Simple Personal FastAPI Boilerplate with postgres+postgis, auto generated migrations with alembic, sqlalchemy with async, pytest and docker

## How to use

1. Clone this repo
2. Install the requirements: `pip install -r requirements.txt`
3. Edit `app>core>config.py` to your needs
4. Write your models in `app>database>repositories`; `app>database>tables` and `app>models>schemas`
5. Write the test (yep, it is important, not for you but for your boss and to feel fashion using TDD)
6. Write a new router in `app/api/routes/`
7. Explore and fix the other things (I'm boring of looking each new thing that I need to do)

## Util commands

### How to test ๐งช

Run:

```
pytest
```

### How to live code ๐จโ๐ป/๐ฉโ๐ป

Run:

```
uvicorn app.main:app --reload
```

### How to debug ๐

Run:

```
ipython -m uvicorn app.main:app --pdb
```

Or press F5 in vscode

### How to get the coverage to pass it on to your Project Manager and avoid stupid questions about your progress ๐

```
pytest --cov=app
```

### How to build everything with docker-compose ๐๐ฆ

```
docker-compose up --build
```

### How to run the test in the docker compose (for CI/CD) ๐งช

```
docker-compose run fastapi-core pytest
```

๐ก Important Note: the pytest project was made to avoid interruptions with the real database, the data is ephemeral in each test

๐ก Important Note #2: There are some mypy issues to be fixed... someday...
