
# Imports
import file_handling

# random module used to randomise question selection & shuffle answers
import random
# os module used to detect Operating System & clear terminal screen
import os
# time module used for time keeping for scoring
import time
# getpass used to hide user input for "press enter to continue" breaks
import getpass
# shutil module get_terminal_size() function to determine screen width
import shutil


def clear_screen() -> None:
    """
    Detects Operating System and selects appropriate command to clear
    the terminal screen
    """
    # Windows: os.name == nt, sys clear command is "cls"
    if os.name == 'nt':
        os.system("cls")
    # Linux: os.name == 'posix', sys clear command is "clear"
    else:
        os.system("clear")


def print_title(title: str) -> None:
    """ Print a decorated heading on the console from input string."""
    # Determine screen width (redo each time incase screen size changes)
    screen_width = min(100, list(shutil.get_terminal_size())[0])
    # Detemine padding space each side of title
    padding = max(int((screen_width - len(title) - 2) / 2), 0)
    # Clear screen
    clear_screen()
    # Print title padded by #'s with a line of -'s above and below
    print("-" * screen_width)
    print("#" * padding, title, "#" * padding)
    print("-" * screen_width)


def question_selector(topic_questions: list) -> list:
    """
    Get a random selection of 10 questions from input parameter
    topic_questions. Return list of 10 questions.
    """
    ten_questions = []
    for i in range(min(10, len(topic_questions))):
        # Select a random question from topic_questions, pop it out and
        # add it to the ten_questions list.
        # If topic_question list < 10 select <10 questions.
        ten_questions.append(
            topic_questions.pop(
                random.randint(0, len(topic_questions) - 1)))
    return ten_questions


def ask_question(question: list, q_num: int) -> int:
    """
    Takes a question & question number, prints to terminal. Shuffles
    answer options and prints to terminal.
    Returns index of correct answer.
    """
    # Present question
    print(f"Question {q_num + 1}: {question[0]}")

    # Shuffle answers
    ans_list = question[1:]
    random.shuffle(ans_list)

    # Print answers to terminal - shuffled & each printed on a line
    for i, ans in enumerate(ans_list):
        print(f"{chr(ord('A') + i)}: {ans}")

    # Return index integer of correct answer (A=1, B=2, C=3, D=4).
    # Note: +1 is added to account for in Q&A list index 0 is Question.
    return ans_list.index(question[1]) + 1


def get_valid_answer() -> int:
    """
    Gets answer from user. Confirms valid input. On invalid response
    prompts user for valid answer until valid answer given.
    Returns valid input as answer integer (A=1, B=2, C=3, D=4)
    """
    while True:
        answer = input("Enter your selection: ")
        match answer.lower():
            case "a" | "1":
                return 1
            case "b" | "2":
                return 2
            case "c" | "3":
                return 3
            case "d" | "4":
                return 4
            case _:
                print(
                    "Invalid selection \n"
                    "Selection must be in the form A, B, C, D or "
                    "1, 2, 3, 4"
                    )


def quiz_round(topic: str):
    """Quiz handler: runs a round of quiz questions and tracks score."""
    # Reset score counter.
    round_score = 0
    # Reset correct counter.
    correct_counter = 0
    # Reset wrong questions.
    wrong_questions = []
    # Get question list.
    topic_questions_list = (
        file_handling.get_question_list_from_file(topic))

    # Get round questions.
    round_questions = question_selector(topic_questions_list)
    for index, question in enumerate(round_questions):
        print_title(topic)
        # Display Question.
        ans_loc = ask_question(question, index)
        # Start question timer.
        start = time.time()
        # Get response from user.
        user_resp = get_valid_answer()
        # Calculate response time.
        ans_time = round(time.time() - start)
        # Check - is user correct- if so give a point.
        if ans_loc == user_resp:
            # Calculate points.
            points = max(1, 11 - (ans_time))
            # Add points to score.
            round_score += points
            correct_counter += 1
            print(
                f"Correct! You answered in {ans_time} seconds and get "
                f"{points} points")
            print(ans_loc)
        else:
            print("Wrong answer!")
            wrong_questions.append(index)
            print(f"The correct answer was: {question[1]}")
        # Press enter to start next question.
        getpass.getpass("Press Enter to continue...")
    # End of Quiz display results.
    print_title("Results")
    print(
        f"You got {correct_counter} / {len(round_questions)} correct, "
        f"scoring {round_score} points!\n")
    if correct_counter == len(round_questions):
        # Print a special message for getting 10/10.
        print("""
        #         ________            ________          ___________
        #         ___  __  ______________  __/____________  /___  /
        #         __  /_/ /  _  _  ___/_  /_ _  _    ___/  __/_  /
        #         _  ____//  __/  /   _  __/ /  __/ /__ / /_  /_/
        #         /_/      ___//_/    /_/     ___/ ___/  __/ (_) \n""")
    else:
        # Display the questions the user got wrong for review
        print("You got the following question wrong:")
        for i in wrong_questions:
            print(f"Question {i+1}:")
            print(round_questions[i][0])
            print("The correct answer was:")
            print(round_questions[i][1], "\n")

    getpass.getpass("Press Enter to continue...")
