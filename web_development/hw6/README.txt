Database connection preparation steps:
1) To start postgres db container:
    $ cd .docker
    $ docker-compose up -d
2) Python connectivity to postgres provided by installing:
    $  pip install "psycopg[binary]"
3) alembic migrations are triggered by "app.py" script before other code execution

