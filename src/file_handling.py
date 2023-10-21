#----------------------------------------------------------------------|
"""
Module to hand file handling for Quiz Terminal Application
"""
#playquiz needed for clear_screen(), ask_question()
import playquiz
# csv module used to read / write quiz question files
import csv
# os used to get directory list
import os
# pyinputplus module used to
import pyinputplus as pyip

def get_available_topics_from_dir() -> list:
    # Read files in quiz directory
    dir_list = os.listdir("./quiz_data")
    quiz_list = []
    for file in dir_list:
        # Filter files by end in ".csv" and start with "quiz_"
        if file.endswith(".csv") and file.startswith("quiz_"):
            #Format as title & add to list
            quiz_list.append(str(file[5:-4]).replace("_", " ").title())

    print(quiz_list)
    return quiz_list

def get_question_list_from_file(quiz_title: str) -> list:
    filename = (
        "./quiz_data/quiz_" + 
        quiz_title.lower().replace(" ", "_") + 
        ".csv")
    question_list = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        reader.__next__() # Skip the first row (the column names)
        for row in reader:
            question_list.append(row)
    return question_list

def get_user_input_new_question() -> list:
    """
    Prompts user through writing a question. 
    Output is a question-answers list in the format [Q,CA,WA,WA,WA] 
    """
    while True:
        #get questions and answers from user 
        question = [pyip.inputStr("Type your question:\n>")]
        question.append(pyip.inputStr("Type the correct answer:\n>"))
        question.append(pyip.inputStr("Type a wrong answer:\n>"))
        question.append(pyip.inputStr("Type another wrong answer:\n>"))
        question.append(pyip.inputStr("Type the last wrong answer:\n>"))
        
        playquiz.clear_screen()

        # display question to user
        num = playquiz.ask_question(question, 1)
        print(
            f"\nThe correct answer is: \n"
            f"{chr(ord('@') + num)}: {question[1]}")
        # confirm correct
        if pyip.inputYesNo("\n is this correct?") == "yes":
            print("Question added!\n")
            return question
        else:
            print("Question discarded!\n")
            if pyip.inputYesNo(
                "\n would you like to try again?") == "no":
                return

    
def write_new_question_to_file(topic: str) -> None:
    """Gets new question, and appends it to topic file"""
    # Get question from user
    question = get_user_input_new_question()
    # Convert topic to filename 
    filename = (
        "./quiz_data/quiz_" + 
        topic.lower().replace(" ", "_") + 
        ".csv")
    # Write question to file
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f) 
        writer.writerows([question])
    return

def delete_question(topic: str) -> None:
    # display list of questions (numbered)
    question_list = get_question_list_from_file(topic)

    # print out all questions in numbered list
    print(f"Questions in {topic}:")
    for i, question in enumerate(question_list):
        print(f"{i+1}. {question}[0]")

    # select question number to delete
    del_q_index = pyip.inputInt("Select question number to delete :",min=1, max=len(question_list)) -1
    # display q & a for selected q
    playquiz.clear_screen()
    playquiz.ask_question(question_list[del_q_index], del_q_index)    
    # confirmation of deletion
    if pyip.inputYesNo("Is this the question you want to delete? [Y/N]") ==  "yes":
        # use q index to delete line in csv 
        ########################CODE GO HERE ######################### ---------------->DEBUG
        # (or detele q in q_list & overwrite file)
        print("Question deleted successfully")
    else:
        print("Cancelled deletion!")
    
        


def new_quiz_name(topic_list: str) ->str:
    # Need to compare against existing quiz list too consider making function ------> DEBUG
    while True:
        topic = input("Please enter quiz title: ")
        if topic == None:
            print("Quiz title cannot be blank.")
        elif topic.replace(" ", "").isalnum() == False:
            print("Quiz title cannot contain special characters.")
        elif topic in topic_list:
            print("Quiz title cannot be the same as existing quiz.")
        else:
            return topic
          

def new_quiz_topic(topic_list) -> None:
    # get name of new quiz
    topic = new_quiz_name(topic_list)
    question_list = []
    next_question = True
    while next_question == True:
        # Get question from user
        success = get_user_input_new_question()
        # If write_question was succesful append to list
        if success != None:
            question_list.append(success)
        # If user is finished set while loop flag to false
        if pyip.inputYesNo("Would you like to Enter another question?") == "no":
            next_question = False
    # If user hasn't entered anything return to menu loop
    if question_list == []:
        return
    # Convert topic to filename 
    filename = "./quiz_data/quiz_" + topic.lower().replace(" ", "_") + ".csv"
    with open(filename, 'w') as f: # Open file for writing
        writer = csv.writer(f) # Create a CSV writer object
        # Write file headings
        writer.writerow(
            ['Question',
                'Correct Answer', 
                "Wrong Answer 1",
                "Wrong Answer 2",
                "Wrong Answer 3"]) # Write the header row first
        writer.writerows(question_list)
        playquiz.clear_screen()
        print("Success! New quizz was created")
    return


#   Tests 

# q_list = [
#     ["Question " + str(i+1), 
#      "Right answer1", 
#      "Wrong answer2", 
#      "Wrong answer3", 
#      "Wrong answer4"] 
#      for i in range(5)
#      ]

# new_question("5 test Questions")
# new_quiz_topic(["test quiz 1"])
print(get_question_list_from_file(get_available_topics_from_dir()[0])[0])
#write_to_file(q_list, "10000 Test Questions")
delete_question("5 test questions")