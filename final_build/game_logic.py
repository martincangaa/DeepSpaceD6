import random
from collections import Counter
import input_output_user as io

CREW_COMMANDER = 0
CREW_TACTICAL = 1
CREW_MEDICAL = 2
CREW_SCIENCE = 3
CREW_ENGINEERING = 4
CREW_SCANNER = 5
EMPTY = 6
no_health_threat = 15

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
    
    boarding_ship = {'name': 'Boarding Ship', 'description': '-2 Hull, Can be blocked if you use one T, but it gets sent to I', 'dice_numbers': [3, 4], 'health': 4, 'attack': '2NM',  'assignable_crew': [CREW_TACTICAL, CREW_TACTICAL], 
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

    cosmic_existentialism = {'name': 'Cosmic Existentialism', 'description': 'Must be completed before assigning any other S', 'dice_numbers': [], 'health': no_health_threat, 'attack': '',  'assignable_crew': [CREW_SCIENCE], 
                'assigned_crew': [], 'block_till_complete': [3], 'mission': True, 'stun': False}

    nebula = {'name': 'Nebula', 'description': 'Shields offline, -1NM when destroyed shields online', 'dice_numbers': [1,2,3,4,5], 'health': 3, 'attack': '1NM',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': True, 'stun': False}

    mercenary = {'name': 'Mercenary', 'description': 'If no threats activated this round, -2Hull', 'dice_numbers': [], 'health': 3, 'attack': '2NM',  'assignable_crew': [], 
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
                       nebula, mercenary, cloaked_threats, assault_cruiser, distracted, time_warp, bomber2, boost_morale, panel_explosion, assault_cruiser2, pandemic, invaders,
                       bomber3, comms_offlime, robot_uprising]
    
    return list_of_threats


def add_threat(active_threats, threats, crew):
    
    active_threats_copy = active_threats.copy()
    threats_copy = threats.copy()
    crew_copy = crew.copy()

    random_threat = random.choice(threats_copy)
    
    active_threats_copy.append(random_threat)
    threats_copy.remove(random_threat)
    
    if random_threat == 'Distracted':
        
        random_list = [0,1,2,3,4,5]
        
        while random_list != []:

            i = random.choice(random_list)
            random_list.remove(i)
        
            if crew[i]['blocked'] == False and crew[i]['infirmary'] == False:
                member[i]['blocked'] == True and member[i]['infimary'] == True
                break
    
    return active_threats_copy, threats_copy, crew_copy

def activate_threats(active_threats,crew, threat, throw_dice_result, health, shield):
    """
    Activates each threat regarding the result of the die.
    Damage_done is a boolean used so as to help with the 'Scouting ship' threat
    activated_threat is a boolean used so as to help with the 'mercernary' threat
    
    Args:
        active_threats: list with the current active threats
        crew: list with the crew 
        threat: 
        throw_dice_result: e
        
    Returns:
        list: The updated list of crewmembers.
    """
    #damage_done 
    damage_done = False
    activated_threat = False
    
    if not threat['mission']:
        
        if throw_dice_result in threat['dice_numbers']:
            #so as to check if the threat is stunned
            if threat['attack'][1:] == 'NM' and threat['stun'] == False:
                shield -= int(threat['attack'][0:1])
                if shield <0:
                    health -= abs(shield)
                    shield=0
            if threat['attack'][1:] == 'IS' and threat['stun'] == False:
                health = health - int(threat['attack'][0:1])
            if threat['attack'][1:] == 'DS' and threat['stun'] == False:
                shield = 0
                health -= int(threat['attack'][0:1])
    
    if threat['mission']:
        
        if throw_dice_result in threat['dice_numbers']:
            
            if threat['name'] == 'Meteoroid' and threat['stun'] == False:
                health -= int(threat['attack'][0:1])
                damage_done = True
                activated_threat = True
                
                if threat['health'] <= 0:
                    shield -= 5
                    if shield <= 0:
                        health -= abs(shield)
                        shield=0
            
            if threat['name'] == 'Meteoroid' and threat['stun'] == True:
                threat['stun'] = False

            if threat['name'] == 'Solar Winds' and threat['stun'] == False:
                shield -= int(threat['attack'][0:1])
                damage_done = True
                activated_threat = True
                if shield <0:
                    health -= abs(shield)
                    shield=0
                active_threats.remove(solar_winds)

            if threat['name'] == 'Solar Winds' and threat['stun'] == True:
                threat['stun'] = False

            if threat['name'] == 'Boarding Ship' and threat['stun'] == False:
                shield -= int(threat['attack'][0:1])
                damage_done = True
                activated_threat = True
                if shield <0:
                    health -= abs(shield)
                    shield=0
                
                
            if threat['name'] == 'Boarding Ship' and threat['stun'] == True:
                threat['stun'] = False
            
            if (threat['name'] == 'Bomber' or threat['name'] == 'Bomber2' or threat['name'] == 'Bomber3') and threat['stun'] == False:
                while True:
                    i = random.randint(0,5)
                    if crew[i]['blocked'] == False and crew[i]['infirmary'] == False:
                        crew[i]['infimary'] = True
                        break     
                shield -= int(threat['attack'][0:1])
                damage_done = True
                activated_threat = True
                if shield <0:
                    health -= abs(shield)
                    shield=0
            
            if (threat['name'] == 'Bomber' or threat['name'] == 'Bomber2' or threat['name'] == 'Bomber3') and threat['stun'] == True:
                threat['stun'] = False
            
            if threat['name'] == 'Hijackers' and threat['stun'] == False:
                shield -= int(threat['attack'][0:1])
                damage_done = True
                activated_threat = True
                if shield <0:
                    health -= abs(shield)
                    shield=0
                
           
            if threat['name'] == 'Hijackers' and threat['stun'] == True:   
                threat['stun'] = False        
            
            if threat['name'] == 'Pandemic' and threat['stun'] == False:
                activated_threat = True
                while True:
                    i = random.randint(0,5)
                    if crew[i]['blocked'] == False and crew[i]['infirmary'] == False:
                        crew[i]['infimary'] = True
                        break
                
            
            if threat['name'] == 'Pandemic' and threat['stun'] == True:
                threat['stun'] = False
            
            if threat['name'] == 'Invaders':
                activated_threat = True
                while True:
                    i = random.randint(0,5)
                    if crew[i]['blocked'] == False and crew[i]['infirmary'] == False:
                        crew[i]['infimary'] = True
                        break
                
            
            if threat['name'] == 'Invaders' and threat['stun'] == True:
                threat['stun'] = False
        
            if threat['name'] == 'Robot Uprising':
                activated_threat = True
                while True:
                    i = random.randint(0,5)
                    if crew[i]['blocked'] == False and crew[i]['infirmary'] == False:
                        crew[i]['infimary'] = True
                        break
                
                   
            if  threat['name'] == 'Robot Uprising' and threat['stun'] == True:
                threat['stun'] = False

            if threat['name'] == 'Panel Explosion' and threat['stun'] == False:
                activated_threat = True
                crew[4]['blocked'] = True
                
            
            if threat['name'] == 'Panel Explosion' and threat['stun'] == True:
                threat['stun'] = False

            if threat['name'] == 'Comms Offline' and threat['stun'] == False:
                activated_threat = True
                crew[0]['blocked'] = True
                

            
            if threat['name'] == 'Comms Offline' and threat['stun'] == True:
                threat['stun'] = False

            if threat['name'] == 'Cosmic Existentialism' and threat['stun'] == False:
                activated_threat = True
                crew[3]['blocked'] = True
                

            
            if threat['name'] == 'Cosmic Existentialism' and threat['stun'] == True:
                threat['stun'] = False

            if threat['name'] == 'Friendly Fire' and threat['stun'] == False:
                activated_threat = True
                for member in crew:
                   if crew['crew_type'] == 1:
                       crew['infirmary'] = True
                
            
            if threat['name'] == 'Friendly Fire' and threat['stun'] == True:
                threat['stun'] = False

            if threat['name'] == 'Boost Morale' and threat['stun'] == False:
                activated_threat = True
                for member in crew:
                    if member['crew_type'] == 5:
                        member['crew_type'] = 6
                        member['blocked'] = False
                        break
                
            
            if threat['name'] == 'Boost Morale' and threat['stun'] == True:
                threat['stun']= False

            if threat['name'] == 'Time Warp' and threat['stun'] == False:
                activated_threat = True
                initial_health = threat['health']
                for t in active_threats:
                    if health != initial_health:
                        health += 1
            
            if threat['name'] == 'Time Warp' and threat['stun'] == True:
                threat['stun'] = False

            if threat['name'] == 'Distracted' and threat['stun'] == False:
                activated_threat = True

                random_list = [0,1,2,3,4,5] # little tricks

                for i in range(len(crew)):
                    i = random.randint(0,5)
                    if member[i]['blocked'] == True and member[i]['infirmary'] == True:
                        member[i]['blocked'] = False  
                        member[i]['infimary'] = False
                
            
            if threat['name'] == 'Distracted' and threat['stun'] == True:
                threat['stun'] = False

            if threat['name'] == 'Cloaked Threats' and threat['stun'] == False:
                activated_threat = True
                iterate_through_threats(active_threats, crew, health, shield)
                
            if threat['name'] == 'Cloaked Threats' and threat['stun'] == True:
                threat['stun'] = False

            if threat['name'] == 'Nebula' and threat['stun'] == False:
                activated_threat = True
                offline_shields_value = -50
                shield = offline_shields_value
                if threat['health'] == 0:
                    shield = 0
                shield -= int(threat['attack'][0:1])
                damage_done = True
                if shield <0:
                    health -= abs(shield)
                    shield=0
            
            if threat['name'] == 'Nebula' and threat['stun'] == True:
                threat['stun'] = False
            
            if threat['name'] == 'Mercenary' and activated_threat == False and threat['stun'] == False :
                shield -= int(threat['attack'][0:1])
                if shield <0:
                    health -= abs(shield)
                    shield=0
            
            if threat['name'] == 'Mercenary' and activated_threat == False and threat['stun'] == True :
                threat['stun'] = False

            if threat['name'] == 'Scouting Ship' and damage_done and threat['stun'] == False:
                shield -= int(threat['attack'][0:1])
                if shield <0:
                    health -= abs(shield)
                    shield=0
            
            if threat['name'] == 'Scouting Ship' and damage_done and threat['stun'] == True:
                threat['stun'] = False
    
    return crew, active_threats, health, shield

def throw_dice(n):
    """
    Throws 'n' number of dice and returns an array with the random numbers.
    
    Args:
        n (int): The number of dice to be thrown.
        
    Returns:
        list: An array with 'n' random numbers between 1 and 6.
    """
    random_numbers = []
    for i in range(n):
        random_numbers.append(random.randint(1, 6))
    return random_numbers

def iterate_through_threats(active_threats, crew, health, shield):
    throw_dice_result = throw_dice(1)

    io.print_interface("Roll threat's dice", health, shield, active_threats, crew, "Press (↵) to continue", True, throw_dice_result[0])

    new_health = health
    new_shield = shield

    for threat in active_threats:
        crew, active_threats, new_health, new_shield = activate_threats(active_threats, crew, threat, throw_dice_result[0], new_health, new_shield)    
    
    return throw_dice_result[0], crew, active_threats, new_health, new_shield

def get_crew(crew):
    crew_copy = crew.copy()

    for member in crew_copy:
        if member['infirmary'] == False and member['blocked'] == False:
                member['crew_type'] = random.choice([CREW_COMMANDER, CREW_TACTICAL, CREW_MEDICAL, CREW_SCIENCE, CREW_ENGINEERING, CREW_SCANNER])
                if member["crew_type"] == CREW_SCANNER:
                    member["blocked"] = True
    return crew_copy

def free_scanners(crew, n_of_scanners):
    """
    Changes the crew type of three crewmates of type scanner

    Args:
        crew (array): An array containing the crewmates
        n_of_scanners (int): the number of scanners in the crew
    
    Returns:
        n_of_scanners (int): the number of remaining scanners in crew
        crew_copy (array): An array containing the updated crewmates
    """
    crew_copy = crew[:]
    crewmate = 0
    n_of_released_scanners = 0

    while n_of_released_scanners < 3 and crewmate < len(crew):
        if crew_copy[crewmate]["crew_type"] == 5:
            crew_copy[crewmate]["crew_type"] = 6
            crew_copy[crewmate]["blocked"] = False
            n_of_released_scanners += 1
            n_of_scanners -= 1
        crewmate += 1
    return n_of_scanners, crew_copy

def check_scanners(crew, active_threats, threats):
    """
    Counts the number of scanners in the crew, spawns a new threat for each 3 scanners
    and then frees those scanners used to spawn the threat.

    Args:
        crew (array): An array containing the crewmates

    Returns: 
        crew_copy (array): An array containing the updated crewmates
    """
    crew_copy = crew[:]
    n_of_scanners = 0

    for crewmate in crew_copy:
        if crewmate["crew_type"] == 5:
            n_of_scanners += 1
    
    while n_of_scanners >= 3:
        active_threats, threats, crew_copy = add_threat(active_threats, threats, crew)
        n_of_scanners, crew_copy = free_scanners(crew, n_of_scanners)

    return crew_copy, active_threats, threats

def check_difficulty(threats):
    """
    Checks the difficulty selected by the user in the menu and substracts a given number of
    Don't Panic cards from the threats array in order to change the difficulty of the game

    Args:
        difficulty (int): The difficulty selection of the user in the menu (1 = easy, 2 = medium, 3 = hard)
    
    Returns:
        new_threats (array): An array similar to the threats one but without the corresponding Don't Panic cards
    """
    new_threats = threats[:]
    dont_panic = {'name': "Don't Panic", 'description': 'nothing happens', 'dice_numbers': [], 'health': 15, 'attack': '',  'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'mission': False, 'stun': False}

    f = open('difficulty.txt', "r")
    difficulty = f.readline().strip() 
    f.close()

    if difficulty == "1":
        cards_to_be_added = 5
    if difficulty == "2":
        cards_to_be_added = 2
    if difficulty == "3":
        cards_to_be_added = 0

    while cards_to_be_added > 0:
        random_index = random.randint(0, len(new_threats))
        new_threats.insert(random_index, dont_panic)
        cards_to_be_added -= 1


    return new_threats

def free_crew(threat, crew):
    crew_copy = crew[:]
    for assigned_crewmate in threat["assigned_crew"]:
        for crewmate in crew_copy:
            if crewmate["crew_type"] == assigned_crewmate and crewmate["blocked"]:
                crewmate["blocked"] = False
                break
    return crew_copy

def check_threats(active_threats, crew):
    active_threats_copy = active_threats[:]
    crew_copy = crew[:]
    threats_to_remove = []
    
    for threat in active_threats_copy:
        if threat['name'] == "Friendly Fire" or threat['name'] == "Boost Morale":
            threats_to_remove.append(threat)
            crew_copy = free_crew(threat, crew)
        if threat['health'] <= 0:
            threats_to_remove.append(threat)
            crew_copy = free_crew(threat, crew)

        if len(threat["assignable_crew"]) > 0 and Counter(threat['assignable_crew']) == Counter(threat['assigned_crew']):
            threats_to_remove.append(threat)
            crew_copy = free_crew(threat, crew)

    for threat in threats_to_remove:
        active_threats_copy.remove(threat)

    return active_threats_copy, crew_copy

def can_be_gathered(crew):
    for crewmate in crew:
        if crewmate['blocked'] == False and crewmate['infirmary'] == False and crewmate['crew_type'] != CREW_SCANNER:
            return True
    return False