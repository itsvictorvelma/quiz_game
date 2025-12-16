class QuizBrain:
    def __init__(self, q_list):
        # Track current question index, store question objects, and keep score
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        # Return True if there are questions left in the quiz
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Get the current question and increment the index
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        while True:
            # Prompt user for answer and clean input
            user_answer = input(
                f"Q{self.question_number}: {current_question.text} (True/False)?: "
            ).capitalize().strip()

            # Accept only valid True/False answers
            if user_answer == "True" or user_answer == "False":
                self.check_answer(user_answer, current_question.answer)
                break
            else:
                print("invalid input")  # Reject invalid entries

    def check_answer(self, user_answer, correct_answer):
        # Compare user input to correct answer and update score
        if user_answer == correct_answer:
            self.score += 1
            print("\nCorrect")
        else:
            print("\nIncorrect")
            print(f"The answer was {correct_answer}...")

        # Show current score after each question
        print(f"Your current score is: {self.score}/{self.question_number}\n")
