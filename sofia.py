import time
import keyboard

# loop --> returns difficulty level

# DONE added to input_output_user.py
def menu():
    """
    Shows the user the different levels that can be played inside the game, asks which of them is going to be played and writes it in a file.


    Returns:
        int: Number corresponding to the level that the user wants to play (1=easy, 2=medium, 3=hard).
    """
    print('LEVELS OF DIFFICULTY:')
    print("1 - Easy: 1 Don't panic card is substracted from the threads")
    print("2 - Medium: 3 Don't panic cards are substracted from the threads")
    print("3 - Hard: 6 Don't panic cards are substracted from the threads")

    difficulty = input('Which level of difficulty do you want to play (1=easy, 2=medium, 3=hard)? ')
    while not (difficulty == '1' or difficulty == '2' or difficulty == '3'):
        print('Not valid level')
        difficulty = input('Which level of difficulty do you want to play (1=easy, 2=medium, 3=hard)? ')
    
    file = open('difficulty.txt', 'w')
    file.write(str(difficulty))
    file.close()


# Checks if there is at least one crewmate that can be gathered back, returns true or false
# A crewmate can't be gathered back if it is in the infirmary, it is a scanner or it is assigned to a Distracted threat

# DONE added to game_logic.py

def can_be_gathered(crew):
    for crewmate in crew:
        if crewmate['blocked'] == False and crewmate['infirmary'] == False and crewmate['crew_type'] != CREW_SCANNER:
            return True
    return False

# aux function that can be used to stop the execution of the program until the user decides
# we will use it if we decide that this approach is better than do it inside the print_interface

# DONE added to input_output_user.py
def user_confirmation():
    keyboard.wait("enter")

# added to input_output_user.py

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

