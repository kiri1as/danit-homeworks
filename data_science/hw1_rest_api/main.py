from dotenv import load_dotenv
import os

from data_science.hw1_rest_api.service import GameService

if __name__ == "__main__":
    load_dotenv()
    DB_URL = (f'postgresql+psycopg2://'
              f'{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}'
              f'@localhost:{os.getenv('POSTGRES_PORT')}'
              f'/{os.getenv('POSTGRES_DB')}')

    service = GameService(DB_URL)
    question = service.get_question_by_id(1)
    print(question.question_text)