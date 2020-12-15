# vex

### Install

#### Deps

```
pip install fastapi[all] uvicorn SQLAlchemy alembic
```

#### Database

* `cp alembic.ini.example alembic.ini` and update sqlalchemy url
* `PYTHONPATH=. alembic upgrade head`

#### Ship it

```
uvicorn main:app --reload
```
