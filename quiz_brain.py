class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        question = self.question_list[self.question_number]
        answer = question.answer
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {question.text} (True/False)? "
        )
        while not user_answer.lower() in ["true", "false"]:
            print("Invalid input! Try again.")
            user_answer = input(
                f"Q.{self.question_number}: {question.text} (True/False)? "
            )
        self.check_answer(user_answer, answer)
            
    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():   
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer is {answer}")    
        print(f"Your current score is: {self.score}/{self.question_number}")
