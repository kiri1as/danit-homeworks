import subprocess


def log_processing(func):
    def wrapper(*args, **kwargs):
        print("... Processing db migration started ... ")
        res = func(*args, **kwargs)
        print("... Processing db migration finished ... ")
        return res

    return wrapper


@log_processing
def run_migration(downgrade=False):
    if downgrade:
        subprocess.run(["alembic", "downgrade", "-1"], check=True)
    else:
        subprocess.run(["alembic", "upgrade", "head"], check=True)
