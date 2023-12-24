
import time

#add_threat
#game_over
#get_crew
#activate_threats
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
    time.sleep(2)
ask_user = input("Do you want to keep playing?\n Yes\n No")
print(ask_user)
while ask_user != 'Yes' or ask_user != 'No':
    ask_user = input("")

if ask_user == "Yes":
    main()
elif ask_user == 'no':
    exit
pass

def add_threat(crew):
    no_health_threat = 15
    flagship = {'name': 'Flagship', 'description': '-3 Hull', 'dice_numbers': [4,5,6], 'health': 4, 'attack': '3NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
    
    solar_winds = {'name': 'Solar Winds', 'description': '-5 Hull then discard ', 'dice_numbers': [2], 'health': no_health_threat, 'attack': '5NM', 'volatility': False, 'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
    
    intercepter = {'name': 'Intercepter', 'description': '-1 Hull', 'dice_numbers': [1,2,3,4,5], 'health': 3, 'attack': '1NM', 'volatility': True, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False}
    
    scouting_ship = {'name': 'Scouting Ship', 'description': 'If you lost Hull this round, lose 1 additional Hull', 'dice_numbers': [], 'health': 3, 'attack': '1NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
    #raiders is repeated 3 times thorough the game
    raiders = {'name': 'Raiders', 'description': '-2 Hull Ignore shields', 'dice_numbers': [4,6], 'health': 2, 'attack': '2IG', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 

    raiders2 = {'name': 'Raiders', 'description': '-2 Hull Ignore shields', 'dice_numbers': [4,6], 'health': 2, 'attack': '2IG', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
    
    raiders3 = {'name': 'Raiders', 'description': '-2 Hull Ignore shields', 'dice_numbers': [4,6], 'health': 2, 'attack': '2IG', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
    
    boarding_ship = {'name': 'Boarding Ship', 'description': '-2 Hull Can be blocked if you use one tactial unit, but it gets sent to infirmary', 'dice_numbers': [3, 4], 'health': 4, 'attack': '2NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [CREW_TACTICAL], 'block_till_complete': [], 'send_infirmary': True, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
    #space_pirates is repeated 3 times thorough the game
    space_pirates = {'name': 'Space Pirates', 'description': '-2 Hull', 'dice_numbers': [1, 3], 'health': 3, 'attack': '2NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False}

    space_pirates2 = {'name': 'Space Pirates', 'description': '-2 Hull', 'dice_numbers': [1, 3], 'health': 3, 'attack': '2NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
    
    space_pirates3 = {'name': 'Space Pirates', 'description': '-2 Hull', 'dice_numbers': [1, 3], 'health': 3, 'attack': '2NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
      
    #Meteoroid removes 5 points of hull when destroyed, I've got no clue on if I should create a new key for that or just do it when I activate it 
    meteoroid = {'name': 'Meteoroid', 'description': '-1 Health, when destroyed -5 Hull', 'dice_numbers': [1], 'health': 4, 'attack': '1IS', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
    #drone is repeated 2 times thorough the game
    drone = {'name': 'Drone', 'description': '-1 Hull', 'dice_numbers': [2,4,6], 'health': 1, 'attack': '1NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False}
    
    drone2 = {'name': 'Drone', 'description': '-1 Hull', 'dice_numbers': [2,4,6], 'health': 1, 'attack': '1NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False}  
    
    bounty_ship = {'name': 'Bounty Ship', 'description': 'Destroy all shields -1 Hull', 'dice_numbers': [1, 2], 'health': 4, 'attack': '1DS', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
    #Bomber is repeated 2 times thorough the game
    bomber = {'name': 'Bomber', 'description': '-1 Hull, send a unit to the infirmary', 'dice_numbers': [3,4], 'health': 3, 'attack': '1NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': True, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
    
    bomber2 = {'name': 'Bomber', 'description': '-1 Hull, send a unit to the infirmary', 'dice_numbers': [3,4], 'health': 3, 'attack': '1NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': True, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
    
    intercepter_x = {'name': 'Intercepter X', 'description': '-1 Hull', 'dice_numbers': [1,2,3,4,5], 'health': 4, 'attack': '1NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
    
    hijackers = {'name': 'Hijackers', 'description': '-2 Hull', 'dice_numbers': [4,5], 'health': 4, 'attack': '1NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [CREW_COMMANDER, CREW_COMMANDER], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
    
    corsair = {'name': 'Corsair', 'description': '-2 Hull', 'dice_numbers': [4,5,6], 'health': 2, 'attack': '2NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
    
    friendly_fire = {'name': 'Friendly Fire', 'description': 'All tactical crew gets sent to infirmary', 'dice_numbers': [], 'health': no_health_threat, 'attack': '', 'volatility': True, 'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': True, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': True} 

    cosmic_existentialism = {'name': 'Cosmic Existentialism', 'description': 'Must be completed before assigning any other scientific crew', 'dice_numbers': [], 'health': -, 'attack': '', 'volatility': False, 'assignable_crew': [CREW_SCIENCE], 
                'assigned_crew': [CREW_SCIENCE], 'block_till_complete': [CREW_SCIENCE], 'send_infirmary': False, 'mercenary': False, 'existentialism': [True, CREW_SCIENCE], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 

    nebula = {'name': 'Nebula', 'description': 'Shields offline, -1NM when destroyed shields online', 'dice_numbers': [1,2,3,4,5], 'health': 3, 'attack': '1NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False, 'shields_online': False}

    mercernary = {'name': 'Mercenary', 'description': 'If no threats activated this round, -2Hull', 'dice_numbers': [], 'health': 3, 'attack': '2NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': True, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False, 'shields_online': False} 

    cloaked_threats = {'name': 'Cloaked Threats', 'description': 'After the threat phase. Roll the threat die again', 'dice_numbers': [2], 'health': no_health_threat, 'attack': '', 'volatility': False, 'assignable_crew': [CREW_SCIENCE, CREW_COMMANDER], 
                'assigned_crew': [CREW_SCIENCE, CREW_COMMANDER], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False, 'shields_online': False} 

    assault_cruiser = {'name': 'Assault Cruiser', 'description': '-2Hull', 'dice_numbers': [4,5], 'health': 4, 'attack': '2NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False, 'shields_online': False}
    #I didn't do distracted because I felt lazy, I'll do it later
    assault_cruiser = {'name': 'Assault Cruiser', 'description': '-2Hull', 'dice_numbers': [4,5], 'health': 4, 'attack': '2NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False, 'shields_online': False}  
    #I didn't do TIME Warp because I felt lazy, I'll do it later
    assault_cruiser = {'name': 'Assault Cruiser', 'description': '-2Hull', 'dice_numbers': [4,5], 'health': 4, 'attack': '2NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False, 'shields_online': False}  
    #DO THOSE TWO DON'T FORGET
    boost_morale = {'name': 'Boost Morale', 'description': 'Return one scanner', 'dice_numbers': [6], 'health': no_health_threat, 'attack': '', 'volatility': True, 'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [CREW_SCANNER], 'send_infirmary': True, 'mercenary': False, 'existentialism': [False], 'return_scanner': True, 'stunt': False, 'tactical_to_infirmary': False} 
    
    panel_explosion = {'name': 'Bomber', 'description': '-1 Hull, send a unit to the infirmary', 'dice_numbers': [3,4], 'health': 3, 'attack': '1NM', 'volatility': False, 'assignable_crew': [CREW_TACTICAL], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': True, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stunt': False, 'tactical_to_infirmary': False} 
    
    

