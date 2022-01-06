from data import question_data
from question_model import Question

question_bank = []

lenQue = len(question_data)
print(lenQue)



for question in question_data:
    myQue = Question(text=question['text'], answer=question['answer'])
    question_bank.append(myQue.text)
    question_bank.append(myQue.answer)

print(question_bank)
