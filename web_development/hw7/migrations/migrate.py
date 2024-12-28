import subprocess


def run_migration(downgrade=False):
    if downgrade:
        subprocess.run(["alembic", "downgrade", "-1"], check=True)
    else:
        subprocess.run(["alembic", "upgrade", "head"], check=True)