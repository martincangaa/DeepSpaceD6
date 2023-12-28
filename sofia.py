import time
import keyboard

# loop --> returns difficulty level
def menu():
    """
    Shows the user the different levels that can be played inside the game and asks which of them is going to be played.

    Returns:
        int: Number corresponding to the level that the user wants to play (1=easy, 2=medium, 3=hard).
    """
    print('LEVELS OF DIFFICULTY:')
    print("1 - Easy: 1 Don't panic card is substracted from the threads")
    print("2 - Medium: 3 Don't panic cards are substracted from the threads")
    print("3 - Hard: 6 Don't panic cards are substracted from the threads")
    time.sleep(4)
    difficulty = int(input('Which level of difficulty do you want to play (1=easy, 2=medium, 3=hard)? '))
    while not (difficulty == 1 or difficulty == 2 or difficulty == 3):
        print('Not valid level')
        time.sleep(2)
        difficulty = int(input('Which level of difficulty do you want to play (1=easy, 2=medium, 3=hard)? '))
    
    return difficulty


# Checks if there is at least one crewmate that can be gathered back, returns true or false
# A crewmate can't be gathered back if it is in the infirmary, it is a scanner or it is assigned to a Distracted threat
def can_be_gathered(crew):
    for crewmate in crew:
        if crewmate['blocked'] == False and crewmate['infirmary'] == False and crewmate['crew_type'] != CREW_SCANNER:
            return True
    return False

# aux function that can be used to stop the execution of the program until the user decides
# we will use it if we decide that this approach is better than do it inside the print_interface
def user_confirmation():
    keyboard.wait("enter")

def win_game():
    print("""
██╗    ██╗██╗███╗   ██╗
██║    ██║██║████╗  ██║
██║ █╗ ██║██║██╔██╗ ██║
██║███╗██║██║██║╚██╗██║
╚███╔███╔╝██║██║ ╚████║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝""")
    time.sleep(2)
    play_again = input('Do you want to play again? (Input "Yes" to play again, anything else to finish the game): ')

    if play_again == 'Yes':
        main()