#----------------------------------------------------------------------|
"""
Main Loop for Terminal application
"""
import playquiz # quiz module playquiz.py
import file_handling # handles read/write to file
import pyinputplus as pyip

def menu_select(menu_items: list) -> int:
    """Get valid user selection from menu. Return menu list index"""
    while True:
        # Print menu (numbered)
        for i, option in enumerate(menu_items):
            print(f"{i+1}. {option}")
        
        # Get user input
        selection = input("\nEnter selection: ").lower()

        try:
            # Check if entered a valid integer, return menu index
            if int(selection[0]) in range(1, len(menu_items) + 1):
                return int(selection) - 1
            
        # Catch exception if string value entered, check for valid strings.
        # Valid strings are full menu name, 1st word or 1st letter.
        # Validity check is CAPS insensitive.  
        except ValueError:
            valid_opt = [
                list(x[0].lower() for x in menu_items),
                list(x.lower().split(" ")[0] for x in menu_items),
                list(x.lower() for x in menu_items)]
            for option in (valid_opt):
                # print(option) #- ---end                        ---------------------->DEBUG
                if selection in option:
                    return option.index(selection)
        
        #If we are still in the loop a valid answer was not received. Ask again.
        print(
            f"Invalid selection: {selection}.\n"
            "Please enter a menu number or name.")
    
def main():
    """Main navigation loop"""
    #Add static menu items to lists
    top_level_menu = ["Play", "Edit Mode", "Help", "Credits", "Quit"]
    edit_menu = ["Edit Existing Quiz", "Create New Quiz"]
    help_menu = ["How to Play", "How to Edit"]
    topic_list = file_handling.get_available_topics_from_dir()
    while True:
        playquiz.print_title("Welcome message") # Update to something fancy - maybe add a Title decorator?----> DEBUG
        choice = menu_select(top_level_menu)
        match choice:
            case 0:
                print("Play")
                play(topic_list)
            case 1:
                print("Edit")
                playquiz.print_title("Edit Options")
                choice = menu_select(edit_menu)
                #new create new quiz
                if choice == 1:
                    file_handling().new_quiz_topic(topic_list)
                #edit existing quiz
                else:
                    edit(topic_list)
                    
                 #  ---------------------------------------------------------->DEBUG
            case 2:
                print("Help")
                choice = menu_select(help_menu)
                break #  ---------------------------------------------------------->DEBUG
            case 3:
                print("Credits")
                break #  ---------------------------------------------------------->DEBUG
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
    edit_quiz_menu = ["Add Question", "Delete Question"]
    # Select quiz to edit    
    playquiz.print_title("Select quiz to edit")
    topic_index = select_topic(topic_list)

    playquiz.print_title("Add or Delete a question?")
    if menu_select(edit_quiz_menu) == 0:
        # launch question writed function
        file_handling.write_new_question_to_file(topic_list[topic_index])
    else:
        #launch delete question function
        file_handling.delete_question(topic_list[topic_index])

def help():
    pass

def credits():
    pass

def select_topic(topic_list: list) -> int:
    for i, topic in enumerate(topic_list):
        print(f"{i+1}. {topic}")    
    # return user choice as # index in topic_list
    return pyip.inputInt("\nSelect topic number:",min=1, max=len(topic_list)) -1
    

    
main()
#----------------------------------------------------------------------|
#TESTING
# select_topic(file_handling.get_available_topics_from_dir())

# menu_select(["Play", "Edit Quiz", "Help", "Credits", "Quit"])
