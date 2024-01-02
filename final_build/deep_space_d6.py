import os
import keyboard
import time
import file_mgmt as fm
import game_logic as gl
import input_output_user as io

CREW_COMMANDER = 0
CREW_TACTICAL = 1
CREW_MEDICAL = 2
CREW_SCIENCE = 3
CREW_ENGINEERING = 4
CREW_SCANNER = 5
EMPTY = 6

def main():
    
    health = 8
    shield = 4  
    # dice_number = None
    crew = []
    threats = []
    active_threats = []
    n_external_defeated = 0 # the number of enemies defeated

    menu()
    
    check_dificulty(difficulty)

    while True:

        io.print_interface(health, shield, active_threats, crew)

        time.sleep(3) # in order for the user to see the board before loosing or restarting

        #Conditions to loose
        if health <= 0 or gl.can_be_gathered(crew) == False: 
            win = False # determine the screen to be printed after ending the loop (see if-statement out of the loop)
            break   # get out of the while

        crew = gl.get_crew(crew)

        iu.print_interface(health, shield, active_threats, crew)
        user_confirmation() # provisional

        gl.check_scanners(crew)
        
        io.print_interface(health, shield, active_threats, crew)

        # COMPLEX FUNCTION --> probably will start a loop until the user can't perform anymore actions or they decide they dont want to do anything else
        # will check if the active_threats can be solved with any current crewmate, if it is possible to get a crewmate out of the infirmary...
        # all the available options will be shown to the user when they select a crewmate and then they will be able to choose one, whathever they do will probably have consequences
        # (crewmate might me blocked when selecting one of it's possible actions for example)
        
        crew, active_threats, health, shield = io.assign_crew(crew, active_threats, health, shield)

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

        io.print_interface(health, shield, active_threats, crew, user_confirmation=True)

        gl.activate_threats(active_threats, crew)

        dice_number = activate_threat(active_threats, crew)

    # Prints different screens depending on the result of the game
    # In both screens the user will be asked if they want to play again, if the answer is yes, the main method will be called
    if win:
        io.win_game()
    else:
        io.game_over()

if __name__ == "__main__":
    main()
