# Database Connection Preparation

# Start PostgreSQL Database Container
cd .docker
docker-compose up -d

# Install Python Connectivity to PostgreSQL
pip install "psycopg[binary]"

# Trigger Alembic Migrations
python app.py
