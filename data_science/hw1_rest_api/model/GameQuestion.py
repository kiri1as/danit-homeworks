from data_science.hw1_rest_api.model.BaseModel import BaseModel
from sqlalchemy import Column, Text, Numeric, CHAR, CheckConstraint


class GameQuestion(BaseModel):
    __tablename__ = 'game_questions'

    question_id =   Column(Numeric, primary_key=True, autoincrement=True)
    question_text = Column(Text, nullable=False)
    question_answer_a = Column(Text, nullable=False)
    question_answer_b = Column(Text, nullable=False)
    question_answer_c = Column(Text, nullable=False)
    question_answer_d = Column(Text, nullable=False)
    question_correct_answer = Column(CHAR, nullable=False)

    __table_args__ = (
        CheckConstraint(
            "question_correct_answer IN ('a', 'b', 'c', 'd')",
            name='check_correct_answer'
        ),
    )
