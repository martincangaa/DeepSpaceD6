    
def user_input_menu():
    pass

def throw_dice():
    pass

def get_crew():
    # call throw_dice
    pass 

def get_thread():
    # call throw_dice
    pass

def game_over():
    pass

def main():
    difficulty = menu() #loop --> returns difficulty level, prints high scores
    
    running = True
    while running:
        
        if health <= 0: # kills the game loop if you die
            running  = False

        print_interface() # prints the ship, health, cards, crew
        crew = get_crew()

        threads = get_thread()
    
    game_over()




if __name__ == "__main__":
    CREW_COMMANDER = 0
    CREW_TACTICAL = 1
    CREW_MEDICAL = 2
    CREW_SCIENCE = 3
    CREW_ENGINEERING = 4
    CREW_SCANNER = 5
    health = 8
    shield = 4
    main()
