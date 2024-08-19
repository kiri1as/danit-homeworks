import os

from dotenv import load_dotenv
from flask import Blueprint, jsonify, request

from data_science.hw1_rest_api.service import GameService

load_dotenv()

DB_URL = (f'postgresql+psycopg2://'
          f'{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}'
          f'@localhost:{os.getenv('POSTGRES_PORT')}'
          f'/{os.getenv('POSTGRES_DB')}')
service = GameService(DB_URL)

bp = Blueprint('main', __name__)


@bp.route('/question/<int:question_id>', methods=['GET'])
def get_question(question_id):
    game_question = service.get_question_by_id(question_id)
    resp = {}

    if game_question is None:
        return jsonify(question_not_found_resp(question_id)), 400

    result = {
        "question_id": game_question.question_id,
        "question_text": game_question.question_text,
        "options": {
            'a': game_question.question_answer_a,
            'b': game_question.question_answer_b,
            'c': game_question.question_answer_c,
            'd': game_question.question_answer_d
        }
    }
    resp["data"] = result
    resp["status"] = "SUCCESS"
    return jsonify(resp), 200


@bp.route('/answer/<int:question_id>', methods=['POST'])
def check_answer(question_id):
    resp = {}
    req_payload = request.get_json()

    if req_payload is None or str(req_payload.get("option")).lower() not in ('a', 'b', 'c', 'd'):
        return invalid_answer_option_resp(), 400

    game_question = service.get_question_by_id(question_id)

    if game_question is None:
        return jsonify(question_not_found_resp(question_id)), 400

    user_option = req_payload.get("option")
    game_correct_answer = game_question.question_correct_answer

    if user_option == game_correct_answer:
        resp["data"] = {
            "message": "Congrats! You are right!"
        }
    else:
        resp["data"] = {
            "message": f"Wrong answer. Correct answer: {game_correct_answer}"
        }

    resp["status"] = "SUCCESS"
    return jsonify(resp), 200


def question_not_found_resp(question_id: int) -> dict:
    return {
        "message": f"Question {question_id} not found",
        "status": "ERROR",
    }


def invalid_answer_option_resp() -> dict:
    return {
        "message": "Invalid game option provided",
        "status": "ERROR",
    }
