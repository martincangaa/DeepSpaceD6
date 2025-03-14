import random
from collections import Counter

no_health_threat = 15
flagship = {'name': 'Flagship', 'description': '-3 Hull', 'dice_numbers': [4,5,6], 'health': 0, 'attack': '3NM', 'volatility': False, 'assignable_crew': [1], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stun': False, 'tactical_to_infirmary': False} 
    
solar_winds = {'name': 'Solar Winds', 'description': '-5 Hull then discard ', 'dice_numbers': [2], 'health': no_health_threat, 'attack': '5NM', 'volatility': False, 'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stun': False, 'tactical_to_infirmary': False} 
    
intercepter = {'name': 'Intercepter', 'description': '-1 Hull', 'dice_numbers': [1,2,3,4,5], 'health': 3, 'attack': '1NM', 'volatility': True, 'assignable_crew': [1], 
                'assigned_crew': [1], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stun': False, 'tactical_to_infirmary': False}
    
scouting_ship = {'name': 'Scouting Ship', 'description': 'If you lost Hull this round, lose 1 additional Hull', 'dice_numbers': [], 'health': 3, 'attack': '1NM', 'volatility': False, 'assignable_crew': [1], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stun': False, 'tactical_to_infirmary': False} 

threats = [flagship, intercepter, solar_winds, scouting_ship]

active_threats = threats[:]

CREW_COMMANDER = 0
CREW_TACTICAL = 1
CREW_MEDICAL = 2
CREW_SCIENCE = 3
CREW_ENGINEERING = 4
CREW_SCANNER = 5
NONE = 6

crew = [{"crew_type":CREW_COMMANDER, "blocked": False, "infirmary": False},{"crew_type":CREW_TACTICAL, "blocked": False, "infirmary": True},{"crew_type":CREW_SCANNER, "blocked": True, "infirmary": False},{"crew_type":CREW_SCANNER, "blocked": True, "infirmary": False},{"crew_type":CREW_SCANNER, "blocked": True, "infirmary": False},{"crew_type":CREW_SCANNER, "blocked": True, "infirmary": False}]

health = 8
shield = 4

# DONE
def print_interface(health, shield, active_threats, crew, message_to_continue = "Press (↵) to continue", dice_number = "_", user_confirmation=False):
    """
    Prints the main interface of the game with the title, health, shield,
    active threats, the threat's dice result, the crew and messages for the user.

    Args:
        health (int): The player's life
        shield (int): The player's shields
        active_threats (array): An array containing the active threats at the moment
        crew (array): An array containing the crewmates
        message_to_continue (String): message to be printed in the bottom right corner to the user that has a default value
        dice_number (int): the threat's dice result, it's default value is a "_" so that it looks good when the dice hasn't been thrown
        user_confirmation (boolean): States wheter if the function should call user_confirmation after printing or just continue without waiting, default value = False
    """
    initials = ["C", "T", "M", "S", "E", "$", "/"]
    health_percentage = int(health/8*100)
    shield_percentage = int(shield/4*100)
    active_threats_str = ""

    for threat in active_threats:
        threat_health = str(threat["health"])
        if threat_health == "15":
            threat_health = "◬"
        threat_info = "- " + threat_health + " | " + str(threat["name"]) + " | " + str(threat["description"]) + " | " + str(threat["assigned_crew"])
        remaining_spaces = 92-len(threat_info)
        str1 = " "* remaining_spaces + "║" + "\n║   "
        active_threats_str += threat_info + str1

    print(f"""
╔═══════════════════════════════════════════════════════════════════════════════════════════════╗   
║                                                                                               ║   C = Commander      T = Tactical
║                             .-. .-. .-. .-.   .-. .-. .-. .-. .-.                             ║   M = Medical        S = Science 
║                             |  )|-  |-  |-'   `-. |-' |-| |   |-                              ║   E = Engineering    $ = Scanner         / = None
║                             `-' `-' `-' '     `-' '   ` ' `-' `-'                             ║   
║                             -------------------------------------                             ║   B = Blocked        I = Infirmary       F = Free
║                                                                                               ║
║                                                                                               ║   ◬ = Internal Threat
║                         ___                        Health: {str(health_percentage) + "%" + " "*(4-len(str(health_percentage))) + "███"*health + " "*(32-health*3-2)}║   Active Threats Structure --> Health | Name | Description | Assigned crew
║     Active Threats:    |_{dice_number}_|                                                                  ║
║   -----------------------------                    Shield: {str(shield_percentage) + "%" + " "*(4-len(str(shield_percentage))) + "███"*shield + " "*(32-shield*3-2)}║
║                                                                                               ║
║   {active_threats_str}                                                                                            ║
║                                                                                               ║
║   ┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌───┐                     {"." + "-"*len(message_to_continue) + "." + " " * (29-len(message_to_continue))}║
║   │ {initials[crew[0]["crew_type"]]} │  │ {initials[crew[1]["crew_type"]]} │  │ {initials[crew[2]["crew_type"]]} │  │ {initials[crew[3]["crew_type"]]} │  │ {initials[crew[4]["crew_type"]]} │  │ {initials[crew[5]["crew_type"]]} │                     |{message_to_continue}|{" " * (29-len(message_to_continue))}║
║   └───┘  └───┘  └───┘  └───┘  └───┘  └───┘                     {"'" + "-"*len(message_to_continue) + "'" + " " * (29-len(message_to_continue))}║
║     {"F" if not crew[0]["blocked"] and not crew[0]["infirmary"] else "I" if crew[0]["infirmary"] else "B"}      {"F" if not crew[1]["blocked"] and not crew[1]["infirmary"] else "I" if crew[1]["infirmary"] else "B"}      {"F" if not crew[2]["blocked"] and not crew[2]["infirmary"] else "I" if crew[2]["infirmary"] else "B"}      {"F" if not crew[3]["blocked"] and not crew[3]["infirmary"] else "I" if crew[3]["infirmary"] else "B"}      {"F" if not crew[4]["blocked"] and not crew[4]["infirmary"] else "I" if crew[4]["infirmary"] else "B"}      {"F" if not crew[5]["blocked"] and not crew[5]["infirmary"] else "I" if crew[5]["infirmary"] else "B"}                                                      ║
║                                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════╝         
           """)
    if user_confirmation == True:
        user_confirmation()

# DONE added to game_logic.py
def check_scanners(crew):
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
        add_threat(active_threats, threats)
        n_of_scanners= free_scanners(crew, n_of_scanners)
        
    print_interface(health, shield, threats, crew, "Press (↵) to continue")

    return crew_copy

# DONE added to game_logic.py
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

# DONE
def check_difficulty(filename):
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

    f = open(filename, "r")
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
    for assigned_crewmate in threat["assigned_crew"]:
        for crewmate in crew:
            if crewmate == assigned_crewmate and crewmate["blocked"]:
                crewmate["blocked"] = False
                break

def check_threats(active_threats):
    active_threats_copy = active_threats[:]
    threats_to_remove = []
    
    for threat in active_threats_copy:
        if threat['name'] == "Friendly Fire" or threat['name'] == "Boost Morale":
            threats_to_remove.append(threat)
            free_crew(threat, crew)
        if threat['health'] <= 0:
            threats_to_remove.append(threat)
            free_crew(threat, crew)
        if len(threat["assignable_crew"]) > 0 and Counter(threat['assignable_crew']) == Counter(threat['assigned_crew']):
            threats_to_remove.append(threat)
            free_crew(threat, crew)

    for threat in threats_to_remove:
        active_threats_copy.remove(threat)

    return active_threats_copy
    
def main():
    #new_threats = check_difficulty(3)
    #print(new_threats)
    #print_interface(health, shield, threats, crew, "Press (↵) to continue")
    #check_scanners(crew)
    print(check_threats(active_threats))

if __name__ == "__main__":
    main()