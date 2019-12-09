import copy
import time
from letters_transform import to_letters, to_numbers, check_if_letters

class Problem(object):

    def __init__(self, initial):
        self.initial = initial
        self.size = len(initial) # Size of grid
        self.height = int(self.size/3) # Size of a quadrant

    def check_legal(self, state):
        # Maximum sum of row, column or quadrant
        exp_sum = sum(range(1, self.size+1))

        # Returns false if expected sum of row or column are invalid
        for row in range(self.size):
            if (len(state[row]) != self.size) or (sum(state[row]) != exp_sum):
                return False
            column_sum = 0
            for column in range(self.size):
                column_sum += state[column][row]
            if (column_sum != exp_sum):
                return False

        # Returns false if expected sum of a quadrant is invalid
        for column in range(0,self.size,3):
            for row in range(0,self.size,self.height):
                block_sum = 0
                for block_row in range(0,self.height):
                    for block_column in range(0,3):
                        block_sum += state[row + block_row][column + block_column]

                if (block_sum != exp_sum):
                    return False
        return True

    # Return set of valid numbers from values that do not appear in used
    def filter_values(self, values, used):
        return [number for number in values if number not in used]

    # Return empty spot on grid with most constraints (least amount of options)
    def get_spot(self, board, state):
        target_option_len = board
        row = 0
        while row < board:
            column = 0
            while column < board:
                if state[row][column] == 0:
                    options = self.filter_row(state, row)
                    options = self.filter_col(options, state, column)
                    options = self.filter_quad(options, state, row, column)
                    if len(options) < target_option_len:
                        target_option_len = len(options)
                        options = []
                        spotrow = row
                        spotcol = column
                column = column + 1
            row = row + 1                
        return spotrow, spotcol

    # Filter valid values based on row
    def filter_row(self, state, row):
        number_set = range(1, self.size+1) # Defines set of valid numbers that can be placed on board
        in_row = [number for number in state[row] if (number != 0)]
        options = self.filter_values(number_set, in_row)
        return options

    # Filter valid values based on column
    def filter_col(self, options, state, column):
        in_column = []
        for column_index in range(self.size):
            if state[column_index][column] != 0:
                in_column.append(state[column_index][column])
        options = self.filter_values(options, in_column)
        return options

    # Filter valid values based on quadrant
    def filter_quad(self, options, state, row, column):
        in_block = [] # List of valid values in spot's quadrant
        row_start = int(row/self.height)*self.height
        column_start = int(column/3)*3
        
        for block_row in range(0, self.height):
            for block_column in range(0,3):
                in_block.append(state[row_start + block_row][column_start + block_column])
        options = self.filter_values(options, in_block)
        return options    

    def actions(self, state):
        row,column = self.get_spot(self.size, state) # Get first empty spot on board

        # Remove a square's invalid values
        options = self.filter_row(state, row)
        options = self.filter_col(options, state, column)
        options = self.filter_quad(options, state, row, column)

        # Return a state for each valid option (yields multiple states)
        for number in options:
            new_state = copy.deepcopy(state) # Norvig used only shallow copy to copy states; deepcopy works like a perfect clone of the original
            new_state[row][column] = number
            yield new_state

class Node:
    
    def __init__(self, state):
        self.state = state

    def expand(self, problem):
        # Return list of valid states
        return [Node(state) for state in problem.actions(self.state)]

def DFS(problem):
    start = Node(problem.initial)
    if problem.check_legal(start.state):
        return start.state

    stack = []
    stack.append(start) # Places the root node on the stack

    while stack: 
        node = stack.pop() # Pops the last node, tests legality, then expands the same popped node
        if problem.check_legal(node.state):
            return node.state
        stack.extend(node.expand(problem)) 
    return None

def H_Solve(board):
    print ("\nSolving with DFS and heuristics...")
    letters = False
    if check_if_letters(board): # Checks of the board contains letters instead of numbers
        board = to_numbers(board) # Transforms letter puzzles to numeric puzzles
        letters = True

    start_time = time.time()
    problem = Problem(board)
    solution = DFS(problem)
    elapsed_time = time.time() - start_time

    if solution:
        if letters:
            solution = to_letters(solution) # Transforms back numeric puzzles to original letter puzzle type of true
        print ("Found solution")
        for row in solution:
            print (row)
    else:
        print ("No possible solutions")

    print ("Elapsed time: " + str(elapsed_time) + " seconds")
