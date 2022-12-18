import html

import requests

from question_model import Question
from quiz_brain import QuizBrain

api_results = requests.get("https://opentdb.com/api.php?amount=20&category=31&type=boolean").json()
question_bank = []
for i in api_results["results"]:
    question = Question(html.unescape(i["question"]), i["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    print("You've completed the quiz.")
    print(f"Your final score was {quiz.score}/{quiz.question_number}")
