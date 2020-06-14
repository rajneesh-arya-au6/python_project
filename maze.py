import argparse

def cross_check(maze):
    # copy of maze with all values as 0
    out_maze = [[0]*length for i in range(length)]
    #returning false and writing -1 in the output file
    # make sure source is (0,0)
    if maze[0][0] == 0 or maze[length-1][length-1] == 0:
        output_file.write('-1')
        return False
    #returning false and writing -1 in the output file
    if maze_solver(maze, 0, 0, out_maze) is False:
        output_file.write('-1')
        return False
    #returning true and writing output in the output file
    for i in out_maze:
        for j in i:
            output_file.write(f' {str(j)} ')
        output_file.write('\n')
    print("your Maze is solved. please check the output file")
    return True

#solving the maze here
def maze_solver(maze, x, y, out_maze):

    if x == length - 1 and y == length - 1:
        out_maze[x][y] = 1
        return True

    if checking_index(maze, x, y) is True:
        out_maze[x][y] = 1

        if maze_solver(maze, x + 1, y, out_maze) is True:
            return True
        if maze_solver(maze, x, y + 1, out_maze) is True:
            return True
        out_maze[x][y] = 0
        return False

# here we are checking if the move is outside the matrix
def checking_index(maze, x, y):

    if x >= 0 and x < length and y >= 0 and y < length and maze[x][y] == 1:
        return True

    return False  # if any index is -1 or in not proper format


# handling the file using Argparser 
pars = argparse.ArgumentParser()
pars.add_argument('inputFile', help='Please provide a full path for the input file')
pars.add_argument('outputFile', help='Please provide a full path for the output file')
arg = pars.parse_args()

input_file = open(arg.inputFile, 'r')
output_file = open(arg.outputFile, 'w')

# getting input from external file
maze = []
for data in input_file:
    [l.strip('\n') for l in data]
    maze.append([int(x) for x in data.split()])
length = len(maze)
cross_check(maze)
