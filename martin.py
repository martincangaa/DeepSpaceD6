import random
import keyboard
import os

CREW_COMMANDER = 0
CREW_TACTICAL = 1
CREW_MEDICAL = 2
CREW_SCIENCE = 3
CREW_ENGINEERING = 4
CREW_SCANNER = 5

crew = [{"crew_type":0, "blocked": False, "infirmary": False},{"crew_type":0, "blocked": True, "infirmary": False},{"crew_type":1, "blocked": True, "infirmary": False},{"crew_type":2, "blocked": True, "infirmary": False},{"crew_type":3, "blocked": True, "infirmary": False},{"crew_type":4, "blocked": True, "infirmary": False}]

health = 8
shield = 4

active_threats = []

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
    
    while True:
        if keyboard.is_pressed('1'):
            crewmember_copy['crew_type'] = CREW_TACTICAL
            break
        if keyboard.is_pressed('2'):
            crewmember_copy['crew_type'] = CREW_MEDICAL
            break
        if keyboard.is_pressed('3'):
            crewmember_copy['crew_type'] = CREW_SCIENCE
            break
        if keyboard.is_pressed('4'):
            crewmember_copy['crew_type'] = CREW_ENGINEERING
            break
        else:
            print('Choose a valid option')
    
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
        message_options = 'COMMANDER options: (Press *C* to exit the menu) \n\n1) Change face of any dice.\n\n2) Reroll dices\n'

        print(message_options)

        key_pressed = False

        while not keyboard.is_pressed('c'):

            if keyboard.is_pressed('1') and not key_pressed:
                
                key_pressed = True

                crew_options = crew_status(crew)
                print(crew_options)
                print('Select the crew member you want to change the face of the dice.\n')

                while True:
                    if keyboard.is_pressed('1'):
                        if crew_copy[0]['blocked'] == False and crew_copy[0]['infirmary'] == False:
                            crew_copy[0] = change_face(crew_copy[0])
                            break
                        else:
                            print('Choose a valid option')
                    
                    if keyboard.is_pressed('2'):
                        if crew_copy[1]['blocked'] == False and crew_copy[1]['infirmary'] == False:
                            crew_copy[1] = change_face(crew_copy[1])
                            break
                        else:
                            print('Choose a valid option')

                    if keyboard.is_pressed('3'):
                        if crew_copy[2]['blocked'] == False and crew_copy[2]['infirmary'] == False:
                            crew_copy[2] = change_face(crew_copy[2])
                            break
                        else:
                            print('Choose a valid option')
                    
                    if keyboard.is_pressed('4'):
                        if crew_copy[3]['blocked'] == False and crew_copy[3]['infirmary'] == False:
                            crew_copy[3] = change_face(crew_copy[3])
                            break
                        else:
                            print('Choose a valid option')
                    
                    if keyboard.is_pressed('5'):
                        if crew_copy[4]['blocked'] == False and crew_copy[4]['infirmary'] == False:
                            crew_copy[4] = change_face(crew_copy[4])
                            break
                        else:
                            print('Choose a valid option')
                    
                    if keyboard.is_pressed('6'):
                        if crew_copy[5]['blocked'] == False and crew_copy[5]['infirmary'] == False:
                            crew_copy[5] = change_face(crew_copy[5])
                            break
                        else:
                            print('Choose a valid option')

                break

            
            if keyboard.is_pressed('2') and not key_pressed:
                
                key_pressed = True

                # I guess this is the part where we reroll the dices using get crew which hopefully will return the crew_copy with the changes made

                break
            else:
                key_pressed = False


    if crewmember['crew_type'] == CREW_TACTICAL:
        pass
    if crewmember['crew_type'] == CREW_MEDICAL:
        pass
    if crewmember['crew_type'] == CREW_SCIENCE:
        pass
    if crewmember['crew_type'] == CREW_ENGINEERING:
        pass

def crew_status(crew):
    """
    Generates a message with the status of each crewmate.
    
    Args:
        crew (list): List of crewmates.
        
    Returns:
        tuple: A tuple containing the list of active crewmates and the status message.
    """

    crew_names = ['COMMANDER', 'TACTICAL', 'MEDICAL', 'SCIENCE', 'ENGINEER', 'SCANNER']

    message = ''

    for crewmate in crew:

        if crewmate['blocked'] == False and crewmate['infirmary'] == False:
            # looking for the unblocked crewmates to add them to the message and to an array of active crew
            for i in range(len(crew_names)):
                if i == crewmate['crew_type']:
                    message += crew_names[i] + ' (' + str(i) + ')   '

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
    message = crew_status(crew_copy)

    active_threats_copy = active_threats.copy()

    message += '\nPress [1,2,3...] respectively to interact with the crew member. (To escape press [c] )\n\n'
    print(message)

    key_pressed = False

    while not keyboard.is_pressed('c'):

        if keyboard.is_pressed('1') and not key_pressed:
            if crew_copy[0]['blocked'] == False and crew_copy[0]['infirmary'] == False:
                key_pressed = True
                crew_copy, active_threats_copy, health, shield = show_options(crew_copy[0], crew_copy, active_threats_copy, health, shield)
            else:
                print('Choose a valid option')
                key_pressed = True

        if keyboard.is_pressed('2') and key_pressed:
            if crew_copy[1]['blocked'] == False and crew_copy[1]['infirmary'] == False:
                key_pressed = True
                crew_copy, active_threats_copy, health, shield = show_options(crew[1], crew_copy, active_threats_copy, health, shield)
            else:
                print('Choose a valid option')
                key_pressed = True
        
        if keyboard.is_pressed('3') and key_pressed:
            if crew_copy[2]['blocked'] == False and crew_copy[2]['infirmary'] == False:
                key_pressed = True
                crew_copy, active_threats_copy, health, shield = show_options(crew_copy[2], crew_copy, active_threats_copy, health, shield)
            else:
                print('Choose a valid option')
                key_pressed = True
        
        if keyboard.is_pressed('4') and key_pressed:
            if crew_copy[3]['blocked'] == False and crew_copy[3]['infirmary'] == False:
                key_pressed = True
                crew_copy, active_threats_copy, health, shield = show_options(crew_copy[3], crew_copy, active_threats_copy, health, shield)
            else:
                print('Choose a valid option')
                key_pressed = True
        
        if keyboard.is_pressed('5') and key_pressed:
            if crew_copy[4]['blocked'] == False and crew_copy[4]['infirmary'] == False:
                key_pressed = True
                crew_copy, active_threats_copy, health, shield = show_options(crew_copy[4], crew_copy, active_threats_copy, health, shield)
            else:
                print('Choose a valid option')
                key_pressed = True
        
        if keyboard.is_pressed('6') and key_pressed:
            if crew_copy[5]['blocked'] == False and crew_copy[5]['infirmary'] == False:
                key_pressed = True
                crew_copy, active_threats_copy, health, shield = show_options(crew_copy[5], crew_copy, active_threats_copy, health, shield)
            else:
                print('Choose a valid option')
                key_pressed = True

        else:
            key_pressed = False

def main():
    assign_crew(crew, active_threats, health, shield)

if __name__ == "__main__":
    main()