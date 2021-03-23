import pygame
from Settings import maze as maze_settings
import MazeFunctions
from Color import Color
from Color import MazeColor

global coordinate_text_size
coordinate_text_size = 10

class Cell:
    """
    :param tuple coordinate: square = (row, column), circle = (ring, element in ring), hexagon = (ring, element in ring) \
        triange = (row, element in row)
    :param tuple position:
    :param tuple graph_position:
    :param int index: cell index in cell_list of a maze
    :param list of tuples walls: list of coordinate pairs of wall endpoints
    :param list of boolenas walls_bool: tuple of walls, if they exists or not
    :param list of tuples border_points: endpoints points of walls
    :param boolean visible: if a cell is discovered or not, used in discovery of a maze
    """
    def __init__(self, coordinate, index, walls_bool):
        self.coordinate = coordinate
        self.position = None
        self.graph_position = None
        self.index = index

        self.walls = None           # coordinate pairs of walls
        self.walls_bool = walls_bool   # tuple of walls, if they exists or not
        self.border_points = None        # points of walls

        self.visible = None         # used in discovery of a maze

    def color_graph(self, screen, color, size = maze_settings.graph_cell_size):
        pygame.draw.circle(screen, color, self.graph_position, size)

    def color(self, screen, color, graph_bool = False, line_color = Color.black, coordinate_text_bool = False):
        """

        :param screen:
        :param color:
        :param graph_bool:
        :param line_color:
        :param coordinate_text_bool:
        """
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

    def color_grid(self, screen, color, graph_bool = False, line_color = Color.black, coordinate_text_bool = False, walls_bool = False):
        """

        :param screen:
        :param color:
        :param graph_bool:
        :param line_color:
        :param coordinate_text_bool:
        """
        pygame.draw.polygon(screen, color, self.border_points)
        l = len(self.walls)

        for i in range(0, l):

            if bool(walls_bool):
                if walls_bool[i] == True:
                    pygame.draw.line(screen, line_color, self.walls[i][0], self.walls[i][1])
                else:
                    pygame.draw.line(screen, color, self.walls[i][0], self.walls[i][1])

            else:
                pygame.draw.line(screen, line_color, self.walls[i][0], self.walls[i][1])

        for point in self.border_points:
            pygame.draw.line(screen, line_color, point, point)

        if coordinate_text_bool == True:
            self.text_display(screen, str(self.coordinate), coordinate_text_size, Color.black, color)

        if graph_bool == True:
            if color == Color.white:
                color = Color.black
            self.color_graph(screen, color, maze_settings.graph_cell_size)



    def text_display(self, screen, text, text_size, text_color = Color.black, background_color = Color.white):
        """
        displays text to a specific cell
        :param screen:
        :param text:
        :param text_size:
        :param text_color:
        :param background_color:
        """
        MazeFunctions.text_display(screen, self.position[0], self.position[1], text, text_size, text_color, background_color)

    def draw_sign(self, screen, color, sign_size = 0):
        """

        :param screen:
        :param color:
        :param sign_size:
        """
        pygame.draw.circle(screen, color, self.position, sign_size)