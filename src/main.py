#--------------------------------------------------------------------------|
"""
Main Navigation Loop for Terminal Quiz Application
"""
import playquiz # quiz module playquiz.py
import file_handling # handles read/write to file
import pyinputplus as pyip
import getpass # Hides user input in terminal 
import os

def select_topic(topic_list: list) -> int:
    for i, topic in enumerate(topic_list):
        print(f"{i+1}. {topic}")    
    # return user choice as # index in topic_list
    return pyip.inputInt("\nSelect topic number:", min=1, max=len(topic_list)) -1
    
def menu_select(menu_items: list) -> int:
    """Get valid user selection from menu. Return menu list index"""
    while True:
        # Print menu (numbered)
        for i, option in enumerate(menu_items):
            print(f"{i+1}. {option}")        
        # Get user selection
        selection = input("\nEnter selection: ").lower()
        # Check for valid user selection. Valid selections are:
            # Full menu name: str
            # First word: str
            # First letter: str
            # option number: int(str)
            # Validity check is CAPS insensitive.
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
    
def main() -> None:
    """Main navigation loop"""
    playquiz.clear_screen()
    #Add static menu items to lists
    top_level_menu = ["Play", "Edit Mode", "Help", "Credits", "Quit"]
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
                    "Premade quiz files can be found at "
                    "https://github.com/dtbooy/DirkBooy-T1A3-TerminalApplication")
                getpass.getpass("Press Enter to Exit...")
                exit()

        playquiz.print_title("Lets Play Terminal Quiz!!") 
        choice = menu_select(top_level_menu)
        match choice:
            case 0:
                play(topic_list)
            case 1:
                edit(topic_list)
            case 2:
                print("Help")
                help_menu()
                 #  ---------------------------------------------------------->DEBUG
            case 3:
                credits()
            case 4:
                playquiz.print_title("Goodbye! Thanks for playing")
                break

def play(topic_list):
    # Quiz topic selection
    playquiz.print_title("Select a quiz")
    print(f"Please select a Quiz topic:")
    topic_index = select_topic(topic_list)
    # send list to playquiz.quiz_round 
    playquiz.quiz_round(topic_list[topic_index])

def edit(topic_list):
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
                # launch question writed function
                playquiz.print_title("New Question")
                file_handling.write_new_question_to_file(topic_list[topic_index])
            else:
                #launch delete question function
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
                f"Are you sure you want to delete quiz: {topic}? [Y/N] :") == "yes":
                    # Delete quiz
                    file_handling.delete_quiz_file(topic)
            else:
                getpass.getpass("Cancelled deletion of quiz. Press enter to return to menu.")

def help_menu():
    help_menu_items = [
        "How to Play", 
        "How to Edit", 
        "Get more quizes", 
        "Return to menu"]
    playquiz.print_title("Help")
    print("what do you need help with?")
    choice = menu_select(help_menu_items)
    match choice:
        case 0:
            # How to play
            help(help_how_to_play)
        case 1:
            #How to edit
            pass
        case 2:
            # get more quizes - link to website?
            pass
        case _:
            #Do nothing - return to menu loop
            pass

def credits():
    playquiz.print_title("Credits")
    getpass.getpass("Press Enter to continue...")
    

def help_how_to_play():
    """testing to see if this is called in the help function"""

try:
    main()
except KeyboardInterrupt:
    playquiz.print_title("Goodbye! Thanks for playing")

#----------------------------------------------------------------------|
#TESTING
# select_topic(file_handling.get_available_topics_from_dir())

# menu_select(["Play", "Edit Quiz", "Help", "Credits", "Quit"])
1