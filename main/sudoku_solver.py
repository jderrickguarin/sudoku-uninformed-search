from BFS_Sudoku import BFS_solve
from DFS_Sudoku import DFS_solve
from Heuristics_Sudoku import H_Solve

print ("\n\nTesting on 6x6 grid...")
grid = [[1,5,0,0,4,0],
      [2,4,0,0,5,6],
      [4,0,0,0,0,3],
      [0,0,0,0,0,4],
      [6,3,0,0,2,0],
      [0,2,0,0,3,1]]

print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid)

print ("\n\nTesting on 6x6 grid...")
grid = [[0,0,0,0,4,0],
      [5,6,0,0,0,0],
      [3,0,2,6,5,4],
      [0,4,0,2,0,3],
      [4,0,0,0,6,5],
      [1,5,6,0,0,0]]

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

print ("\n\nTesting on 9x9 grid...")
grid = [[0,0,0,8,4,0,6,5,0],
      [0,8,0,0,0,0,0,0,9],
      [0,0,0,0,0,5,2,0,1],
      [0,3,4,0,7,0,5,0,6],
      [0,6,0,2,5,1,0,3,0],
      [5,0,9,0,6,0,7,2,0],
      [1,0,8,5,0,0,0,0,0],
      [6,0,0,0,0,0,0,4,0],
      [0,5,2,0,8,6,0,0,0]]

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

print ("\n\nTesting on 9x9 grid...")
grid = [[3,0,5,4,2,0,8,1,0],
      [4,8,7,9,0,1,5,0,6],
      [0,2,9,0,5,6,3,7,4],
      [8,5,0,7,9,3,0,4,1],
      [6,1,3,2,0,8,9,5,7],
      [0,7,4,0,6,5,2,8,0],
      [2,4,1,3,0,9,0,6,5],
      [5,0,8,6,7,0,1,9,2],
      [0,9,6,5,1,2,4,0,8]]

print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)
DFS_solve(grid)
H_Solve(grid)

print ("\n\nTesting on 9x9 grid...")
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

print ("\n\nTesting on 9x9 grid...")
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

"""print ("\n\nTesting on hard 9x9 grid")
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