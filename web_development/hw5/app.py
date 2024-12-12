import logging

# logger configuration for app.log file
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s',
                    handlers=[logging.FileHandler(".data/app.log")])

from controllers import init_db, main_loop

if __name__ == '__main__':
    print("--- Starting app ---")
    init_db()
    main_loop()
    print("--- Ending app ---")

