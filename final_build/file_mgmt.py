def write_difficulty(difficulty):
    f = open('difficulty', 'w')
    
    f.write(str(difficulty))
    f.close()

def read_difficulty():
    
    f = open('difficulty', "r")
    
    difficulty = f.readline().strip() 
    f.close()
    
    return difficulty