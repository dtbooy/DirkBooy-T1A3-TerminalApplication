import playquiz

#------------------------Test-runs-------------------------------------|

#create a list of template questions
q_list = [
    ["Question " + str(i+1), 
     "Right answer1", 
     "Wrong answer2", 
     "Wrong answer3", 
     "Wrong answer4"] 
     for i in range(5)
     ]

#start a round 
q = playquiz.quiz_round(q_list)
# question_selector(q_list)
#test the ask_question function
#ask_question(q[0], 1)