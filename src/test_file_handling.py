import file_handling
import pytest


def test_read_write_file():
    """
    This test will:
    1. create a test quiz,
    2. write it to a file,
    3. check that the newly generated quiz appears in the topics list
    4. read the quiz from file back into the program and compare it
       to the original generated quiz.
    5. delete the generated quiz file
    6. confirm all changes have beeen reverted

    It will test the following functions in file_handling.py:
    1. write_full_quiz_to_file(topic: str, question_list: list):
    2. get_topics_from_directory()
    3. get_question_list_from_file(quiz_title: str)
    4. delete_quiz_file(topic: str)
    """

    # Generate a list of template questions
    gen_q_list = [[
        "Question " + str(i+1),
        "Right answer1",
        "Wrong answer2",
        "Wrong answer3",
        "Wrong answer4"]
        for i in range(50)
        ]
    gen_topic = "Generated Questions Topic"
    # Get topic list from dir
    original_topic_list = file_handling.get_topics_from_directory()
    # Make sure gen_topic is not an existing quiz
    assert gen_topic not in original_topic_list
    # Write generated quiz to file
    file_handling.write_full_quiz_to_file(gen_topic, gen_q_list)
    # Get updated topic list from directory
    new_topic_list = file_handling.get_topics_from_directory()
    # TEST: gen_topic should now be in topic list
    assert gen_topic in new_topic_list
    # Read generated quiz file
    file_q_list = file_handling.get_question_list_from_file(gen_topic)
    # TEST: list read from file equals the original generated list
    assert file_q_list == gen_q_list
    # Delete temporary test file
    file_handling.delete_quiz_file(gen_topic)
    # Get final topic list from directory
    final_topic_list = file_handling.get_topics_from_directory()
    # TEST: confirm quiz has been deleted successfully
    assert final_topic_list == original_topic_list


def test_edit_file(monkeypatch):
    """
    This test will:
    1. Get the list of quiz topics
    2. Write a test question to the first quiz file
    3. Load questions from quiz file
    4. Confirm test question was written to file
    5. Delete test question from file
    6. Confirm deletion of test question form file

    It will test the following functions in file_handling.py:
    1. get_topics_from_dir()
    2. write_new_question_to_file(topic)
    3. get_question_list_from_file(quiz_title)
    4. delete_question(topic)
    """
    # Get quiz topics
    topic_list = file_handling.get_topics_from_directory()
    # Set test question
    gen_question = [
        "Generated Test Question",
        "GTQ Right answer1",
        "GTQ Wrong answer2",
        "GTQ Wrong answer3",
        "GQT Wrong answer4"]
    # Set monkey patch to stop running clear_screen during test
    monkeypatch.setattr(
        "file_handling.playquiz.clear_screen", lambda: print("clear screen"))

    # Set monkey patch on get_new_question_from_user_input() to
    # return gen_question
    monkeypatch.setattr(
        file_handling, "get_new_question_from_user_input",
        lambda: gen_question)

    # TEST - Make sure gen_question isn't already in question list
    original_question_list = (
        file_handling.get_question_list_from_file(topic_list[0]))
    assert gen_question != original_question_list[-1]

    # write question to file in first quiz file in topic list
    file_handling.write_new_question_to_file(topic_list[0])
    # get list of question in first quiz in topic list from file
    question_list = file_handling.get_question_list_from_file(topic_list[0])
    # TEST - question has been written to file and loaded from file
    assert gen_question == question_list[-1]

    # Set monkey patch pyip.inputInt() to len(question list)
    monkeypatch.setattr(
        "pyinputplus.inputInt", ret_int)
    # Set monkey patch pyip.inputYesNo() to "yes"
    monkeypatch.setattr(
        file_handling.pyip, "inputYesNo", ret_yes)
    # Delete test question from file
    file_handling.delete_question(topic_list[0])

    # Confirm question has been deleted
    final_question_list = (
        file_handling.get_question_list_from_file(topic_list[0]))
    assert gen_question != final_question_list[-1]

    # Confirm changes have been reverted
    assert original_question_list == final_question_list


# Function to replace user input with index of last question
def ret_int(a=None, min=None, max=None, b=None):
    topic_list = file_handling.get_topics_from_directory()
    question_list = file_handling.get_question_list_from_file(topic_list[0])
    return len(question_list)


# Function to replace user input with "yes"
def ret_yes(input=None):
    return "yes"
