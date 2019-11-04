# Solving a rank-2 Sudoku puzzle using Backtracking Depth-First Search and Breadth-First Search
##### Estoque, Carlo Gabriel; Guarin, Jan Derrick; Villanueva, Raphael Ervin
*Midterm project for Introduction to Artificial Intelligence where we solve Sudoku using uninformed search strategies.*

## The Game of Sudoku
Sudoku (Japanese: “Su” meaning number + “Doku” meaning single) is a combinatorial number puzzle popularized in magazines and newspapers a few decades back. A typical Sudoku puzzle involves a 9x9 square grid, with each cell of the grid containing another 9 cells. Each section of 9 cells form a block. In total, there are 81 cells in the game, 9 cells contained in 9 blocks. Some cells contain a given number from the set (1,2,...,9). 
To win the game, the player must fill up all 81 cells with number using numbers from the set, where each row, column of block contains each number exactly once. Such constraint, called the ”One Rule”, makes the grid setup with pre-filled cells an interesting puzzle. 
There exists variations of the typical Sudoku game of size 3^2\*3^2, the game described above. A game of such size is defined to be a Sudoku game of rank-3. Another possible form of the Sudoku game is a rank-2 Sudoku game of size 2^2\*2^2. This is comprised of a 4 cells contained in 4 blocks making up a 16-celled grid. 
A rank-2 Sudoku puzzle

## Implementing Uninformed Search Strategies in Sudoku
Uninformed search strategies are algorithms that searches the state space for the goal state by means of a tree-traversing algorithm, without relying on other information. In this project, we are using a Backtracking Depth-First Search (B-DFS) and Breadth-First Search (BFS) to arrive at the solution of an arbitrary rank-2 Sudoku puzzle. The point of this project is not to determine the most efficient solution, but only to show an implementation of uninformed search strategies in a combinatorial puzzle. The puzzle game, along with implementations of the two search strategies, is implemented on VBA and MS Excel.
##### **Backtracking Depth-First Search**
A Backtracking Depth-First Search (B-DFS) is similar to the regular Depth-First Search strategy \[ADD LATER]
##### **Breadth-First Search**
This method makes use of horizontal expansions in order to cover all possibilities that may result in the sudoku board. With a queue method of arraying, it ensures that all nodes are addressed, however this algorithm is also time-consuming.

## PEAS Specification
For this project, consider a timed rank-2 Sudoku game. Suppose that the agent aims to solve the puzzle (note: only one solution to each puzzle exists). The properties of the agent that will solve this can be grouped into a PEAS Specification. 
- Performance Measure: Satisfaction of One Rule on each row, column and block; Speed, or the shortest time at which the agent finishes the puzzle
- Environment: Given the rank-2 Sudoku game, the environment is given as a 4x4 grid with 4 blocks containing 4 cells, and some cells - filled with digits chosen from 1 to 9. 
- Actuators: String generator to display number that will satisfy the constraints. The agent may also clear the ‘board’.
- Sensors: A scanner function that will scan rows, columns and blocks to determine the correct number number to input in blank cells 

## Installation and Operation
*Note: Make sure to enable the* **Developer** *ribbon in your MS Excel*
##### To use the Excel file containing the game and the solving algorithms:
1. Unzip the file containing `sudoku.xlsm`.
2. Open the `sudoku.xlsm` file in MS Excel. You will see a rank-2 Sudoku grid on the worksheet, along with the buttons: **Create**, **Clear**, **Solve B-DFS**, and **Solve BFS**.
3. The **Create** button creates a new random puzzle. 
4. The **Solve B-DFS** button uses Backtracking Depth-First Search to solve the puzzle, while the **Solve BFS** uses Breadth-First Search to solve the puzzle. 
5. Click the **Clear** button to return the grid to a blank slate. 
##### To check the source code of the solver:
1. In the **Developer** ribbon, click **Visual Basic** to open the Visual Basic Editor.
2. In the left pane, right click on **Module 1** under the workbook titled `sudoku.xlsm`.
3. Click **View Code**. Use the **(Declarations)** drop-down list box to navigate the code. 

## References
https://www.slideshare.net/FernandoJunior52/bdfsdfspaper?fbclid=IwAR07gT0SZ94nOHQILqatoMKqsqyXYuvpHbSrDIxv1iuwgnUuBgqBLzAm-gk

https://github.com/tphanco/sample/blob/master/BDFS_Sudoku.py 
