import copy
import time

class Problem(object):

    def __init__(self, initial):
        self.initial = initial
        self.type = len(initial) # Defines board type, either 6x6 or 9x9
        self.height = int(self.type/3) # Defines height of quadrant (2 for 6x6, 3 for 9x9)

    def goal_test(self, state):
        # Expected sum of each row, column or quadrant.
        total = sum(range(1, self.type+1))

        # Check rows and columns and return false if total is invalid
        for row in range(self.type):
            if (len(state[row]) != self.type) or (sum(state[row]) != total):
                return False

            column_total = 0
            for column in range(self.type):
                column_total += state[column][row]

            if (column_total != total):
                return False

        # Check quadrants and return false if total is invalid
        for column in range(0,self.type,3):
            for row in range(0,self.type,self.height):

                block_total = 0
                for block_row in range(0,self.height):
                    for block_column in range(0,3):
                        block_total += state[row + block_row][column + block_column]

                if (block_total != total):
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
        number_set = range(1, self.type+1) # Defines set of valid numbers that can be placed on board
        in_row = [number for number in state[row] if (number != 0)]
        options = self.filter_values(number_set, in_row)
        return options

    # Filter valid values based on column
    def filter_col(self, options, state, column):
        in_column = [] # List of valid values in spot's column
        for column_index in range(self.type):
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
        row,column = self.get_spot(self.type, state) # Get first empty spot on board

        # Remove spot's invalid options
        options = self.filter_row(state, row)
        options = self.filter_col(options, state, column)
        options = self.filter_quad(options, state, row, column)

        # Yield a state for each valid option
        for number in options:
            new_state = copy.deepcopy(state)
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
    if problem.goal_test(start.state):
        return start.state

    stack = []
    stack.append(start) # Place initial node onto the stack

    while stack: 
        node = stack.pop() # Pops the last node, tests legality, then expands the same popped node
        if problem.goal_test(node.state):
            return node.state
        stack.extend(node.expand(problem)) 
    return None

def HSolve(board):
    print ("\nSolving with DFS and heuristics...")
    start_time = time.time()
    problem = Problem(board)
    solution = DFS(problem)
    elapsed_time = time.time() - start_time

    if solution:
        print ("Found solution")
        for row in solution:
            print (row)
    else:
        print ("No possible solutions")

    print ("Elapsed time: " + str(elapsed_time))
