def write_difficulty(difficulty):
    """
    Write the difficulty level to a file.

    Args:
        difficulty (int): The difficulty level to be written.

    Returns:
        None
    """
    # Open the file in write mode
    f = open('difficulty', 'w')
    
    # Write the difficulty level as a string
    f.write(str(difficulty))
    
    # Close the file
    f.close()

def read_difficulty():
    """
    Reads the difficulty level from the 'difficulty' file and returns it.
    
    Returns:
        str: The difficulty level read from the file.
    """
    f = open('difficulty', "r")
    
    difficulty = f.readline().strip() 
    f.close()
    
    return difficulty