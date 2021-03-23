from Maze import Maze
from Cell import Cell

def read_from_file(file_name):
    maze_file = open(file_name, "r+")

    size = int(maze_file.readline().split(':')[1][1:-2])
    type = maze_file.readline().split(':')[1][1:-2]
    algorithm = maze_file.readline().split(':')[1][1:-2]

    maze = Maze(size, type, algorithm)


    maze_file.readline()[:-2]

    new_line = maze_file.readline()[:-2]

    # cell_list
    cell_list = []
    while new_line != 'maze_list:':
        cell_string = new_line.split(';')
        coordinate_parts = cell_string[0].split(', ')
        coordinate = (int(coordinate_parts[0][1:]), int(coordinate_parts[1][:-1]))
        index = int(cell_string[1][1:])

        walls_string = (cell_string[2][2: -1].split(', '))
        walls_bool = [i == 'True' for i in walls_string]

        cell = Cell(coordinate, index, walls_bool)
        cell_list.append(cell)
        new_line = maze_file.readline()[:-2]

    maze.cell_list = cell_list

    new_line = maze_file.readline()[:-2]

    # maze_list
    maze_list = []
    while new_line != '&&&':
        list_parts = new_line[1:-1].split(', ')
        list_int = [int(i) for i in list_parts]
        maze_list.append(list_int)
        new_line = maze_file.readline()[:-2]

    maze.maze_list = maze_list
    maze_file.close()

    print(f"maze is succefully opened from {file_name}")

    return maze

