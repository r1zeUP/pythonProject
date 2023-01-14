import json

from question import Question


def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = []
    for item in data:
        text = item['q']
        difficulty = item['d']
        right_answer = item['a']
        question = Question(text, difficulty, right_answer)
        questions.append(question)
    return questions


def build_statistics(questions):
    score = 0
    count_answer = 0

    for question in questions:
        if question.is_correct():
            score += question.score
            count_answer += 1
    return f'Вот и все!\n' \
           f'Отвечено на {count_answer} вопроса из {len(questions)}\n' \
           f'Набранно баллов: {score}'