from data import question_data, new_Data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

# This code is working just to need to comment it for another code testing
#
# for question in question_data:
#     myQue = Question(text=question['text'], answer=question['answer'])
#     question_bank.append(myQue)
#     # question_bank.append(myQue.answer)
#
# quiz = QuizBrain(question_bank)
# quiz.next_question()
#
# print(len(question_bank))
#
# while quiz.still_has_question():
#     quiz.still_has_question()
#
# if len(question_bank) == quiz.question_number:
#     print("You've completed the quiz")
#     print(f"Your final score was {quiz.score}/{quiz.question_number}")

# newQuestion = Question(text='question', answer='correct_answer')

for data in new_Data:
    myNew = Question(text=data['question'], answer=data['correct_answer'])
    question_bank.append(myNew)
    # data.get('question')
    #print(myNew.answer)

# print(question_bank)

myQuiz = QuizBrain(question_bank)

while myQuiz.still_has_question():
    myQuiz.next_question()

print(myQuiz.next_question())
