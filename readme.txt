this project includes
1. fastapi
2. sqlalchemy - orm
3. pydantic
4. uvicorn - for running project asynchronously (uvicorn main:app --reload - to run project)
5. alembic - for managing migrations


NOTE :-
1. first install alembic. - pip install alembic
2. then run command  - alembic init alembic
3. this will create alembic folder for managing migrations
4. in alembic folder change env.py accordingly 
5. import all models there, and also set 
    target_metadata = Base.metadata
    config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

6. for applying migrations run command. - alembic revision --autogenerate -m "initial migration"
7. other useful commands
alembic upgrade head      # apply all migrations
alembic downgrade -1      # rollback last migration
alembic current           # see which migration is currently applied
alembic history           # see all migrations list

workflow :-
# 1. Make changes to your model
# 2. Generate migration
alembic revision --autogenerate -m "describe your change"
# 3. Apply migration
alembic upgrade head