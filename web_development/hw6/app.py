from db_utils import run_migration
from controllers import main_menu_loop

if __name__ == "__main__":
    run_migration()
    main_menu_loop()
