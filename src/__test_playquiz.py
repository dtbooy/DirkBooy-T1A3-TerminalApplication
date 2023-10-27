import playquiz
import pytest

#----------
# functions in playqiz.py
## clear_screen() ---> process
## question_selectior(topic_questions) 
## ask_question(question, q_num)
## get_valid_answer()
## print_title()
## quiz_round()

pytest
def ask_question(question, q_num):
    pass


#------------------------Test-runs-------------------------------------|

#create a list of template questions
# q_list = [
#     ["Question " + str(i+1), 
#      "Right answer1", 
#      "Wrong answer2", 
#      "Wrong answer3", 
#      "Wrong answer4"] 
#      for i in range(5)
#      ]

#start a round 
# q = playquiz.quiz_round(q_list)
# question_selector(q_list)
#test the ask_question function
#ask_question(q[0], 1)

topic = ""
while topic == None or (topic.replace(" ", "").isalnum() == False):
    topic = input("what si topic?")



