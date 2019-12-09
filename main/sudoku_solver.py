from BFS_Sudoku import BFS_solve
from DFS_Sudoku import DFS_solve
from Heuristics_Sudoku import H_Solve

print ("\n\nTesting on easy 6x6 grid...")
grid = [[6,0,0,0,0,0],
      [0,0,1,3,0,6],
      [0,0,4,0,0,0],
      [1,2,0,0,0,0],
      [0,0,0,0,0,4],
      [3,0,5,0,0,0]]

print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid)

print ("\n\nTesting on hard 6x6 grid...")
grid = [[0,0,0,3,0,0],
      [0,0,0,0,5,0],
      [0,0,3,0,0,0],
      [0,5,0,0,0,0],
      [6,0,0,5,4,0],
      [0,0,2,0,6,0]]

print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid)

print ("\n\nTesting on expert 6x6 grid...")
grid = [[0,3,0,1,0,0],
      [0,0,0,6,4,0],
      [0,0,5,0,2,0],
      [0,0,0,0,0,0],
      [4,0,0,0,0,0],
      [0,5,1,0,0,0]]


print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid)

print ("\n\nTesting on invalid 9x9 grid...")
grid = [[0,0,9,0,7,0,0,0,5],
      [0,0,2,1,0,0,9,0,0],
      [1,0,0,0,2,8,0,0,0],
      [0,7,0,0,0,5,0,0,1],
      [0,0,8,5,1,0,0,0,0],
      [0,5,0,0,0,0,3,0,0],
      [0,0,0,0,0,3,0,0,6],
      [8,0,0,0,0,0,0,0,0],
      [2,1,0,0,0,0,0,8,7]]

print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid)

print ("\n\nTesting on easy 9x9 grid...")
grid = [[0,0,7,2,8,0,0,0,0], 
      [0,0,0,0,0,0,5,0,6],
      [4,1,3,0,0,6,0,8,0],
      [7,2,0,3,9,0,0,0,0],
      [3,4,0,0,0,0,8,1,0],
      [6,8,0,1,0,7,0,0,2],
      [0,0,0,6,7,4,0,2,3],
      [0,0,0,0,0,5,7,0,0],
      [1,0,6,0,2,3,0,4,0]]

print ("Problem:")
for row in grid:
      print (row)
      
BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid)

print ("\n\nTesting on filled valid 9x9 grid...")
grid = [[9,7,4,2,3,6,1,5,8],
      [6,3,8,5,9,1,7,4,2],
      [1,2,5,4,8,7,9,3,6],
      [3,1,6,7,5,4,2,8,9],
      [7,4,2,9,1,8,5,6,3],
      [5,8,9,3,6,2,4,1,7],
      [8,6,7,1,2,5,3,9,4],
      [2,5,3,6,4,9,8,7,1],
      [4,9,1,8,7,3,6,2,5]]

print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid)

print ("\n\nTesting on medium 9x9 grid...")
grid = [[0,0,0,0,5,0,9,7,6], 
      [8,0,5,1,9,0,0,3,0],
      [3,7,0,0,4,0,0,8,0],
      [0,8,0,0,0,0,0,0,9],
      [0,2,0,0,0,0,4,0,7],
      [0,9,0,0,2,6,0,1,5],
      [0,0,0,0,8,1,6,0,0],
      [9,0,0,3,0,0,0,0,0],
      [2,0,0,4,0,9,0,0,0]]

print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid)

print ("\n\nTesting on medium 9x9 grid...")
grid = [[0,0,2,0,3,0,0,0,8],
      [0,0,0,0,0,8,0,0,0],
      [0,3,1,0,2,0,0,0,0],
      [0,6,0,0,5,0,2,7,0],
      [0,1,0,0,0,0,0,5,0],
      [2,0,4,0,6,0,0,3,1],
      [0,0,0,0,8,0,6,0,5],
      [0,0,0,0,0,0,0,1,3],
      [0,0,5,3,1,0,4,0,0]]

print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid)

print ("\n\nTesting unsolvable quadrant on a 9x9 grid...")
grid = [[0,9,0,3,0,0,0,0,1],
      [0,0,0,0,8,0,0,4,6],
      [0,0,0,0,0,0,8,0,0],
      [4,0,5,0,6,0,0,3,0],
      [0,0,3,2,7,5,6,0,0],
      [0,6,0,0,1,0,9,0,4],
      [0,0,1,0,0,0,0,0,0],
      [5,8,0,0,2,0,0,0,0],
      [2,0,0,0,0,7,0,6,0]]

print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid)

print ("\n\nTesting on hard 9x9 grid...")
grid = [[0,3,9,0,0,0,1,2,0],
      [0,0,0,9,0,7,0,0,0],
      [8,0,0,4,0,1,0,0,6],
      [0,4,2,0,0,0,7,9,0],
      [0,0,0,0,0,0,0,0,0],
      [0,9,1,0,0,0,5,4,0],
      [5,0,0,1,0,9,0,0,3],
      [0,0,0,8,0,5,0,0,0],
      [0,1,4,0,0,0,8,7,0]]
 
print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid)

print ("\n\nTesting on very hard 9x9 grid...")
grid = [[0,3,0,0,0,1,5,0,0],
      [0,0,0,5,0,0,0,8,4],
      [0,0,5,0,0,7,0,6,0],
      [0,0,0,0,0,0,0,0,0],
      [0,8,0,2,0,0,0,7,0],
      [0,0,0,8,5,0,0,0,9],
      [0,0,3,0,9,4,0,0,7],
      [0,0,4,0,0,0,0,0,8],
      [5,0,6,0,1,0,0,0,0]]
 
print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid)

print("\n\nTesting on a 9x9 easy letter puzzle")
grid = [['I','.','.','.','.','D','.','B','H'], 
        ['H','.','.','.','G','B','.','.','.'],
        ['.','.','C','A','.','.','F','.','.'],
        ['E','G','.','.','C','.','A','.','.'],
        ['.','I','.','H','B','G','.','C','.'],
        ['.','.','B','.','F','.','.','I','G'],
        ['.','.','E','.','.','C','B','.','.'],
        ['.','.','.','G','H','.','.','.','A'],
        ['D','C','.','B','.','.','.','.','I']]

print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid) 

print("\n\nTesting on a 9x9 hard letter puzzle")
grid = [['C','.','G','.','.','.','.','A','.'], 
        ['.','.','.','H','.','E','.','.','F'],
        ['I','.','.','.','G','.','.','.','D'],
        ['.','.','H','.','E','.','.','.','.'],
        ['B','.','.','F','.','H','.','.','C'],
        ['.','.','.','.','I','.','E','.','.'],
        ['H','.','.','.','A','.','.','.','G'],
        ['F','.','.','I','.','D','.','.','.'],
        ['.','C','.','.','.','.','I','.','H']]

print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid)  


"""print ("\n\nTesting on Norvig hard 9x9 grid") # around 23 minutes for a DFS with heuristic
grid = [[0,0,0,0,0,5,0,8,0],
      [0,0,0,6,0,1,0,4,3],
      [0,0,0,0,0,0,0,0,0],
      [0,1,0,5,0,0,0,0,0],
      [0,0,0,1,0,6,0,0,0],
      [3,0,0,0,0,0,0,0,5],
      [5,3,0,0,0,0,0,6,1],
      [0,0,0,0,0,0,0,0,4],
      [0,0,0,0,0,0,0,0,0]]

BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid) 
"""