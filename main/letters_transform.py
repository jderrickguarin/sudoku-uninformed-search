import string

def get_key(dictionary, val): 
    for key, value in dictionary.items(): 
         if val == value: 
             return key 
  
    return "Error: key doesn't exist"

def get_val(dictionary, k):
    for key, value in dictionary.items():
        if k == key:
            return value

    return "Error: value doesn't exist"

def dots_spaces(lettergrid):
    for row in range(len(lettergrid)):
        for column in range(len(lettergrid)):
            if lettergrid[row][column] == '.':
                return True
            elif lettergrid[row][column] == ' ':
                return False

def check_if_letters(grid):
    for row in range(len(grid)):
        for column in range(len(grid)):
            if isinstance(grid[row][column],str):
                return True 
            #else:
                #return False

def to_numbers(lettergrid):

    gridSize = len(lettergrid)
    numKeys = [num for num in range(1,gridSize+1)]
    letterValues = list(map(chr, range(ord('A'), ord('A')+gridSize+1)))
    alphanumDict = dict(zip(numKeys, letterValues))
    if dots_spaces(lettergrid) == True:
        alphanumDict[0] = '.'
    elif dots_spaces(lettergrid) == False:
        alphanumDict[0] = ' '

    numbergrid = [[] for new_list in range(gridSize)]    
    blanklist = []
    for row in range(gridSize):
        for column in range(gridSize):
            blanklist.append(get_key(alphanumDict, lettergrid[row][column]))
        numbergrid[row].extend(blanklist)
        blanklist.clear()
    return numbergrid

def to_letters(numbergrid):
    
    gridSize = len(numbergrid)
    numKeys = [num for num in range(1,gridSize+1)]
    letterValues = list(map(chr, range(ord('A'), ord('A')+gridSize+1)))
    alphanumDict = dict(zip(numKeys, letterValues))
    alphanumDict[0] = '.'

    lettergrid = [[] for new_list in range(gridSize)]
    blanklist = []
    for row in range(gridSize):
        for column in range(gridSize):
            blanklist.append(get_val(alphanumDict, numbergrid[row][column]))
        lettergrid[row].extend(blanklist)
        blanklist.clear()
    return lettergrid

