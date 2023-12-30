import random
import keyboard
import os
import time
import izan as zn
import add_threats as at

CREW_COMMANDER = 0
CREW_TACTICAL = 1
CREW_MEDICAL = 2
CREW_SCIENCE = 3
CREW_ENGINEERING = 4
CREW_SCANNER = 5
NONE = 6


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

def gather_crew(crew):
    """
    Counts the number of unblocked crewmates.
    
    Args:
        crew (list): List of crewmates.
        
    Returns:
        int: The number of unblocked crewmates.
    """
    crew_to_roll = 0
    for crewmate in crew:
        if not crewmate['blocked']:
            crew_to_roll += 1
    return crew_to_roll

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

def attack_threat(active_threats):
    """
    Shows the different external threats that can be attacked and attacks the threat choosen by the user.

    Args:
        active_threats (list): List of active threats.
    
    Returns:
        list of active threats with the corresponding modifications
    """
    threat_attacked = False
    external_threats_options = ''
    for i in len(active_threats):
        if active_threats[i]['health'] != 15:
            external_threats_options += str(i+1) + ') Name: ' + active_threats[i]['name'] + '; Health: ' + active_threats[i]['health'] + '\n'
    
    print('Which threat do you want to attack?')
    print(external_threats_options)

    while True:
        for i in range(len(active_threats)):
            if keyboard.is_pressed(str(i+1)):
                if active_threats[i]['health'] == 15:
                    break
                else:
                    active_threats[i]['health'] -= 1
                    threat_attacked = True
                    break
        if threat_attacked:
            break
        else:
            print('Choose a valid option')

    return active_threats

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
    for crewmember in crew:
        if crewmember['type'] == CREW_SCANNER:
            return True
    return False

def show_options(crewmember, crew, active_threats, health, shield):
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

        return crew_copy, active_threats_copy, health, shield

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
                        active_threats_copy = attack_threat(active_threats_copy)
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

        return crew_copy, active_threats_copy, health, shield

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
                        for crewmate in crew:
                            if crewmate['type'] == CREW_SCANNER:
                                crewmate['type'] == NONE
                                break
                    break

            elif keyboard.is_pressed('enter'):
                break

            else:
                key_pressed = False

        return crew_copy, active_threats_copy, health, shield
    
    if crewmember['crew_type'] == CREW_SCIENCE:
        return crew_copy, active_threats, health, shield
    if crewmember['crew_type'] == CREW_ENGINEERING:
        return crew_copy, active_threats, health, shield

def crew_status(crew):
    """
    Generates a message with the status of each crewmate.
    
    Args:
        crew (list): List of crewmates.
        
    Returns:
        tuple: A tuple containing the list of active crewmates and the status message.
    """

    crew_names = ['COMMANDER', 'TACTICAL', 'MEDICAL', 'SCIENTIFIC', 'ENGINEER', 'SCANNER']

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
    zn.print_interface(health, shield, active_threats, crew_copy, message_to_continue)
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
                    crew_copy, active_threats_copy, health, shield = show_options(crew_copy[0], crew_copy, active_threats_copy, health, shield)
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
                    crew_copy, active_threats_copy, health, shield = show_options(crew_copy[1], crew_copy, active_threats_copy, health, shield)
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
                    crew_copy, active_threats_copy, health, shield = show_options(crew_copy[2], crew_copy, active_threats_copy, health, shield)
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
                    crew_copy, active_threats_copy, health, shield = show_options(crew_copy[3], crew_copy, active_threats_copy, health, shield)
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
                    crew_copy, active_threats_copy, health, shield = show_options(crew_copy[4], crew_copy, active_threats_copy, health, shield)
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
                    crew_copy, active_threats_copy, health, shield = show_options(crew_copy[5], crew_copy, active_threats_copy, health, shield)
                else:
                    print('Choose a valid option')
                    key_pressed = True

        else:
            key_pressed = False
        
    return crew_copy, active_threats_copy, health, shield
    
def main():
    """
    Test functionality.
    """
    # Initialize variables
    health = 8
    shield = 1
    crew = [
        {'crew_type': CREW_COMMANDER, 'blocked': False, 'infirmary': False},
        {'crew_type': CREW_TACTICAL, 'blocked': False, 'infirmary': False},
        {'crew_type': CREW_MEDICAL, 'blocked': False, 'infirmary': False},
        {'crew_type': CREW_SCIENCE, 'blocked': False, 'infirmary': False},
        {'crew_type': CREW_ENGINEERING, 'blocked': False, 'infirmary': False},
        {'crew_type': CREW_SCANNER, 'blocked': True, 'infirmary': False}]
    active_threats = [{'name': 'Hijackers', 'description': '-2 Hull', 'dice_numbers': [4,5], 'health': 4, 'attack': '1NM', 'volatility': False, 'assignable_crew': [0, 0, 1], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stun': False, 'tactical_to_infirmary': False}]
    
    assign_crew(crew, active_threats, health, shield)

if __name__ == '__main__':
    main()