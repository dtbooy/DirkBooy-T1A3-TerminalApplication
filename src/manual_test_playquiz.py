"""
This file is used to manually test the playquiz.py functions 
are working correctly. It generates a test quiz file with 
numbered questions and the correct answer indicated and runs it 
through the quiz round handler.
"""
import playquiz

#-------------Manual Test-runs----------------------|

# create a list of template questions
q_list = [
    ["Question " + str(i+1), 
     "Right answer1", 
     "Wrong answer2", 
     "Wrong answer3", 
     "Wrong answer4"] 
     for i in range(50)
     ]

# Start a round 
q = playquiz.quiz_round(q_list)


#test the ask_question function
#ask_question(q[0], 1)





