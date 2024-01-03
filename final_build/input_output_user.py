import random
import keyboard
import os
import time
from collections import Counter

CREW_COMMANDER = 0
CREW_TACTICAL = 1
CREW_MEDICAL = 2
CREW_SCIENCE = 3
CREW_ENGINEERING = 4
CREW_SCANNER = 5
NONE = 6

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
    while difficulty != '1' and difficulty != '2' and difficulty != '3':
        print('Not valid level')
        difficulty = input('Which level of difficulty do you want to play (1=easy, 2=medium, 3=hard)? ')
    
    file = open('difficulty.txt', 'w')
    file.write(str(difficulty))
    file.close()

def print_interface(health, shield, active_threats, crew, message_to_continue='Press (↵) to continue', user_confirmation=False, dice_number='_'):
    os.system("cls")
    initials = ["C", "T", "M", "S", "E", "$", "/"]
    health_percentage = int(health/8*100)
    shield_percentage = int(shield/4*100)
    active_threats_str = ""

    for threat in active_threats:
        threat_health = str(threat["health"])
        if threat_health == "15":
            threat_health = "◬"
        threat_info = "- " + threat_health + " | " + str(threat["name"]) + " | " + str(threat["description"]) + " | " + str(threat["assignable_crew"]) + " | " + str(threat["assigned_crew"]) 
        remaining_spaces = 92-len(threat_info)
        str1 = " "* remaining_spaces + "║" + "\n║   "
        active_threats_str += threat_info + str1

    print(f"""
╔═══════════════════════════════════════════════════════════════════════════════════════════════╗   
║                                                                                               ║   C = Commander (0)     T = Tactical (1)
║                             .-. .-. .-. .-.   .-. .-. .-. .-. .-.                             ║   M = Medical (2)        S = Science (3) 
║                             |  )|-  |-  |-'   `-. |-' |-| |   |-                              ║   E = Engineering (4)    $ = Scanner         / = None
║                             `-' `-' `-' '     `-' '   ` ' `-' `-'                             ║   
║                             -------------------------------------                             ║   B = Blocked        I = Infirmary       F = Free
║                                                                                               ║
║                                                                                               ║   ◬ = Internal Threat
║                         ___                        Health: {str(health_percentage) + "%" + " "*(4-len(str(health_percentage))) + "███"*health + " "*(32-health*3-2)}║   Active Threats Structure --> Health | Name | Description | Assignable crew | Assigned crew
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
    
    if user_confirmation:
        keyboard.wait("enter")

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

def clear_terminal():
    """
    Clears the terminal screen.
    """
    # Check the operating system
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Linux or Mac
        os.system('clear')


def change_face(crewmember):
    """
    Changes the crew type of a crewmember based on user input.
    
    Args:
        crewmember (dict): The crewmember whose crew type is to be changed.
        
    Returns:
        dict: The updated crewmember with the new crew type.
    """
    crewmember_copy = crewmember.copy()
    print('Choose into what you want to change the crewmember to: \n\n1) Tactical\n2) Medical\n3) Scientific\n4) Engineer')
    
    time.sleep(0.1)

    key_pressed = True

    while True:
        if keyboard.is_pressed('1'):
            if not key_pressed:
                key_pressed = True
                crewmember_copy['crew_type'] = CREW_TACTICAL
                break
        elif keyboard.is_pressed('2'):
            if not key_pressed:
                key_pressed = True
                crewmember_copy['crew_type'] = CREW_MEDICAL
                break
        elif keyboard.is_pressed('3'):
            if not key_pressed:
                key_pressed = True
                crewmember_copy['crew_type'] = CREW_SCIENCE
                break
        elif keyboard.is_pressed('4'):
            if not key_pressed:
                key_pressed = True
                crewmember_copy['crew_type'] = CREW_ENGINEERING
                break
        else:
            key_pressed = False
            
    return crewmember_copy

def reroll_crew(crew, crewmember):
    """
    Rerolls the crew type of a crewmember and updates the crew list accordingly.
    
    Args:
        crew (list): The list of crewmembers.
        crewmember (dict): The crewmember whose crew type is to be rerolled.
        
    Returns:
        list: The updated list of crewmembers.
    """
    crewmember['blocked'] = True

    crew_copy = crew.copy()

    for member in crew_copy:
        if member['infirmary'] == False and member['blocked'] == False:
                member['crew_type'] = random.choice([CREW_COMMANDER, CREW_TACTICAL, CREW_MEDICAL, CREW_SCIENCE, CREW_ENGINEERING, CREW_SCANNER])
    return crew_copy

def assign_crew_threat(crewmember, active_threats, crew, health, shield):
    """
    Assigns a crewmember to an active threat and updates the active threats list accordingly.
    
    Args:
        crewmember (dict): The crewmember to be assigned.
        active_threats (list): List of active threats.
        crew (list): List of crewmembers.
        health (int): The current health value.
        shield (int): The current shield value.
        
    Returns:
        list: The updated list of active threats.
    """
    crewmember['blocked'] = True
    real_index = []
    fake_index = []
    assignable_string = ''
    i = 0

    active_threats_copy = active_threats.copy()

    if crewmember['crew_type'] == CREW_COMMANDER:
        name = 'Commander'
    elif crewmember['crew_type'] == CREW_TACTICAL:
        name = 'Tactical'
    elif crewmember['crew_type'] == CREW_MEDICAL:
        name = 'Medical'
    elif crewmember['crew_type'] == CREW_SCIENCE:
        name = 'Science'
    elif crewmember['crew_type'] == CREW_ENGINEERING:
        name = 'Engineering'

    for threat in active_threats:
        if len(threat['assigned_crew']) < len(threat['assignable_crew']) and crewmember['crew_type'] in threat['assignable_crew']:
            
            i += 1
            real_index.append(active_threats_copy.index(threat))
            fake_index.append(i)
            assignable_string += f"{str(i)}) {threat['name']}\n"
        
    #print_assign(health, shield, active_threats_copy, crew, 'Press (↵) to escape')
    print(f"Select the threat you want to assign the {name} to:\n{assignable_string}")
    
    while True:
        input = keyboard.read_event().name
        
        if input.isnumeric():
            if int(input) in fake_index:
                active_threats_copy[real_index[fake_index.index(int(input))]]['assigned_crew'].append(crewmember['crew_type'])
                break

        if input == 'enter':
            break
    
    return active_threats_copy

def external_threats(active_threats):
    """
    Iterates over the list of threats checking which of them are external ones.

    Args:
        active_threats (list): List of active threats.
    
    Returns:
        list containing the external threats.
    """
    external_threats = []
    for threat in active_threats:
        if threat['health'] != 15:
            external_threats.append(threat)
    return external_threats

def attack_threat(active_threats, first_attack):
    """
    Shows the different external threats that can be attacked and attacks the threat choosen by the user.

    Args:
        active_threats (list): List of active threats.
    
    Returns:
        list of active threats with the corresponding modifications
    """
    active_threats_copy = active_threats.copy()

    external_threats_options = ''
    for i in range(len(active_threats_copy)):
        if active_threats_copy[i]['health'] != 15:
            external_threats_options += str(i+1) + ') Name: ' + active_threats_copy[i]['name'] + '; Health: ' + str(active_threats_copy[i]['health']) + '\n'
    
    print('Which threat do you want to attack?\n')
    print(external_threats_options)

    time.sleep(0.1)
    
    key_pressed = True

    while True:

        input = keyboard.read_event().name

        if input.isnumeric() and int(input) < len(active_threats) and int(input) >= 0 and not key_pressed:
            key_pressed = True
            i = int(input) - 1
            if active_threats[i]['health'] == 15:
                    print('Choose an external threat')
            else:
                if not first_attack:
                    active_threats[i]['health'] -= 1
                    first_attack = True
                else:
                    active_threats[i]['health'] -= 2
                
                break
        else:
            key_pressed = False
            

    return active_threats_copy, first_attack

def are_infirmary(crew):
    """
    Iterates over the crew checking if any of them is in the infirmary.

    Args:
        crew (list): List of crewmates

    Return:
        boolean: True if any member of the crew is in the infirmary, otherwise false.
    """
    for crewmember in crew:
        if crewmember['infirmary'] == True:
            return True
    return False

def are_scanners(crew):
    """
    Iterates over the crew checking if there is any scanner.

    Args:
        crew (list): List of crewmates
    
    Return:
        boolean: True if there is any scanner in the crew, otherwise false.
    """
    for crewmate in crew:
        if crewmate['crew_type'] == CREW_SCANNER:
            return True
    return False

def stun_threat(active_threats):
    threat_stunned = False
    active_threats_list = ""

    for i in range(len(active_threats)):
        active_threats_list += str(i+1) + ") " + active_threats[i]["name"] + "\n"

    print('Select the threat you want to stun:\n')
    print(active_threats_list)  

    time.sleep(0.1) 

    while True:
        for i in range(len(active_threats)):
            if keyboard.is_pressed(str(i+1)):
                if not threat_stunned:
                    active_threats[i]["stun"] = True
                    threat_stunned = True
                    break
        if threat_stunned:
            break

    return active_threats

def show_options(crewmember, crew, active_threats, health, shield, first_attack, hull_repaired_in_turn = False):
    """
    Displays options for a crewmember based on their crew type.
    
    Args:
        crewmember (dict): The crewmember for whom options are displayed.
        crew (list): List of all crewmembers.
        active_threats (list): List of active threats.
        health (int): The current health value.
        shield (int): The current shield value.
        
    Returns:
        tuple: A tuple containing the updated crew, active threats, health and shield values.
    """
    crew_copy = crew.copy()
    active_threats_copy = active_threats.copy()

    if crewmember['crew_type'] == CREW_COMMANDER:
        
        clear_terminal()
        print_assign(health, shield, active_threats, crew, 'Press (↵) to exit the menu', message_2='')
        message_options = 'COMMANDER options: \n\n1) Change face of any dice.\n\n2) Reroll dices\n\n3) Assign commander\n'

        print(message_options)

        key_pressed = True
        key_pressed2 = True
        
        time.sleep(0.1)
        
        while True:

            if keyboard.is_pressed('1'):
                if not key_pressed:
                    key_pressed = True

                    crew_options = crew_status(crew)
                    print(crew_options)
                    print('Select the crew member you want to change the face of the dice.\n')
                    
                    time.sleep(0.1)

                    while True:
                        if keyboard.is_pressed('1'):
                            if not key_pressed2:
                                key_pressed2 = True

                                if crew_copy[0]['blocked'] == False and crew_copy[0]['infirmary'] == False:
                                    crew_copy[0] = change_face(crew_copy[0])
                                    break
                                else:
                                    print('Choose a valid option')

                        if keyboard.is_pressed('2'):
                            if not key_pressed2:
                                key_pressed2 = True

                                if crew_copy[1]['blocked'] == False and crew_copy[1]['infirmary'] == False:
                                    crew_copy[1] = change_face(crew_copy[1])
                                    break
                                else:
                                    print('Choose a valid option')

                        if keyboard.is_pressed('3'):
                            if not key_pressed2:
                                key_pressed2 = True

                                if crew_copy[2]['blocked'] == False and crew_copy[2]['infirmary'] == False:
                                    crew_copy[2] = change_face(crew_copy[2])
                                    break
                                else:
                                    print('Choose a valid option')

                        if keyboard.is_pressed('4'):
                            if not key_pressed2:
                                key_pressed2 = True

                                if crew_copy[3]['blocked'] == False and crew_copy[3]['infirmary'] == False:
                                    crew_copy[3] = change_face(crew_copy[3])
                                    break
                                else:
                                    print('Choose a valid option')

                        if keyboard.is_pressed('5'):
                            if not key_pressed2:
                                key_pressed2 = True

                                if crew_copy[4]['blocked'] == False and crew_copy[4]['infirmary'] == False:
                                    crew_copy[4] = change_face(crew_copy[4])
                                    break
                                else:
                                    print('Choose a valid option')

                        if keyboard.is_pressed('6'):
                            if not key_pressed2:
                                key_pressed2 = True

                                if crew_copy[5]['blocked'] == False and crew_copy[5]['infirmary'] == False:
                                    crew_copy[5] = change_face(crew_copy[5])
                                    break
                                else:
                                    print('Choose a valid option')
                        
                        else:
                            key_pressed2 = False
                    
                    break
            
            elif keyboard.is_pressed('2'):
                if not key_pressed:
                    key_pressed = True
                    crew_copy = reroll_crew(crew_copy, crewmember)

                    break
            
            elif keyboard.is_pressed('3'):
                if not key_pressed:
                    key_pressed = True

                    active_threats_copy = assign_crew_threat(crewmember, active_threats_copy, crew_copy, health, shield)

                    break

            elif keyboard.is_pressed('enter'):
                break

            else:
                key_pressed = False

        return crew_copy, active_threats_copy, health, shield, first_attack, hull_repaired_in_turn

    if crewmember['crew_type'] == CREW_TACTICAL:
        clear_terminal()
        print_assign(health, shield, active_threats, crew, 'Press (↵) to exit the menu', message_2='')
        message_options = 'TACTICAL options: \n\n1) Attack external threat.\n\n2) Assign tactical.\n'

        print(message_options)

        key_pressed = True
        key_pressed2 = True
        
        time.sleep(0.1)

        while True:
            if keyboard.is_pressed('1'):
                if not key_pressed:
                    key_pressed = True
                    if len(external_threats(active_threats_copy)) == 0:
                        print('There are no external threats to be attacked, choose another option.')
                    else:
                        active_threats_copy, first_attack = attack_threat(active_threats_copy, first_attack)
                    break

            elif keyboard.is_pressed('2'):
                if not key_pressed:
                    key_pressed = True
                    active_threats_copy = assign_crew_threat(crewmember, active_threats_copy, crew_copy, health, shield)
                    break

            elif keyboard.is_pressed('enter'):
                break

            else:
                key_pressed = False

        return crew_copy, active_threats_copy, health, shield, first_attack, hull_repaired_in_turn 

    if crewmember['crew_type'] == CREW_MEDICAL:
        clear_terminal()
        print_assign(health, shield, active_threats, crew, 'Press (↵) to exit the menu', message_2='')
        message_options = 'MEDICAL options: \n\n1) Recover crew members in the infirmary.\n\n2) Assign medical.\n\n3) Recover one scanner.\n'

        print(message_options)

        key_pressed = True
        key_pressed2 = True

        time.sleep(0.1)

        while True:
            if keyboard.is_pressed('1'):
                if not key_pressed:

                    key_pressed = True

                    if not are_infirmary(crew_copy):
                        print('There is no crew in the infirmary, choose another option')

                    else:
                        for crewmember in crew_copy:
                            if crewmember['infirmary'] == True:
                                crewmember['infirmary'] == False
                        break
                    break

            elif keyboard.is_pressed('2'):
                if not key_pressed:
                    key_pressed = True
                    active_threats_copy = assign_crew_threat(crewmember, active_threats_copy, crew_copy, health, shield)
                    break

            elif keyboard.is_pressed('3'):
                if not key_pressed:
                    key_pressed = True

                    if not are_scanners(crew_copy):
                        # Check if there is, at least, one scanner in the crew.
                        print('There are no scanners, choose another option')
                    
                    else:
                        for crewmate in crew_copy:
                            if crewmate['crew_type'] == CREW_SCANNER:
                                crewmate['crew_type'] = NONE
                                break
                    break

            elif keyboard.is_pressed('enter'):
                break

            else:
                key_pressed = False

        return crew_copy, active_threats_copy, health, shield, first_attack, hull_repaired_in_turn
    
    if crewmember['crew_type'] == CREW_SCIENCE:
        
        clear_terminal()
        print_assign(health, shield, active_threats, crew, 'Press (↵) to exit the menu', message_2='')
        message_options = 'SCIENCE options: \n\n1) Fire Stasis Beam\n\n2) Recharge shields\n\n3) Assign science\n'

        print(message_options)

        key_pressed = False
        key_pressed2 = True

        time.sleep(0.1)

        while True:
            if keyboard.is_pressed('1'):
                if not key_pressed:
                    key_pressed = True
                    active_threats_copy = stun_threat(active_threats_copy)
                    break
            
            elif keyboard.is_pressed('2'):
                if not key_pressed:
                    key_pressed = True
                    shield = 4
                    break

            elif keyboard.is_pressed('3'):
                if not key_pressed:
                    key_pressed = True
                    active_threats_copy = assign_crew_threat(crewmember, active_threats_copy, crew_copy, health, shield)
                    break

            elif keyboard.is_pressed('enter'):
                break

            else:
                key_pressed = False

        return crew_copy, active_threats_copy, health, shield, first_attack, hull_repaired_in_turn
    
    if crewmember['crew_type'] == CREW_ENGINEERING:

        clear_terminal()
        print_assign(health, shield, active_threats, crew, 'Press (↵) to exit the menu', message_2='')
        message_options = 'ENGINEERING options: \n\n1) Repair the hull\n\n2) Assign engineer\n'

        print(message_options)

        key_pressed = True

        hull_repaired_in_turn = False

        time.sleep(0.1)

        while True:
            if keyboard.is_pressed('1'):
                if not key_pressed:
                    key_pressed = True
                    if not hull_repaired_in_turn:
                        health += 1
                        hull_repaired_in_turn = True
                    elif hull_repaired_in_turn:
                        health += 2
                    break

            elif keyboard.is_pressed('2'):
                if not key_pressed:
                    key_pressed = True
                    active_threats_copy = assign_crew_threat(crewmember, active_threats_copy, crew_copy, health, shield)
                    break

            elif keyboard.is_pressed('enter'):
                break

            else:
                key_pressed = False

        return crew_copy, active_threats_copy, health, shield, first_attack, hull_repaired_in_turn

def crew_status(crew):
    """
    Generates a message with the status of each crewmate.
    
    Args:
        crew (list): List of crewmates.
        
    Returns:
        tuple: A tuple containing the list of active crewmates and the status message.
    """

    crew_names = ['COMMANDER', 'TACTICAL', 'MEDICAL', 'SCIENTIFIC', 'ENGINEER', 'SCANNER', 'EMPTY']

    message = ''

    for crewmate in crew:

        if crewmate['blocked'] == False and crewmate['infirmary'] == False:
            # looking for the unblocked crewmates to add them to the message and to an array of active crew
            for i in range(len(crew_names)):
                if i == crewmate['crew_type']:
                    message += crew_names[i] + ' (' + str(crew.index(crewmate)+1) + ')   '

        if crewmate['blocked'] == True:
            # looking for the blocked crewmates and adding them to the message indicating they are doing some stuff
            for i in range(len(crew_names)):
                if i == crewmate['crew_type']:
                    message += crew_names[i] + ' (BLOCKED)   '
        
        if crewmate['infirmary'] == True:
            # looking for the injured crewmates and adding them to the message indicating they are injured
            for i in range(len(crew_names)):
                if i == crewmate['crew_type']:
                    message += crew_names[i] + ' (INFIRMARY)   '
        
    return message

def print_assign(health, shield, active_threats, crew_copy, message_to_continue, dice_number=' ', message_2 = '\nPress [1,2,3...] respectively to interact with the crew member.\n\n'):

    clear_terminal()
    print_interface(health, shield, active_threats, crew_copy, message_to_continue)
    message = crew_status(crew_copy)
    message += message_2
    print(message)

# COMPLEX FUNCTION,behaviour described in its appearance in the running loop, I think it's better to understand if you see it there
# Ayuda
def assign_crew(crew, active_threats, health, shield):
    """
    Assigns crew members to interact with threats based on user input.
    
    Args:
        crew (list): List of crewmates.
        active_threats (list): List of active threats.
        health (int): Current health value.
        shield (int): Current shield value.
    """
    crew_copy = crew.copy()

    active_threats_copy = active_threats.copy()

    print_assign(health, shield, active_threats_copy, crew_copy, 'Press (↵) to escape')

    key_pressed = False
    
    crew_action_1 = False
    crew_action_2 = False
    crew_action_3 = False
    crew_action_4 = False
    crew_action_5 = False
    crew_action_6 = False

    first_attack = False

    time.sleep(0.1)

    while not keyboard.is_pressed('enter'):

        if keyboard.is_pressed('1'):
            if not key_pressed:

                if crew_action_1:
                    key_pressed = True
                    print('You have already interacted with this crew member')

                elif crew_copy[0]['blocked'] == False and crew_copy[0]['infirmary'] == False:
                    key_pressed = True
                    crew_action_1 = True
                    crew_copy, active_threats_copy, health, shield, first_attack, hull_repaired_in_turn = show_options(crew_copy[0], crew_copy, active_threats_copy, health, shield, first_attack)
                    print_assign(health, shield, active_threats_copy, crew_copy, 'Press (↵) to escape')

                else:
                    print('Choose a valid option')
                    key_pressed = True

        elif keyboard.is_pressed('2'):
            if not key_pressed:
                
                if crew_action_2:
                    key_pressed = True
                    print('You have already interacted with this crew member')

                elif crew_copy[1]['blocked'] == False and crew_copy[1]['infirmary'] == False:
                    key_pressed = True
                    crew_action_2 = True
                    crew_copy, active_threats_copy, health, shield, first_attack, hull_repaired_in_turn = show_options(crew_copy[1], crew_copy, active_threats_copy, health, shield, first_attack)
                    print_assign(health, shield, active_threats_copy, crew_copy, 'Press (↵) to escape')
                else:
                    print('Choose a valid option')
                    key_pressed = True
        
        elif keyboard.is_pressed('3'):
            if not key_pressed:
                
                if crew_action_3:
                    key_pressed = True
                    print('You have already interacted with this crew member')

                elif crew_copy[2]['blocked'] == False and crew_copy[2]['infirmary'] == False:
                    key_pressed = True
                    crew_action_3 = True
                    crew_copy, active_threats_copy, health, shield, first_attack, hull_repaired_in_turn = show_options(crew_copy[2], crew_copy, active_threats_copy, health, shield, first_attack)
                    print_assign(health, shield, active_threats_copy, crew_copy, 'Press (↵) to escape')
                else:
                    print('Choose a valid option')
                    key_pressed = True
        
        elif keyboard.is_pressed('4'):
            if not key_pressed:

                if crew_action_4:
                    key_pressed = True
                    print('You have already interacted with this crew member')

                elif crew_copy[3]['blocked'] == False and crew_copy[3]['infirmary'] == False:
                    key_pressed = True
                    crew_action_4 = True
                    crew_copy, active_threats_copy, health, shield, first_attack, hull_repaired_in_turn = show_options(crew_copy[3], crew_copy, active_threats_copy, health, shield, first_attack)
                    print_assign(health, shield, active_threats_copy, crew_copy, 'Press (↵) to escape')
                else:
                    print('Choose a valid option')
                    key_pressed = True
        
        elif keyboard.is_pressed('5'):
            if not key_pressed:

                if crew_action_5:
                    key_pressed = True
                    print('You have already interacted with this crew member')

                elif crew_copy[4]['blocked'] == False and crew_copy[4]['infirmary'] == False:
                    key_pressed = True
                    crew_action_5 = True
                    crew_copy, active_threats_copy, health, shield, first_attack, hull_repaired_in_turn = show_options(crew_copy[4], crew_copy, active_threats_copy, health, shield, first_attack)
                    print_assign(health, shield, active_threats_copy, crew_copy, 'Press (↵) to escape')
                else:
                    print('Choose a valid option')
                    key_pressed = True
        
        elif keyboard.is_pressed('6'):
            if not key_pressed:

                if crew_action_6:
                    key_pressed = True
                    print('You have already interacted with this crew member')

                elif crew_copy[5]['blocked'] == False and crew_copy[5]['infirmary'] == False:
                    key_pressed = True
                    crew_action_6 = True
                    crew_copy, active_threats_copy, health, shield, first_attack, hull_repaired_in_turn = show_options(crew_copy[5], crew_copy, active_threats_copy, health, shield, first_attack)
                    print_assign(health, shield, active_threats_copy, crew_copy, 'Press (↵) to escape')
                else:
                    print('Choose a valid option')
                    key_pressed = True

        else:
            key_pressed = False
        
    return crew_copy, active_threats_copy, health, shield