import subprocess

def migration_upgrade():
    subprocess.run(["alembic", "upgrade", "head"], check=True)

def migration_downgrade():
    subprocess.run(["alembic", "downgrade", -1], check=True)