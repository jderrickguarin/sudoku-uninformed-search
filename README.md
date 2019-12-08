# Solving a Sudoku puzzle using Depth-First Search, Breadth-First Search and DFS with Heuristics
##### Estoque, Carlo Gabriel; Guarin, Jan Derrick; Villanueva, Raphael Ervin
*Midterms & finals project for Introduction to Artificial Intelligence where we solve Sudoku using uninformed search strategies.*

## The Game of Sudoku
Sudoku (Japanese: “Su” meaning number + “Doku” meaning single) is a combinatorial number puzzle popularized in magazines and newspapers a few decades back. A typical Sudoku puzzle involves a 9x9 square grid, with each cell of the grid containing another 9 cells. Each section of 9 cells form a block. In total, there are 81 cells in the game, 9 cells contained in 9 blocks. Some cells contain a given number from the set (1,2,...,9).  

To win the game, the player must fill up all 81 cells with number using numbers from the set, where each row, column of block contains each number exactly once. Such constraint, called the ”One Rule”, makes the grid setup with pre-filled cells an interesting puzzle. 
There exists variations of the typical Sudoku game of size 3^2\*3^2, the game described above. A game of such size is defined to be a Sudoku game of rank-3. Another possible form of the Sudoku game is a rank-2 Sudoku game of size 2^2\*2^2. This is comprised of a 4 cells contained in 4 blocks making up a 16-celled grid.  

<p align="center"> A rank-2 Sudoku puzzle:  </p>

<p align="center">
  <img width="180" height="180" src="https://stemmiami.files.wordpress.com/2015/11/sudokuk4x4.jpg">
</p>

## Implementing Uninformed Search Strategies in Sudoku
Uninformed search strategies are algorithms that searches the state space for the goal state by means of a tree-traversing algorithm, without relying on other information. In this project, we are using a Depth-First Search (DFS) and Breadth-First Search (BFS) to arrive at the solution of an arbitrary Sudoku puzzle. The point of this project is not to determine the most efficient solution, but only to show an implementation of uninformed search strategies in a combinatorial puzzle. The puzzle game, along with implementations of the two search strategies, is implemented on Python.  

Peter Norvig, an AI expert, wrote an [essay](https://norvig.com/sudoku.html "Solving Every Sudoku Puzzle") and a program to explain how to solve any Sudoku puzzle in an efficient manner. Taking cue from the expert himself, we recognize that without using constraint propagation, that is accounting for constraints in a given square, any uninformed search algorithm risks solving any given puzzle in just a few billion years. Thus we made sure to limit the number of children of any node by applying the one-rule constraints in all tiles of a given puzzle.
##### **Depth-First Search**
A Depth-First Search (DFS) is a tree-traversal algorithm that makes use a stack data structure to iterate through the nodes and arrive at the goal state. This is utilized in the project by adding viable states to the stack based on all the legal options in a specific square. Each last node in the stack is popped and, as a successor state, is expanded. The cycle repeats until the Sudoku grid is complete. To note, in this case, the grid is solved raster-scan style, meaning from left to right, from top to bottom, which is inefficient.
##### **Breadth-First Search**
A Breadth-First Search (BFS) is a tree-traversal algorithm making use of a queue instead of a stack. This method makes use of horizontal expansions in order to cover all possibilities that may result in the Sudoku grid. With a queue method of arraying, it ensures that all nodes are addressed, however this algorithm is also time-consuming and therefore inefficient.
#### **Utilizing heuristics**
Besides the two uninformed search strategies, heuristics can also be applied in solving any Sudoku puzzle. Common algorithms that incorporate heuristics are the A* Search and Best-First Search, both of which consider the costs of traversing one node to another to get to the goal state quickly. However, this is hard to achieve in the game of Sudoku given that a puzzle only has one solution and it is impossible to quantify costs of each state since each action constitute to only one square answered. Therefore we had to find other heuristic methods to complement the search techniques.

In both DFS and BFS implementations, the method of solving the board is raster-scan. Norvig suggests that in solving a Sudoku puzzle, we have to choose between *variable ordering* and *value ordering* in solving a certain puzzle. Variable ordering refers to which tile should be first solved, while value ordering refers to which number should be placed in a tile first. In the case of our project, we consider variable ordering to solve puzzles more efficiently. More specifically, we utilized a similar concept to that used by Norvig, *"minimum remaining values"*, which means that we choose a tile with the least number of possible options. This replaces the initial raster-scan method of solving and is applied to the more efficient DFS implementation.

## PEAS Specification
For this project, consider a timed Sudoku game. Suppose that the agent aims to solve the puzzle (note: only one solution to each puzzle exists). The properties of the agent that will solve this can be grouped into a PEAS Specification. 
- Performance Measure: Satisfaction of One Rule on each row, column and block; Speed, or the shortest time at which the agent finishes the puzzle
- Environment: Given the Sudoku game, the environment is given as any N x N grid with n blocks containing n cells, and some cells filled with digits chosen from 1 to n. 
- Actuators: String generator to display number that will satisfy the constraints.
- Sensors: A scanner function that will scan rows, columns and blocks to determine the correct number number to input in blank cells 

## Results
In general, most puzzles were solved slower using Breadth-First Search. Depth-first Search proved to be more efficient in handling a Sudoku puzzle. If a heuristic is added in solving the puzzle, such as DFS with minimum remaining values heuristic, then the puzzle is solved in even a lesser amount of time.
This project though can still be made better if other factors are used. [Peter Norvig](https://norvig.com/sudoku.html "Solving Every Sudoku Puzzle") used a dictionary data structure instead of lists in making a Sudoku grid and his solutions to any problem were significantly faster than ours. He also proposes a value ordering heuristic called *least-constraining value*, which chooses first the value that imposes the fewest constraints on peers, and this might even improve the solution time.
In addition, there are other algorithms that can be used to solve a Sudoku puzzle, some of which might even be faster (e.g. Backtracking DFS).

## Installation and Operation
##### To use the check the process of solving:
1. Open `sudoku_solver.py` in the console.
2. You may change the test grids in the code using any text editor.
3. Use the `DFS_solve`, `BFS_solve` or `HSolve` functions according to which method you want to use in solving a grid.
4. You may check the code of each algorithm in their respective Python files.

## References
https://www.slideshare.net/FernandoJunior52/bdfsdfspaper?fbclid=IwAR07gT0SZ94nOHQILqatoMKqsqyXYuvpHbSrDIxv1iuwgnUuBgqBLzAm-gk
https://norvig.com/sudoku.html
https://github.com/tphanco/sample/blob/master/BDFS_Sudoku.py 
