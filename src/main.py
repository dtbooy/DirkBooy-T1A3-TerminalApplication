#----------------------------------------------------------------------|
# Imports
# random module used to randomise question selection & shuffle answers
import random
# os module used to detect Operating System & clear terminal screen 
import os 
# time module used for delay timing 
# may also be used for timeout of questions and scoring   --------------------->  DEBUG
import time

def clear_screen():
    """
    Detects Ooperating systems and uses appropriate command to clear 
    the terminal screen 
    """
    # Windows: os.name == nt, sys clear command is "cls"
    if os.name == 'nt':
        os.system("cls")
     # Linux: os.name == 'posix', sys clear command is "clear"
    else:
        os.system("clear")

def question_selector(topic_questions: list) -> list:
    """
    Get a random selection of 10 questions from input parameter
    topic_questions. Return list of 10 questions.
    """
    ten_questions = []
    for i in range (10):    
        # Select a random question from topic_questions, pop it out and 
        # add it to the ten_questions list
        ten_questions.append(
            topic_questions.pop(
                random.randint(0, len(topic_questions) - 1)))
    # print([q[0] for q in ten_questions])  # ----------------------------------> DEBUG
    return ten_questions

def ask_question(question: list, q_num: int) -> int:
    """
    Takes a question & question number, prints to terminal.
    Shuffles answer options and prints to terminal. 
    Returns index of correct answer
    """
    # Present question
    print(f"Question {q_num + 1}: {question[0]}")
    
    # Shuffle answers
    ans_list = question[1:]
    random.shuffle(ans_list)    
    
    for i, ans in enumerate(ans_list):
    # print answers to terminal  - shuffled & each printed on a line 
        print(f"{chr(ord('A') + i)}: {ans}")

    # Return index integer of correct answer (A=1, B=2, C=3, D=4).
    # Note: +1 is added to account for in Q&A list index 0 is Question. 
    # print(ans_list.index(question[1]) + 1)              #    ---------------------> DEBUG
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


def quiz_round(questions_list: list):
    """takes a list of 10 questions and plays the quiz"""
    # reset score counter
    round_score = 0

    for index, question in enumerate(questions_list):
        
        
        # Display Question
        ans_loc = ask_question(question, index + 1)

        # Get response from user
        user_resp = get_valid_answer()

        # Check - is user correct- if so give a point
        if ans_loc == user_resp:
            round_score += 1
            print("Correct! Well Done!")
            print(ans_loc)

        # Display the correct answer & feedback to user 
        print(f"The correct answer was: {question[1]}")

        # wait 3 seconds before next question starts
        time.sleep(3)
        # Clear screen for next question
        clear_screen()
        #EOL




#------------------------Test-runs-------------------------------------|

#create a list of template questions
q_list = [
    ["Question " + str(i+1), 
     "Right answer1", 
     "Wrong answer2", 
     "Wrong answer3", 
     "Wrong answer4"] 
     for i in range(100)
     ]

#start a round 
q = quiz_round(question_selector(q_list))
# question_selector(q_list)
#test the ask_question function
#ask_question(q[0], 1)

    