def create_threats():
    #A few comments and points that I've jotted down in the making of this function
    #First of all, there are some threats which you can simply eliminate with tactical crew, but they can also be eliminated by assigning crew members
    #prolly, what we should do is create another boolean to check if said those two conditions are met (having health and also being able to disable it by assigning crew)
    #another thing that i've noted is that there is one function that can be disable either with a 3 or a with a 2, one option I've thought is the creation of another boolean
    #I've also been pondering if I should add another boolean to time_warp or instead I should  just do its effect on activate_threads
    no_health_threat = 15
    flagship = {'name': 'Flagship', 'description': '-3 Hull', 'dice_numbers': [4,5,6], 'health': 4, 'attack': '3NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False} 
    
    solar_winds = {'name': 'Solar Winds', 'description': '-5 Hull then discard ', 'dice_numbers': [2], 'health': no_health_threat, 'attack': '5NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False} 
    
    intercepter = {'name': 'Intercepter', 'description': '-1 Hull', 'dice_numbers': [1,2,3,4,5], 'health': 3, 'attack': '1NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False}
    
    scouting_ship = {'name': 'Scouting Ship', 'description': 'If you lost Hull this round, lose 1 additional Hull', 'dice_numbers': [], 'health': 3, 'attack': '1NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False}
    #raiders is repeated 3 times thorough the game
    raiders = {'name': 'Raiders', 'description': '-2 Hull Ignore shields', 'dice_numbers': [4,6], 'health': 2, 'attack': '2IG',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False} 

    raiders2 = {'name': 'Raiders', 'description': '-2 Hull Ignore shields', 'dice_numbers': [4,6], 'health': 2, 'attack': '2IG',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False} 
    
    raiders3 = {'name': 'Raiders', 'description': '-2 Hull Ignore shields', 'dice_numbers': [4,6], 'health': 2, 'attack': '2IG',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False} 
    
    boarding_ship = {'name': 'Boarding Ship', 'description': '-2 Hull Can be blocked if you use one tactial unit, but it gets sent to infirmary', 'dice_numbers': [3, 4], 'health': 4, 'attack': '2NM',  'assignable_crew': [CREW_TACTICAL, CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False}
    #space_pirates is repeated 3 times thorough the game
    space_pirates = {'name': 'Space Pirates', 'description': '-2 Hull', 'dice_numbers': [1, 3], 'health': 3, 'attack': '2NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False}

    space_pirates2 = {'name': 'Space Pirates', 'description': '-2 Hull', 'dice_numbers': [1, 3], 'health': 3, 'attack': '2NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False}
    
    space_pirates3 = {'name': 'Space Pirates', 'description': '-2 Hull', 'dice_numbers': [1, 3], 'health': 3, 'attack': '2NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False}
      
    #Meteoroid removes 5 points of hull when destroyed, I've got no clue on if I should create a new key for that or just do it when I activate it 
    meteoroid = {'name': 'Meteoroid', 'description': '-1 Health, when destroyed -5 Hull', 'dice_numbers': [1], 'health': 4, 'attack': '1IS',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False}
    #drone is repeated 2 times thorough the game
    drone = {'name': 'Drone', 'description': '-1 Hull', 'dice_numbers': [2,4,6], 'health': 1, 'attack': '1NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False}
    
    drone2 = {'name': 'Drone', 'description': '-1 Hull', 'dice_numbers': [2,4,6], 'health': 1, 'attack': '1NM',  'assignable_crew': [],
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False}
    
    bounty_ship = {'name': 'Bounty Ship', 'description': 'Destroy all shields -1 Hull', 'dice_numbers': [1, 2], 'health': 4, 'attack': '1DS',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False}
    #Bomber is repeated 2 times thorough the game though with different characteristics
    bomber = {'name': 'Bomber', 'description': '-1 Hull, send a unit to the infirmary', 'dice_numbers': [3,4], 'health': 3, 'attack': '1NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False}
    
    bomber2 = {'name': 'Bomber', 'description': '-1 Hull, send a unit to the infirmary', 'dice_numbers': [2,4], 'health': 2, 'attack': '1NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False}
    
    bomber3 = {'name': 'Bomber', 'description': '-2 Hull, send a unit to the infirmary', 'dice_numbers': [2,4], 'health': 2, 'attack': '2NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False}
    
    intercepter_x = {'name': 'Intercepter X', 'description': '-1 Hull', 'dice_numbers': [1,2,3,4,5], 'health': 4, 'attack': '1NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False}
    
    hijackers = {'name': 'Hijackers', 'description': '-2 Hull', 'dice_numbers': [4,5], 'health': 4, 'attack': '1NM',  'assignable_crew': [CREW_COMMANDER, CREW_COMMANDER], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False}
    
    corsair = {'name': 'Corsair', 'description': '-2 Hull', 'dice_numbers': [4,5,6], 'health': 2, 'attack': '2NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False}
    #This threat makes tactical go to infirmary
    friendly_fire = {'name': 'Friendly Fire', 'description': 'All tactical crew gets sent to infirmary', 'dice_numbers': [], 'health': no_health_threat, 'attack': '',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False}

    cosmic_existentialism = {'name': 'Cosmic Existentialism', 'description': 'Must be completed before assigning any other scientific crew', 'dice_numbers': [], 'health': no_health_threat, 'attack': '',  'assignable_crew': [CREW_SCIENCE], 
                'assigned_crew': [], 'block_till_complete': [3], 'mission': True, 'stun': False}

    nebula = {'name': 'Nebula', 'description': 'Shields offline, -1NM when destroyed shields online', 'dice_numbers': [1,2,3,4,5], 'health': 3, 'attack': '1NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False}

    mercernary = {'name': 'Mercenary', 'description': 'If no threats activated this round, -2Hull', 'dice_numbers': [], 'health': 3, 'attack': '2NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False} 

    cloaked_threats = {'name': 'Cloaked Threats', 'description': 'After the threat phase. Roll the threat die again', 'dice_numbers': [2], 'health': no_health_threat, 'attack': '',  'assignable_crew': [CREW_SCIENCE, CREW_COMMANDER], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False} 
    #assault_cruiser is repeated two times thorough the game 
    assault_cruiser = {'name': 'Assault Cruiser', 'description': '-2Hull', 'dice_numbers': [4,5], 'health': 4, 'attack': '2NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False}
    
    assault_cruiser2 = {'name': 'Assault Cruiser', 'description': '-2Hull', 'dice_numbers': [4,5], 'health': 4, 'attack': '2NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False}
    
    distracted = {'name': 'Distracted', 'description': 'Return distracted unit, then discard', 'dice_numbers': [3,4], 'health': no_health_threat, 'attack': '',  'assignable_crew': [CREW_MEDICAL, CREW_MEDICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False}  
    
    time_warp = {'name': 'Time Warp', 'description': 'All threats recover one damage', 'dice_numbers': [2], 'health': no_health_threat, 'attack': '',  'assignable_crew': [CREW_SCIENCE, CREW_SCIENCE], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False}  
    
    boost_morale = {'name': 'Boost Morale', 'description': 'Return one scanner', 'dice_numbers': [6], 'health': no_health_threat, 'attack': '',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False} 
    
    panel_explosion = {'name': 'Panel explosion', 'description': 'You may not assing engineers', 'dice_numbers': [], 'health': no_health_threat, 'attack': '',  'assignable_crew': [CREW_MEDICAL], 
                'assigned_crew': [], 'block_till_complete': [4], 'mission': True, 'stun': False} 
    
    pandemic = {'name': 'Pandemic', 'description': 'send a unit to the infirmary', 'dice_numbers': [1], 'health': no_health_threat, 'attack': '',  'assignable_crew': [CREW_SCIENCE, CREW_MEDICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False} 
    
    invaders = {'name': 'Invaders', 'description': 'send a unit to the infirmary', 'dice_numbers': [2,4], 'health': no_health_threat, 'attack': '',  'assignable_crew': [CREW_TACTICAL,CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False} 
    
    comms_offlime = {'name': 'Comms Offline', 'description': 'You may not assign commanders', 'dice_numbers': [], 'health': no_health_threat, 'attack': '',  'assignable_crew': [CREW_ENGINEERING], 
                'assigned_crew': [], 'block_till_complete': [0], 'mission': True, 'stun': False} 
    
    robot_uprising = {'name': 'Robot Uprising', 'description': 'Send unit to infirmary', 'dice_numbers': [1,2,3], 'health': no_health_threat, 'attack': '',  'assignable_crew': [CREW_ENGINEERING], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False} 
    
    list_of_threats = [flagship, solar_winds, intercepter, scouting_ship, raiders, boarding_ship, space_pirates, raiders2, raiders2, raiders3,
                       meteoroid, drone, bounty_ship, bomber, space_pirates2, intercepter_x, space_pirates3, drone2, hijackers, corsair, friendly_fire, cosmic_existentialism,
                       nebula, mercernary, cloaked_threats, assault_cruiser, distracted, time_warp, bomber2, boost_morale, panel_explosion, assault_cruiser2, pandemic, invaders,
                       bomber3, comms_offlime, robot_uprising]
    
    return list_of_threats
