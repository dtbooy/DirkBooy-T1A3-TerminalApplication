#----------------------------------------------------------------------|
#imports
import random

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
    # print(g[q[0] for q in ten_questions])  # --> DEBUG
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

    # return index integer of correct answer (A=0, B=1, C=2, D=3)
    return ans_list.index(question[1])


def get_valid_answer():
    """
    Gets answer from user. Confirms valid input. On invalid response 
    prompts user for valid answer until valid answer given.
    Returns valid input as answer integer (A=0, B=1, C=2, D=3)
    """
    pass 
#current location
########################################################################



def quiz_round(questions_list: list):
    """takes a list of 10 questions and plays the quiz"""
    pass            # DEBUG - skip below code until finished
    for index, question in enumerate(questions_list):
        # Display user Question
        ans_loc = ask_question(question, index + 1)
        # Get response from user
        user_resp = get_valid_answer()
        # Check - is user correct- if so give a point
        # Display the correct answer & feedback to user 
        #######CODE GOES HERE######
        # Press enter to continue
        # Clear screen 
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

q = question_selector(q_list)
#print(q)
ask_question(q[0], 1)

    