from Maze import Maze
import MazeToFile

maze_background = Maze(15, 'circle', 'kruskal')
file_background = "maze_background.txt"

MazeToFile.write_to_file(maze_background, file_background)