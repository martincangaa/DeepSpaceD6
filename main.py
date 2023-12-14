    
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



def main():
    difficulty = menu() #loop --> returns difficulty level, prints high scores
    while running:
        print_interface() # prints the ship, health, cards, crew
        crew = get_crew()

        threads = get_thread()




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
