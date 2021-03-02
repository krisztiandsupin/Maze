import pygame
from Settings import maze as maze_settings
import MazeFunctions
from Color import Color
from Color import MazeColor

global coordinate_text_size
coordinate_text_size = 10

class Cell:
    def __init__(self, coordinate, index, walls_bool):
        self.coordinate = coordinate
        self.position = None
        self.graph_position = None
        self.index = index

        self.walls = None           # coordinate pairs of walls
        self.walls_bool = walls_bool   # tuple of walls, if they exists or not
        self.border_points = None        # points of walls

    def color_graph(self, screen, color, size = maze_settings.graph_cell_size):
        '''pygame.draw.circle(screen, MazeColor.background, MazeFunctions.graph_position(self.position), maze_settings.graph_cell_size)
        pygame.draw.circle(screen, color, MazeFunctions.graph_position(self.position), size)'''
        pygame.draw.circle(screen, color, self.graph_position, size)

    def color(self, screen, color, graph_bool = False, line_color = Color.black, coordinate_text_bool = False):
        pygame.draw.polygon(screen, color, self.border_points)
        l = len(self.walls)

        for i in range(0, l):
            if self.walls_bool[i] == True:
                pygame.draw.line(screen, line_color, self.walls[i][0], self.walls[i][1])
            else:
                pygame.draw.line(screen, color, self.walls[i][0], self.walls[i][1])

        for point in self.border_points:
            pygame.draw.line(screen, line_color, point, point)

        if coordinate_text_bool == True:
            self.text_display(screen, str(self.coordinate), coordinate_text_size, Color.black, color)

        if graph_bool == True:
            if color == Color.white:
                color = Color.black
            self.color_graph(screen, color, maze_settings.graph_cell_size)

    def color_grid(self, screen, color, graph_bool = False, line_color = Color.black, coordinate_text_bool = False):
        pygame.draw.polygon(screen, color, self.border_points)
        l = len(self.walls)

        for i in range(0, l):
            pygame.draw.line(screen, line_color, self.walls[i][0], self.walls[i][1])

        if coordinate_text_bool == True:
            self.text_display(screen, str(self.coordinate), coordinate_text_size, Color.black, color)

        if graph_bool == True:
            if color == Color.white:
                color = Color.black
            self.color_graph(screen, color, maze_settings.graph_cell_size)

    def text_display(self, screen, text, text_size, text_color = Color.black, highlight_color = Color.white):
        MazeFunctions.text_display(screen, self.position[0], self.position[1], text, text_size, text_color, highlight_color)