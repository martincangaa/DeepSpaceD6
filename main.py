import os
import keyboard
import time

def user_input_menu():
    pass

def throw_dice():
    pass

def get_crew():
    # call throw_dice
    pass 

def get_thread():
    # call throw_dice call get_spawn_power
    pass

def game_over():
    pass

def menu():
    pass

def print_interface(health, shield, crew, threads, dice_number):
    pass

def can_be_gathered():
    pass

def check_dificulty():
    pass

def gather_crew():
    pass

def user_confirmation():
    pass

def check_scanners():
    pass

def assign_crew():
    pass

def add_threat():
    pass

def check_threats():
    pass

def activate_threats():
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
    n_external_defeated = 0

    difficulty, running = menu() #loop --> returns difficulty level, prints high scores
    
    check_dificulty(difficulty)

    while running:

        print_interface(health, shield, crew, threats, dice_number)
        time.sleep(3)

        if health <= 0 or can_be_gathered(crew) == False:
            win = False
            break

        gather_crew(crew)

        get_crew(crew)

        print_interface(health, shield, crew, threats, dice_number)
        user_confirmation()

        check_scanners(crew)
        
        # METER EN CHECK SCANNER!!
        # if n_scanners >= 3:
        #     add_threat(threats, active_threats)
        #     free_scaner(crew)
        #     
        #     print_interface(health, shield, crew, threats, dice_number)
        
        print_interface(health, shield, crew, threats, dice_number)

        assign_crew(crew)

        print_interface(health, shield, crew, threats, dice_number)

        n_external_defeated += check_threats(active_threats)

        if n_external_defeated >= 36 or len(threats) == 0:
            win = True
            break

        add_threat(threats, active_threats)

        print_interface(health, shield, crew, threats, dice_number)

        dice_number = activate_threats(active_threats, crew)

    running = False

    if win:
        win()
    else:
        game_over()

    #set_spawn_power(2)
    #
    #running = True
    #while running:
    #    
    #    if health <= 0: # kills the game loop if you die
    #        running  = False
    #
    #    print_interface(health, shield, crew, threads, dice_number) # prints the ship, health, cards, crew
    #    crew = get_crew()
    #
    #    threads, dice_number = get_thread()

if __name__ == "__main__":
    main()