# Maze Solver Project
---
By : Rajneesh Arya
Email : rajneesharya94@gmail.com
---

## What is Maze Solver:

It is a program that determine the path between one end to another in a maze, which contains 0's and 1's as the path wherer 0 is the blocked path and 1 is the open path.

## This Read me file consits of following topics:
- How to run MazeSolver In Windows Operating System.
- How to run MazeSolver In Linux Operating System.
- My Approach to tackle the problem.
- Code Explanation (function by function).
- Modules used.
- My Final Words.

The Project folder consists of 4 files.

1. maze.py

2. input.txt

3. output.txt

4. README.md




### maze.py
This file contains the codes for the maze solver.

### input.txt
This text files contains a unsolved matrix, which will be the input for the maze.py !!!

### output.txt
This text files contains a solved matrix, which is coming as the output from the maze.py !!!

### README.md 
It is a UserGuid for the mazesolver project.

## How to run MazeSolver In Windows Operating System

Firstly, in the `project` directory you can see input.txt file insert your maze combination to that file.

`Things to keep in mind while making a maze.`

The input should be space-separated like, `1 0 0 1 0 1 0` likewise.
>Don’t forget to give space between each numeral

Now, that you give input correctly. In the same directory, you can see W_MazeSolver.bat file just double click on that file and the program will automatically generate output.txt file with the correct path.

And in the case, you don't want to name output file as output.txt then in that case,

First, make .txt file type in the command

`mazeSolver (name_of_input_file.txt) (name_of_output_file.txt)`

then after editing change this file extension to .bat and run it by double-clicking the icon

## How to run MazeSolver In Linux Operating System

Firstly, in the `python project` directory you can see input.txt file give your maze combination to that file.

`Please keep in mind while making a maze.`

The input should be space-separated like, `1 0 0 1 0 1 0` likewise.
=> Don’t forget to give space between each numeral

Now, that you give input correctly. In the same directory, you can see maze.py file just run the file using Command line interface(make sure you are in the same directory as maze.py)

## HOW TO RUN THE FILE IN THE COMMAND LINE INTERFACE (CLI)
`python absolute path of the maze.py (absolute Path of the input file) (absolute path of the output file)`

******Important*********

>>>For EXAMPLE:
## python "e:/workspace/project/maze.py" "e:/workspace/project/input.txt" "e:/workspace/project/output.txt" 


### Code Explanation (function by function)

Program is starting from line 49, where I'm asking the user to give input file and destination file name with the help of python module named as `argparse` .

Then on line 58, I'm taking maze as list and on line 59 to 61 taking user inputs and storing into maze list.

**authorize_maze() Function**

Firstly, making out_maze exact same format as given input maze, you can also call it a copy of user input maze but with all elements as 0, just a structure of user input maze.

If src (starting_point) is 0, then it will print(-1) i.e, Maze has no path.

If the path found between src(starting_point) and dest(destination_point) then it will be printed on output file where 0 blocks and 1 is the path walkover.

**maze_solver() Function**

If dest(destination_point) is 1 or not, if dest(destination_point) is 0, then it will print (-1) i.e, Maze has no path, then moving to authorize index step by step and after that recursion, starts and find the path.

**authorize_index() Function**

Basically, this function authorizes indices/format of the matrix


## Modules Used

In creating this program I used couple of predefined python modules like :

`argparse` - To get user input in command line

