create sequence game_questions_seq start with 1 increment by 1;

create table game_questions
(
    question_id             numeric not null default nextval('game_questions_seq') primary key,
    question_text           text    not null,
    question_answer_a       text    not null,
    question_answer_b       text    not null,
    question_answer_c       text    not null,
    question_answer_d       text    not null,
    question_correct_answer char    not null check (question_correct_answer in ('a', 'b', 'c', 'd'))
);