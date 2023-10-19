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
        # Select arandom question from topic_questions, pop it out and 
        # add it to the ten_questions list
        ten_questions.append(
            topic_questions.pop(
                random.randint(0, len(topic_questions) - 1)))
    
    # print([q[0] for q in ten_questions])  # --> DEBUG
    return ten_questions






#------------------------Test-runs-------------------------------------|

#create a list of template questions
q_list = [["Question " + str(i+1), "Right answer1", "Wrong answer2", "Wrong answer3", "Wrong answer4"] for i in range(100)]
quiz_round(question_selector(q_list))
    
    