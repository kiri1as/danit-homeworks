# Database Connection Preparation

Follow these steps to set up and prepare the database connection for your project.

## Step 1: Start PostgreSQL Database Container

Navigate to the `.docker` directory and start the PostgreSQL database container using Docker Compose:

```sh

cd .docker
docker-compose up -d
```

## Step 2: Install Python Connectivity to PostgreSQL

Ensure Python can connect to PostgreSQL by installing the psycopg package:

```sh

pip install "psycopg[binary]"
```

## Step 3: Trigger Alembic Migrations (automated before each run)

Before executing any other code, app.py script runs migrations

```sh

python app.py
```