import random
import keyboard

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

def show_options(crewmember, crew, active_threats, message):
    """
    Displays options for a crewmember based on their crew type.
    
    Args:
        crewmember (dict): The crewmember for whom options are displayed.
        crew (list): List of all crewmembers.
        active_threats (list): List of active threats.
        message (str): The current message to be displayed.
        
    Returns:
        str: The updated message after displaying options.
    """
    if crewmember['crew_type'] == CREW_COMMANDER:
        message += 'COMMANDER options: \n\n1) Change face of any dice.\n\n2) Reroll dices'
        while not keyboard.is_pressed('c'):
            key_pressed = False
    if crewmember['crew_type'] == CREW_TACTICAL:
        pass
    if crewmember['crew_type'] == CREW_MEDICAL:
        pass
    if crewmember['crew_type'] == CREW_SCIENCE:
        pass
    if crewmember['crew_type'] == CREW_ENGINEERING:
        pass
    if crewmember['crew_type'] == CREW_TACTICAL:
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
    active_crew = []

    message = ''

    for crewmate in crew:

        if crewmate['blocked'] == False:
            # looking for the unblocked crewmates to add them to the message and to an array of active crew
            for i in range(len(crew_names)):
                if i == crewmate['crew_type']:
                    message += crew_names[i] + ' (' + i + ')   '
                    active_crew.append(crewmate)
        
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
        
    return active_crew, message

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
    active_crew, message = crew_status(crew)
    
    active_threats_copy = active_threats.copy()

    message += '\nPress [1,2,3...] respectively to interact with the crew member.\n\n'
    print(message)

    while keyboard.is_pressed('c') == False:

        key_pressed = False

        if keyboard.is_pressed('1') and key_pressed:
            try:
                message = show_options(active_crew[0], crew, active_threats_copy, message)
            finally:
                key_pressed = True
        
        if keyboard.is_pressed('2') and key_pressed:
            try:
                message = show_options(active_crew[1], active_threats_copy, message)
            finally:
                key_pressed = True
        
        if keyboard.is_pressed('3') and key_pressed:
            try:
                message = show_options(active_crew[2], active_threats_copy, message)
            finally:
                key_pressed = True
        
        if keyboard.is_pressed('4') and key_pressed:
            try:
                message = show_options(active_crew[3], active_threats_copy, message)
            finally:
                key_pressed = True
        
        if keyboard.is_pressed('5') and key_pressed:
            try:
                message = show_options(active_crew[4], active_threats_copy, message)
            finally:
                key_pressed = True
        
        if keyboard.is_pressed('6') and key_pressed:
            try:
                message = show_options(active_crew[5], active_threats_copy, message)
            finally:
                key_pressed = True

        else:
            key_pressed = False


