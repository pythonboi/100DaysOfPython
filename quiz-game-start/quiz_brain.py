class QuizBrain:

    def __init__(self, myList):
        self.question_number = 0
        self.question_list = myList
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            self.next_question()
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        User_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(User_ans, current_question.answer)

    def check_answer(self, User_ans, current_answer):
        if User_ans.lower() == current_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
            print(f"The correct answer was {current_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")






