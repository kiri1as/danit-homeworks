import os

from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(bind=engine)

def close_all_sessions():
    engine.dispose()
    print("\n... SQLAlchemy sessions terminated")
