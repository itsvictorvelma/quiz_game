from question_model import Question  # Question class for quiz items
from data import question_data  # List of question dicts
from quiz_brain import QuizBrain  # Handles quiz logic
import os  # For clearing the terminal screen


def clear_screen():
    # Clear terminal for Windows or Unix-based systems
    os.system("cls" if os.name == "nt" else "clear")


def quiz_game():
    # Prepare the list of Question objects from raw data
    question_bank = []
    for item in question_data:
        question_text = item['text']
        question_answer = item['answer']
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    # Initialize quiz logic with question bank
    quiz = QuizBrain(question_bank)

    game_over = False
    while not game_over:
        # Ask user if they want to start
        start = input("\nStart quiz? (y/n): ").lower().strip()

        if start == "y":
            clear_screen()

            # Loop through questions until finished
            while quiz.still_has_questions():
                quiz.next_question()

                # End of quiz
                if not quiz.still_has_questions():
                    print("You've completed the quiz")
                    print(f"Your final score is: {quiz.score}/{len(question_bank)}")
                    game_over = True

        elif start == "n":
            print("Thank you for your time!")
            game_over = True

        else:
            print("invalid input")

        # Option to replay
        if game_over:
            play_again = input("\nWould you like to play again? (y/n): ")
            if play_again == "y":
                clear_screen()
                quiz_game()  # Restart the quiz
            else:
                print("\nThanks for playing, see you next time!")
                break


quiz_game()  # Run the game
