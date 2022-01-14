from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []


for question in question_data:
    myQue = Question(text=question['text'], answer=question['answer'])
    #newQue
    question_bank.append(myQue)
    #question_bank.append(myQue.answer)


quiz = QuizBrain(question_bank)
quiz.next_question()

print(question_bank)

print(myQue.text)
print(myQue.answer)

# lenQue = (question_bank[1])
# print(lenQue)


