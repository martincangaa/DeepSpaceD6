    
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

def print_interface(int health, int shield, int crew[], int threads[], dice_number):
    pass

def main():
    
    CREW_COMMANDER = 0
    CREW_TACTICAL = 1
    CREW_MEDICAL = 2
    CREW_SCIENCE = 3
    CREW_ENGINEERING = 4
    CREW_SCANNER = 5
    health = 8
    shield = 4  
    dice_number = None

    crew = []
    threads = []
    difficulty = menu() #loop --> returns difficulty level, prints high scores
    
    set_spawn_power(2)

    running = True
    while running:
        
        if health <= 0: # kills the game loop if you die
            running  = False

        print_interface(health, shield, crew, threads, dice_number) # prints the ship, health, cards, crew
        crew = get_crew()

        threads, dice_number = get_thread()


    
    game_over()




if __name__ == "__main__":
    main()
