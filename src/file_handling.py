"""
Module to hand file handling for Quiz Terminal Application
"""
# ---------------------------------------------------------------------|
# playquiz needed for clear_screen(), ask_question().
import playquiz
# csv module used to read / write quiz question files.
import csv
# os used to get directory list.
import os
# pyinputplus module used to get valid user inputs.
import pyinputplus as pyip
# getpass used to hide user input when asked to press enter to continue.
import getpass


def get_topics_from_directory() -> list:
    # Check if directory exists
    if not os.path.exists("./quiz_data"):
        # If directory doesn't exist, create directory & raise error
        os.mkdir("./quiz_data")
        raise FileNotFoundError(
            "Could not find quiz directory! Creating new directory: "
            f"{os.getcwd()}/quiz_data/")

    # Read files in quiz directory.
    dir_list = os.listdir("./quiz_data")
    quiz_list = []
    for file in dir_list:
        # Filter files by end in ".csv" and start with "quiz_".
        if file.endswith(".csv") and file.startswith("quiz_"):
            # Format as title & add to list.
            quiz_list.append(str(file[5:-4]).replace("_", " ").title())
    # Raise an error if no quizzes are found.
    if quiz_list == []:
        raise FileNotFoundError("No quiz files found.")
    # Sort quiz_list and return
    quiz_list.sort()
    return quiz_list


def get_question_list_from_file(quiz_title: str) -> list:
    filename = (
        "./quiz_data/quiz_" +
        quiz_title.lower().replace(" ", "_") +
        ".csv")
    question_list = []
    error_count = 0
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        reader.__next__()  # Skip first row (column names).
        for row in reader:
            # Ensure there are 5 items in row: 1 Question + 4 answers
            if len(row) == 5:
                question_list.append(row)
            else:
                error_count += 1
    if error_count > 0:
        print(
            f"Warning - {error_count} question/s were in incorrect"
            " format and removed from quiz")
        getpass.getpass("Press enter to continue...")
    return question_list


def get_new_question_from_user_input() -> list:
    """
    Prompts user through writing a question.
    Output is a question-answers list in the format [Q,CA,WA,WA,WA]
    """
    while True:
        # Get questions and answers from user.
        question = [pyip.inputStr("Type your question:\n>")]
        question.append(pyip.inputStr("Type the correct answer:\n>"))
        question.append(pyip.inputStr("Type a wrong answer:\n>"))
        question.append(pyip.inputStr("Type another wrong answer:\n>"))
        question.append(pyip.inputStr("Type the last wrong answer:\n>"))

        # Display question to user.
        playquiz.print_title("Question Preview")
        num = playquiz.ask_question(question, 0)
        print(
            f"\nThe correct answer is: \n"
            f"{chr(ord('@') + num)}: {question[1]}")
        # Confirm correct.
        if pyip.inputYesNo(
                "\nDo you want to add this question? [Y/N]: ") == "yes":
            print("Question added!\n")
            return question
        else:
            print("Question discarded!\n")
            # Repeat while loop if user wants to try again, otherwise
            # return to menu
            if pyip.inputYesNo(
                    "Would you like to try again? [Y/N] ") == "no":
                raise ValueError("Add question process cancelled")


def write_new_question_to_file(topic: str) -> None:
    """Gets new question, and appends it to quiz file"""
    # Get question from user
    try:
        question = get_new_question_from_user_input()
    except ValueError as err_msg:
        print(f"Question creation failed: {err_msg}")
    else:
        # Convert topic to filename.
        filename = (
            "./quiz_data/quiz_" +
            topic.lower().replace(" ", "_") +
            ".csv")
        # Write question to file
        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([question])
        playquiz.print_title("Success! Question saved!")
    finally:
        getpass.getpass("Press Enter to return to menu...")


def delete_question(topic: str) -> None:
    """Deletes question from quiz question file"""
    # Get list of questions in topic
    question_list = get_question_list_from_file(topic)
    # print out all questions in numbered list
    print(f"Questions in {topic}:")
    for i, question in enumerate(question_list):
        print(f"{i+1}. {question[0]}")

    # select question number to delete
    del_q_index = pyip.inputInt(
        "Select question number to delete: ",
        min=1, max=len(question_list)) - 1
    # Display Q&As for selected question
    playquiz.print_title("Delete Question")
    playquiz.ask_question(question_list[del_q_index], del_q_index)
    # confirmation of deletion
    confirm = pyip.inputYesNo(
        "\nIs this the question you want to delete? [Y/N]")
    if confirm == "yes":
        # remove question from question_list
        question_list.remove(question_list[del_q_index])
        # write question_list to file
        write_full_quiz_to_file(topic, question_list)
        print("Question deleted successfully")
    else:
        print("Cancelled deletion!")
    # If no questions in quiz, delete quiz file
    if question_list == []:
        print("That was the last question in the quiz. Deleting quiz file.")
        delete_quiz_file(None, topic)
    getpass.getpass("Press Enter to continue...")


def new_quiz_name(topic_list: list) -> str:
    """Gets a valid new quiz name from user input"""
    while True:
        print(
            "Note: Quiz title must be unique, and cannot contain "
            "special characters")
        topic = input("Please enter quiz title: ")
        if topic == "":
            # Ensure user has entered a name
            print("Quiz title cannot be blank.")
        elif topic.replace(" ", "").isalnum() is False:
            # Ensure filename has no special character.
            print("Quiz title cannot contain special characters.")
        elif topic.title() in topic_list:
            # Check if filename exists
            print("Quiz title cannot be the same as existing quiz.")
        else:
            return topic


def new_quiz_topic(topic_list: str) -> None:
    """Guides user through process of creating new quiz"""
    # Print title
    playquiz.print_title("New Quiz")
    # get name of new quiz
    topic = new_quiz_name(topic_list)
    question_list = []
    next_question = True
    while next_question is True:
        try:
            # Get question from user
            new_question = get_new_question_from_user_input()
        except ValueError as err_msg:
            print(f"Question creation failed: {err_msg}")
        else:
            # If write_question was succesful append to list.
            question_list.append(new_question)
        finally:
            # If user is finished set while loop flag to false.
            if pyip.inputYesNo(
                    "Would you like to enter another question?") == "no":
                next_question = False

    # If user hasn't entered anything return to menu loop
    if question_list == []:
        playquiz.clear_screen()
        print("New quiz creation cancelled: No questions added")
    else:
        # Save quizz to file
        write_full_quiz_to_file(topic, question_list)
        playquiz.print_title("Success! New quiz was created")
    getpass.getpass("\nPress Enter to continue...")


def write_full_quiz_to_file(topic: str, question_list: list) -> None:
    """Takes quiz name and question list and writes them to a new quiz file"""
    # Convert topic to filename
    filename = ("./quiz_data/quiz_" +
                topic.lower().replace(" ", "_") +
                ".csv")
    # Open file for writing
    with open(filename, 'w') as f:
        # Create a CSV writer object
        writer = csv.writer(f)
        # Write file headings
        writer.writerow(
            ['Question',
                'Correct Answer',
                "Wrong Answer 1",
                "Wrong Answer 2",
                "Wrong Answer 3"])
        writer.writerows(question_list)


def delete_quiz_file(topic: str) -> None:
    """Deletes file from directory"""
    # Convert topic to filename
    filename = (
            "./quiz_data/quiz_" +
            topic.lower().replace(" ", "_") +
            ".csv")
    # Delete file
    os.remove(filename)
