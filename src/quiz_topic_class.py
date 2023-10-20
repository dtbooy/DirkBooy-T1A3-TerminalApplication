"""
Module to hand file handling for Quiz Terminal Application
"""

import csv

class QuizTopic():
    """
    Class to hold and manipulate Quiz topic questions
    Methods to: 
    get question_list from file
    add questions to list & file
    remove questions to list & file
    save
    """
    def __init__(self, topic: tuple) -> None:
        # parameter topic will be tuple of (topic:str, filename:str) 
        self.topic = topic[0]
        self.filename = topic[1]
        self.question_list = self.get_questions(self.filename)
    
    def get_questions(self, filename):
        # doublecheck file exists
        # Read csv file
        # format output to question_list
        # return question_list
        pass

    def write_question(self):
        # 1 - get question 
        # 2 - get correct answer
        # 3,4,5 - get wrong answer
        # generate list [1,2,3,4,5]
        # present question, reiterate correct answer
        # ask for confirmation of adding - 
            # n - ask if try again?
        # append  question to self.question_list
        # append question to csv

    def delete_question(self):
        # display list of questions (numbered)
        # select question number to delete
        # display q & a for selected q
        # confirmation of deletion
        # use q index to delete line in csv 
        # (or detele q in q_list & overwrite file)

        
def get_available_topics():
    # Read files in quiz directory
    # Filter files by end in ".csv" and start with "quiz_"
    # Create name strings from file list
        # remove "quiz_"
        # remove ".csv" 
        # split into list via "_"
        # Capitalise first letters "str"[0].upper 
        # recombine wordlist into name
    # add to dictonary {"Topic" : filename}
    pass

def write_to_file(topic, question):
    # get topic 
    pass