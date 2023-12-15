import os
import keyboard
import time

# throws a dice and returns it's value
def throw_dice():
    pass

# (throw_dice internally)x6 ---> updates the values of the six crewmates (commander, tactical, medical...)
def get_crew(crew):
    # call throw_dice
    pass 

# Prints the game_over screen, maybe the high scores and asks the user if they want to play again
def game_over():
    print("""
         .d8888b.         d8888 888b     d888 8888888888 
        d88P  Y88b       d88888 8888b   d8888 888        
        888    888      d88P888 88888b.d88888 888        
        888            d88P 888 888Y88888P888 8888888    
        888  88888    d88P  888 888 Y888P 888 888        
        888    888   d88P   888 888  Y8P  888 888        
        Y88b  d88P  d8888888888 888   "   888 888        
         "Y8888P88 d88P     888 888       888 8888888888 
                                                 
                                                 
                                                 
         .d88888b.  888     888 8888888888 8888888b.     
        d88P" "Y88b 888     888 888        888   Y88b    
        888     888 888     888 888        888    888    
        888     888 Y88b   d88P 8888888    888   d88P    
        888     888  Y88b d88P  888        8888888P"     
        888     888   Y88o88P   888        888 T88b      
        Y88b. .d88P    Y888P    888        888  T88b     
         "Y88888P"      Y8P     8888888888 888   T88b 
          """)
    pass

# loop --> returns difficulty level, running = True (when enter is pressed)
def menu():
    pass

# Prints the whole board: graph for health, graph for shield, crew, active_threats,threat_dice... (Maybe wait for an input from the user to continue,
# this could be done at the end of the function itself or with another function user_confirmation() after each print_interface()
# There is an example of this second option after one of the print_interface from the running loop
def print_interface(health, shield, crew, threads, dice_number):
    pass

# Checks if there is at least one crewmate that can be gathered back, returns true or false
# A crewmate can't be gathered back if it is in the infirmary, it is a scanner or it is assigned to a Distracted threat
def can_be_gathered(crew):
    pass

# substracts a number of Don't Panic cards from the threats list (number in canva)
def check_dificulty(difficulty):
    pass

# Restarts the status of the crewmates that can be gathered back 
def gather_crew(crew):
    pass

# aux function that can be used to stop the execution of the program until the user decides
# we will use it if we decide that this approach is better than do it inside the print_interface
def user_confirmation():
    pass

# counts the number of scanners in the crew, then free three scanners by adding a threat and finally print (add_threat()-->free_scanner()-->print_interface())
def check_scanners(crew):
    # METER EN CHECK SCANNER!!
    # if n_scanners >= 3:
    #     add_threat(threats, active_threats)
    #     free_scaner(crew)
    #     
    #     print_interface(health, shield, crew, threats, dice_number)
    pass

# COMPLEX FUNCTION,behaviour described in its appearance in the running loop, I think it's better to understand if you see it there
def assign_crew(crew, active_threats):
    pass

# Takes a random threat from threats to active_threats
def add_threat(threats, active_threats):
    pass

# checks if enemies have been defeated or missions accomplished, returns the number of enemies defeated in this turn
def check_threats(active_threats):
    pass

def win_game():
    print("""
██╗    ██╗██╗███╗   ██╗
██║    ██║██║████╗  ██║
██║ █╗ ██║██║██╔██╗ ██║
██║███╗██║██║██║╚██╗██║
╚███╔███╔╝██║██║ ╚████║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝""")
    pass
# A throw_dice is called internally, then it loops over the active_functions and checks which ones get activated
# returns the dice_number to get it printed in the print_interface (this will happen at the start of the next turn)
def activate_threats(active_threats, crew):
    pass

# CREW_COMMANDER = 0
# CREW_TACTICAL = 1
# CREW_MEDICAL = 2
# CREW_SCIENCE = 3
# CREW_ENGINEERING = 4
# CREW_SCANNER = 5

def main():
    
    health = 8
    shield = 4  
    # dice_number = None
    crew = []
    threats = []
    active_threats = []
    n_external_defeated = 0 # the number of enemies defeated

    difficulty, running = menu()
    
    check_dificulty(difficulty)

    while running:
 
        print_interface(health, shield, crew, threats, dice_number)

        time.sleep(3) # in order for the user to see the board before loosing or restarting

        #Conditions to loose
        if health <= 0 or can_be_gathered(crew) == False: 
            win = False # determine the screen to be printed after ending the loop (see if-statement out of the loop)
            break   # get out of the while

        gather_crew(crew)

        get_crew(crew)

        print_interface(health, shield, crew, threats, dice_number)
        user_confirmation() # provisional

        check_scanners(crew)
        
        print_interface(health, shield, crew, threats, dice_number)

        # COMPLEX FUNCTION --> probably will start a loop until the user can't perform anymore actions or they decide they dont want to do anything else
        # will check if the active_threats can be solved with any current crewmate, if it is possible to get a crewmate out of the infirmary...
        # all the available options will be shown to the user when they select a crewmate and then they will be able to choose one, whathever they do will probably have consequences
        # (crewmate might me blocked when selecting one of it's possible actions for example)
        assign_crew(crew, active_threats)
        # |
        # |-> 
            # for every repetition inside the assign_crew we will use at least this:
            # n_external_defeated += check_threats(active_threats)
            # print_interface

        #Conditions to win
        if n_external_defeated >= 36 or len(threats) == 0:
            win = True  # determine the screen to be printed after ending the loop (see if-statement out of the loop)
            break   # get out of the while

        add_threat(threats, active_threats)

        print_interface(health, shield, crew, threats, dice_number)

        dice_number = activate_threats(active_threats, crew)

    running = False # I think this doesn't really do anything

    # Prints different screens depending on the result of the game
    # In both screens the user will be asked if they want to play again, if the answer is yes, the main method will be called
    if win:
        win_game()
    else:
        game_over()

if __name__ == "__main__":
    main()