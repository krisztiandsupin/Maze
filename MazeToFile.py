"""
    Maze file format
    size: int n
    type_value: int n
    algorithm: str algorithm_name
    cell_list: <cell_type> list
	    <cell_type> = coordinate, index, walls_bool
    maze_list: int nested list which stores available path in the maze in an edge list
"""


def write_to_file(maze, file_name):
    maze_file = open(file_name, "w+")

    maze_file.write(f"size: {maze.size} \n")
    maze_file.write(f"maze_type: {maze.maze_type} \n")
    maze_file.write(f"algorithm: {maze.algorithm} \n")

    # write cells info
    maze_file.write("cell_list: \n")
    for cell in maze.cell_list:
        maze_file.write(f"{cell.coordinate}; {cell.index}; {cell.walls_bool} \n")

    # write maze info
    maze_file.write("maze_list: \n")
    for cell in maze.maze_list:
        maze_file.write(f"{cell} \n")



    # end of file
    maze_file.write("&&& \n")
    print(f"maze is succefully saved to {file_name}")
    maze_file.close()
