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

### How to test

Run:

```
pytest
```

### How to live code

Run:

```
uvicorn app.main:app --reload
```

### How to debug

Run:

```
ipython -m uvicorn app.main:app --pdb
```

Or press F5 in vscode

### How to get the coverage to pass it on to your Project Manager and avoid stupid questions about your progress:

```
pytest --cov=app
```
