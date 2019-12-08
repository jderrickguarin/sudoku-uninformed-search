import string

def get_key(dictionary, val): 
    for key, value in dictionary.items(): 
         if val == value: 
             return key 
  
    return "Error: key doesn't exist"

def dots_spaces(lettergrid):
    for row in range(len(lettergrid)):
        for column in range(len(lettergrid)):
            if lettergrid[row][column] == '.':
                return True
            elif lettergrid[row][column] == ' ':
                return False

def to_numbers(lettergrid):

    gridSize = len(lettergrid) + 1
    numKeys = [num for num in range(1,gridSize)]
    letterValues = list(map(chr, range(ord('A'), ord('A')+gridSize)))
    alphanumDict = dict(zip(numKeys, letterValues))
    if dots_spaces(lettergrid) == True:
        alphanumDict[0] = '.'
    elif dots_spaces(lettergrid) == False:
        alphanumDict[0] = ' '

    numbergrid = [[] for new_list in range(len(lettergrid))]
    # numbergrid = []
    blanklist = []
    for row in range(len(lettergrid)):
        for column in range(len(lettergrid)):
            blanklist.append(get_key(alphanumDict, lettergrid[row][column]))
        numbergrid[row].extend(blanklist)
        blanklist.clear()
    return numbergrid

sample = [['D','A','.','.','.','G','.','.','E'],
        ['.','.','C','B','.','I','.','.','H'],
        ['.','.','H','.','E','A','I','D','.'],
        ['F','C','E','.','.','.','.','G','.'],
        ['.','.','B','.','.','.','A','.','.'],
        ['.','D','.','.','.','.','H','E','B'],
        ['.','I','D','G','C','.','F','.','.'],
        ['C','.','.','D','.','F','B','.','.'],
        ['H','.','.','I','.','.','.','C','D']]

print(to_numbers(sample))