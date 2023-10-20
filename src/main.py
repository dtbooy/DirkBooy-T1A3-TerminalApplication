#----------------------------------------------------------------------|
"""
Main Loop for Terminal application
"""
import playquiz # quiz module playquiz.py

def menu_select(menu_items: list) -> int:
    """Get valid user selection from menu. Return menu list index"""
    while True:
        # Print menu (numbered)
        for i, option in enumerate(menu_items):
            print(f"{i+1}. {option}")
        
        # Get user input
        selection = input("Enter selection: ").lower()

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
    top_level_menu = ["Play", "Edit Quiz", "Help", "Credits", "Quit"]
    edit_menu = ["Edit Quiz", "New Quiz Topic"]
    help_menu = ["How to Play", "How to Edit"]

    while True:
        print("Welcome message") # Update to something fancy - maybe add a Title decorator?----> DEBUG
        choice = menu_select(top_level_menu)
        match choice:
            case 0:
                print("Play")
                break #  ---------------------------------------------------------->DEBUG
            case 1:
                print("Edit")
                choice = menu_select(edit_menu)
                break #  ---------------------------------------------------------->DEBUG
            case 2:
                print("Help")
                choice = menu_select(help_menu)
                break #  ---------------------------------------------------------->DEBUG
            case 3:
                print("Credits")
                break #  ---------------------------------------------------------->DEBUG
            case 4:
                print("Goodbye! Thanks for playing")
                break
        
main()
#----------------------------------------------------------------------|
#TESTING


# menu_select(["Play", "Edit Quiz", "Help", "Credits", "Quit"])
