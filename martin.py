import random
import keyboard
import os
import time

CREW_COMMANDER = 0
CREW_TACTICAL = 1
CREW_MEDICAL = 2
CREW_SCIENCE = 3
CREW_ENGINEERING = 4
CREW_SCANNER = 5


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
            crewmember_copy['crew_type'] = CREW_TACTICAL
            break
        elif keyboard.is_pressed('2'):
            crewmember_copy['crew_type'] = CREW_MEDICAL
            break
        elif keyboard.is_pressed('3'):
            crewmember_copy['crew_type'] = CREW_SCIENCE
            break
        elif keyboard.is_pressed('4'):
            crewmember_copy['crew_type'] = CREW_ENGINEERING
            break

    return crewmember_copy

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

    if crewmember['crew_type'] == CREW_COMMANDER:
        
        clear_terminal()
        message_options = 'COMMANDER options: (Press *enter* to exit the menu) \n\n1) Change face of any dice.\n\n2) Reroll dices\n'

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

                    # I guess this is the part where we reroll the dices using get crew which hopefully will return the crew_copy with the changes made

                    break
            
            elif keyboard.is_pressed('enter'):
                break

            else:
                key_pressed = False

        return crew_copy, active_threats, health, shield

    if crewmember['crew_type'] == CREW_TACTICAL:
        return crew_copy, active_threats, health, shield
    if crewmember['crew_type'] == CREW_MEDICAL:
        return crew_copy, active_threats, health, shield
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

def print_assign(crew_copy):

    clear_terminal()
    # print_interface(health, shield, crew_copy, active_threats_copy, dice_number)
    message = crew_status(crew_copy)
    message += '\nPress [1,2,3...] respectively to interact with the crew member. (To escape press [enter] )\n\n'
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
    print_assign(crew_copy)

    key_pressed = False
    
    crew_action_1 = False
    crew_action_2 = False
    crew_action_3 = False
    crew_action_4 = False
    crew_action_5 = False
    crew_action_6 = False

    time.sleep(0.1)

    while not keyboard.is_pressed('c'):

        if keyboard.is_pressed('1'):
            if not key_pressed:

                if crew_action_1:
                    print('You have already interacted with this crew member')

                elif crew_copy[0]['blocked'] == False and crew_copy[0]['infirmary'] == False:
                    key_pressed = True
                    crew_action_1 = True
                    crew_copy, active_threats_copy, health, shield = show_options(crew_copy[0], crew_copy, active_threats_copy, health, shield)
                    print_assign(crew_copy)

                else:
                    print('Choose a valid option')
                    key_pressed = True

        elif keyboard.is_pressed('2'):
            if not key_pressed:
                
                if crew_action_2:
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
    
def main():
    """
    Test functionality.
    """
    # Initialize variables
    health = 8
    shield = 4
    crew = [
        {'crew_type': CREW_COMMANDER, 'blocked': False, 'infirmary': False},
        {'crew_type': CREW_TACTICAL, 'blocked': False, 'infirmary': False},
        {'crew_type': CREW_MEDICAL, 'blocked': False, 'infirmary': False},
        {'crew_type': CREW_SCIENCE, 'blocked': False, 'infirmary': False},
        {'crew_type': CREW_ENGINEERING, 'blocked': False, 'infirmary': False},
        {'crew_type': CREW_SCANNER, 'blocked': False, 'infirmary': False}]
    active_threats = [{'name': 'Hijackers', 'description': '-2 Hull', 'dice_numbers': [4,5], 'health': 4, 'attack': '1NM', 'volatility': False, 'assignable_crew': [0, 0, 1], 
                'assigned_crew': [], 'block_till_complete': [], 'send_infirmary': False, 'mercenary': False, 'existentialism': [False], 'return_scanner': False, 'stun': False, 'tactical_to_infirmary': False}]
    
    assign_crew(crew, active_threats, health, shield)

if __name__ == '__main__':
    main()