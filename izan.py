
threats = [{"name": "Don't Panic", "ID": 0},{"name": "Menace 1", "Life": 2},{"name": "Don't Panic", "ID": 1},
           {"name": "Don't Panic", "ID": 2},{"name": "ey", "Life": 3},{"name": "Don't Panic", "ID": 3},
           {"name": "Don't Panic", "ID": 4},{"name": "Don't Panic", "ID": 5}]

active_threats = threats[:]

crew = [{"crew_type":"scanner"},{"crew_type":"scanner"},{"crew_type":"medical"},{"crew_type":"scanner"},{"crew_type":"scanner"},{"crew_type":"scanner"}]

health = 8
shield = 4

# ALMOST DONE --> Change what is printed from each threat
def print_interface(health, shield, dice_number, active_threats, crew):
    health_percentage = int(health/8*100)
    shield_percentage = int(shield/4*100)
    active_threats_str = ""

    for threat in active_threats:
        remaining_spaces = 92-len(str(threat))
        str1 = " "* remaining_spaces + "║" + "\n║   "
        active_threats_str += str(threat) + str1

    print(f"""
╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                               ║
║                             .-. .-. .-. .-.   .-. .-. .-. .-. .-.                             ║
║                             |  )|-  |-  |-'   `-. |-' |-| |   |-                              ║
║                             `-' `-' `-' '     `-' '   ` ' `-' `-'                             ║
║                             -------------------------------------                             ║
║                                                                                               ║
║                                                                                               ║
║                         ___                        Health: {health_percentage}% {"███" * health}{" "*(33-health*3-len(str(health_percentage)))}║
║     Active Threats:    |_{dice_number}_|                                                                  ║
║   -----------------------------                    Shield: {shield_percentage}% {"███" * shield}{" "*(33-shield*3-len(str(shield_percentage)))}║
║                                                                                               ║
║   {active_threats_str}                                                                                            ║
║                                                                                               ║
║   ┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌───┐                     .-----------------------.      ║
║   │ {crew[0]["crew_type"][0].upper()} │  │ {crew[1]["crew_type"][0].upper()} │  │ {crew[2]["crew_type"][0].upper()} │  │ {crew[3]["crew_type"][0].upper()} │  │ {crew[4]["crew_type"][0].upper()} │  │ {crew[5]["crew_type"][0].upper()} │                     |Press enter to continue|      ║
║   └───┘  └───┘  └───┘  └───┘  └───┘  └───┘                     '-----------------------'      ║
║                                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════╝         
           """)
    
    user_confirmation()

# DONE
def check_scanners(crew):
    n_of_scanners = 0

    for crewmate in crew:
        if crewmate["crew_type"] == "scanner":
            n_of_scanners += 1
    
    while n_of_scanners >= 3:
        add_threat(active_threats, threats)
        n_of_scanners= free_scanners(crew, n_of_scanners)
        
        
    print_interface(health, shield, 6, threats, crew)

# DONE
def free_scanners(crew, n_of_scanners):
    crewmate = 0
    n_of_released_scanners = 0

    while n_of_released_scanners < 3 and crewmate < len(crew):
        if crew[crewmate]["crew_type"] == "scanner":
            crew[crewmate]["crew_type"] = "none"
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
    #print_interface(health, shield, 6, threats, crew)
    check_scanners(crew)

if __name__ == "__main__":
    main()