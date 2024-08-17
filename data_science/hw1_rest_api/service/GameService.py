from sqlalchemy.exc import NoResultFound

from .SingletonServiceMeta import SingletonServiceMeta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..model import GameQuestion


class GameService(metaclass=SingletonServiceMeta):
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def get_question_by_id(self, question_id):
        session = self.Session()
        try:
            question = session.query(GameQuestion).filter_by(question_id=question_id).one()
            return question
        except NoResultFound:
            return None
        finally:
            session.close()
