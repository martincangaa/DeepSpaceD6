
no_health_threat = 15
flagship = {'name': 'Flagship', 'description': '-3 Hull', 'dice_numbers': [4,5,6], 'health': 4, 'attack': '3NM', 'volatility': False, 'assignable_crew': [1], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stun': False, 'tactical_to_infirmary': False} 
    
solar_winds = {'name': 'Solar Winds', 'description': '-5 Hull then discard ', 'dice_numbers': [2], 'health': no_health_threat, 'attack': '5NM', 'volatility': False, 'assignable_crew': [], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stun': False, 'tactical_to_infirmary': False} 
    
intercepter = {'name': 'Intercepter', 'description': '-1 Hull', 'dice_numbers': [1,2,3,4,5], 'health': 3, 'attack': '1NM', 'volatility': True, 'assignable_crew': [1], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stun': False, 'tactical_to_infirmary': False}
    
scouting_ship = {'name': 'Scouting Ship', 'description': 'If you lost Hull this round, lose 1 additional Hull', 'dice_numbers': [], 'health': 3, 'attack': '1NM', 'volatility': False, 'assignable_crew': [1], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stun': False, 'tactical_to_infirmary': False} 

threats = [flagship, solar_winds, intercepter, scouting_ship]

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

# DONE
def check_scanners(crew):
    n_of_scanners = 0

    for crewmate in crew:
        if crewmate["crew_type"] == 5:
            n_of_scanners += 1
    
    while n_of_scanners >= 3:
        add_threat(active_threats, threats)
        n_of_scanners= free_scanners(crew, n_of_scanners)
        
        
    print_interface(health, shield, threats, crew, "Press (↵) to continue")

# DONE
def free_scanners(crew, n_of_scanners):
    crewmate = 0
    n_of_released_scanners = 0

    while n_of_released_scanners < 3 and crewmate < len(crew):
        if crew[crewmate]["crew_type"] == 5:
            crew[crewmate]["crew_type"] = 6
            crew[crewmate]["blocked"] = False
            n_of_released_scanners += 1
            n_of_scanners -= 1
        crewmate += 1
    return n_of_scanners

# DONE
def check_difficulty(difficulty):
    new_threats = threats[:]

    if difficulty == "1":
        cards_to_be_removed = 1
    if difficulty == "2":
        cards_to_be_removed = 3
    if difficulty == "3":
        cards_to_be_removed = 6

    while cards_to_be_removed > 0:
        for threat in new_threats:
            if threat["name"] == "Don't Panic":
                new_threats.remove(threat)
                cards_to_be_removed -= 1
                break

    return new_threats

def user_confirmation():
    pass

def add_threat(active_threats, threats):
    pass

def main():
    #new_threats = check_difficulty("3")
    #print(new_threats)
    print_interface(health, shield, threats, crew, "Press (↵) to continue")
    check_scanners(crew)

if __name__ == "__main__":
    main()