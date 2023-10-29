"""
Main Navigation Loop for Terminal Quiz Application
"""
# Import playquiz and filehandling to call functions
import playquiz  # Handles the quiz functions
import file_handling  # Handles read/write to file
# pyinputplus used for simple user input validation
import pyinputplus as pyip
# getpass used to hides user input in terminal
import getpass
# os used to get directory path
import os
# json used to read help text from file
import json


def menu_select(menu_items: list) -> int:
    """Gets valid user selection from menu. Return menu list index"""
    while True:
        # Print menu (numbered)
        for i, option in enumerate(menu_items):
            print(f"{i+1}. {option}")
        # Get user selection
        selection = input("\nEnter selection: ").lower()
        # Check for valid user selection. Valid selections are:
        #   Full menu name: str
        #   First word: str
        #   First letter: str
        #   option number: int(str)
        #   Validity check is CAPS insensitive.
        valid_opt = [
            list(x[0].lower() for x in menu_items),
            list(x.lower().split(" ")[0] for x in menu_items),
            list(x.lower() for x in menu_items),
            list(map(str, range(1, len(menu_items) + 1)))]
        for option in (valid_opt):
            if selection in option:
                return option.index(selection)
        # If still in the while loop a valid answer was not received.

        playquiz.clear_screen()
        print(
            f"Invalid selection: {selection}.\n"
            "Please enter a menu number or name.\n")


def main_menu() -> None:
    """Main navigation loop"""
    playquiz.clear_screen()
    # Add static menu items to lists
    top_level_menu = ["Play", "Edit Mode", "Help", "Quit"]
    while True:
        # Get list of topics (refreshes each menu reload)
        try:
            topic_list = file_handling.get_topics_from_directory()
        # Catch error if there are no quiz files available
        except FileNotFoundError as err_msg:
            print(f"Error: {err_msg}\n")
            print("No quiz files found, create a new quiz now to play!")
            if pyip.inputYesNo(
                    "Would you like to create a quiz now?") == "yes":
                # pass empty topic list to new_quiz_topic()
                file_handling.new_quiz_topic([])
            else:
                playquiz.print_title("Good-Bye!")
                print(
                    "No quiz files found, please copy a quiz file to "
                    f"{os.getcwd()}/quiz_data/ \n"
                    "Premade quiz files can be found at https://github"
                    ".com/dtbooy/DirkBooy-T1A3-TerminalApplication")
                getpass.getpass("Press Enter to Exit...")
                exit()
        # Display Menu
        playquiz.print_title("Lets Play Terminal Quiz!!")
        choice = menu_select(top_level_menu)
        match choice:
            case 0:
                play_menu(topic_list)
            case 1:
                edit_menu(topic_list)
            case 2:
                print("Help")
                help_menu()
            case 3:
                playquiz.print_title("Goodbye! Thanks for playing")
                break


def select_topic(topic_list: list) -> int:
    for i, topic in enumerate(topic_list):
        print(f"{i+1}. {topic}")
    # return user choice as # index in topic_list
    return pyip.inputInt(
        "\nSelect topic number:",
        min=1, max=len(topic_list)) - 1


def play_menu(topic_list) -> None:
    # Quiz topic selection
    playquiz.print_title("Select a quiz")
    print(f"Please select a Quiz topic:")
    topic_index = select_topic(topic_list)
    # send list to playquiz.quiz_round
    playquiz.quiz_round(topic_list[topic_index])


def edit_menu(topic_list) -> None:
    edit_menu_1 = ["Edit Existing Quiz", "Create New Quiz", "Delete Quiz"]
    edit_menu_2 = ["Add Question", "Delete Question"]
    playquiz.print_title("Edit Options")
    choice = menu_select(edit_menu_1)
    # Create new quiz
    match choice:
        case 0:
            # Edit existing quiz
            # Select quiz to edit
            playquiz.print_title("Edit Existing Quiz")
            print("Select quiz to edit:")
            topic_index = select_topic(topic_list)
            # Add or Delete Question Menu
            playquiz.print_title("Add or Delete a question?")
            if menu_select(edit_menu_2) == 0:
                # Launch write question function
                playquiz.print_title("New Question")
                file_handling.write_new_question_to_file(
                    topic_list[topic_index])
            else:
                # Launch delete question function
                playquiz.print_title("Delete Question")
                file_handling.delete_question(topic_list[topic_index])
        case 1:
            # New Quiz
            file_handling.new_quiz_topic(topic_list)
        case 2:
            # Delete Quiz
            playquiz.print_title("Delete quiz")
            # Select quiz to delete
            print("Select quiz to delete")
            topic = topic_list[select_topic(topic_list)]
            # Confirm deletion
            print("\nWARNING THIS ACTION CANNOT BE UNDONE!\n")
            if pyip.inputYesNo(
                    f"Are you sure you want to delete quiz: {topic}? "
                    "[Y/N] :") == "yes":
                # Delete quiz
                file_handling.delete_quiz_file(topic)
            else:
                getpass.getpass(
                    "Cancelled deletion of quiz. Press enter to return to"
                    " menu.")


def help_menu() -> None:
    help_menu_items = [
        "How to Play",
        "Add a question to a quiz",
        "Delete a question to a quiz",
        "Create a new quiz",
        "Delete a quiz",
        "Return to menu"]
    # Load help topics from file to dictionary
    with open('help_files.json', 'r') as f:
        # Read help_dictionary from file
        help_dictionary = json.load(f)
    while True:
        playquiz.print_title("Help")
        print("What do you need help with?")
        choice = menu_select(help_menu_items)
        match choice:
            case 0:
                # How to play
                playquiz.print_title("How to quiz!")
                print(help_dictionary["Play"])
                getpass.getpass("Press Enter to continue...")
            case 1:
                # Add a question
                playquiz.print_title("Add questions to a quiz")
                print(help_dictionary["Add Question"])
                getpass.getpass("Press Enter to continue...")
            case 2:
                # Delete a question
                playquiz.print_title("Delete a question from a quiz")
                print(help_dictionary["Delete Question"])
                getpass.getpass("Press Enter to continue...")
            case 3:
                # Create New Quiz
                playquiz.print_title("Make your own quiz")
                print(help_dictionary["New Quiz"])
                getpass.getpass("Press Enter to continue...")
            case 4:
                # Delete Quiz
                playquiz.print_title("Delete a quiz")
                print(help_dictionary["Delete Quiz"])
                getpass.getpass("Press Enter to continue...")
            case 5:
                # Return to menu loop
                break


# Initiate Main Menu
if __name__ == "__main__":
    try:
        main_menu()
        # Catch Keyboard Interupts
    except KeyboardInterrupt:
        playquiz.print_title("Goodbye! Thanks for playing")
