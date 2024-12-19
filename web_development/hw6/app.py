from db_utils import run_migration
from controllers import menu_loop

if __name__ == "__main__":
    run_migration()
    menu_loop()
