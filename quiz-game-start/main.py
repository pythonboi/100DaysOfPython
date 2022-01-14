from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    myQue = Question(text=question['text'], answer=question['answer'])
    question_bank.append(myQue)
    # question_bank.append(myQue.answer)

quiz = QuizBrain(question_bank)
quiz.next_question()

print(len(question_bank))

while quiz.still_has_question():
    quiz.still_has_question()

if len(question_bank) == quiz.question_number:
    print("You've completed the quiz")
    print(f"Your final score was {quiz.score}/{quiz.question_number}")
