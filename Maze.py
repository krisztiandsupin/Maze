from Settings import screen as screen_settings
from Color import Color
import CellList
import EdgeList
import pygame
import Generation
import MazeFunctions
import Solving

global coordinate_text_size
coordinate_text_size = 10


class Maze:
    class Type:
        square = 0
        circle = 1
        hexagon = 2
        triangle = 3

    def __init__(self, size, maze_type, algorithm):
        self.size = size
        self.maze_type = maze_type
        self.type_value = getattr(self.Type, maze_type)
        self.position = None
        self.cell_size = None
        self.graph_cell_size = None
        self.algorithm = algorithm

        self.cell_list = CellList.generate(self.type_value, self.size)
        self.edge_list = EdgeList.generate(self.type_value, self.size)

        #self.frame_list = MazeFunctions.frame_generation(self.type_value, self.cell_list)
        self.maze_list, self.maze_order = Generation.generate(algorithm, self.type_value, self.cell_list, self.edge_list)

        self.solution_path = []
        self.visited = []

        self.graph_bool = False
        self.step_bool = False
        self.delay = False

        (start, end) = MazeFunctions.cell_endpoints_calculate(self.type_value, self.size)
        self.start = self.cell_list[start]
        self.end = self.cell_list[end]

    def copy(self):
        return Maze(self.size, self.maze_type, self.algorithm)

    def print_statistics(self):
        print('size:', self.size)
        print('type: {0} ({1})'.format(type, self.type_value))
        print('algorithm:', self.algorithm)
        print('cell_size:', self.cell_size)
        print('cell list:', len(self.cell_list))
        print('edge list:', len(self.edge_list))
        #print('grid number:', len(self.grid))
        print('frame number:', len(self.frame_list))
        print('graph number:', len(self.graph_list))
        print()

    def create(self, maze_position = (screen_settings.screen_size[0] // 2, screen_settings.screen_size[1]), \
               display_type = 0, graph_bool = False):
        """
        :param tuple maze_position: center of position; default: middle of screen
        :param int display_type: fullscreen = 0, half screen = 1, quarter_screen
        :param bool graph_bool: if True displays the graph of the maze; delfault = True
        """
        self.position = maze_position
        self.cell_size = MazeFunctions.cell_size_calculate(display_type, self.type_value, self.size, graph_bool)
        self.graph_cell_size = MazeFunctions.graph_cell_size_calculate(self.type_value, self.cell_size)
        CellList.create_square(self.cell_list, self.type_value, maze_position, display_type, graph_bool, self.cell_size)
        self.frame_list = MazeFunctions.frame_generation(self.type_value, self.cell_list)


    def draw(self, screen, graph_bool = True, step_bool = False, delay = 100,
             position = (screen_settings.screen_size[0] // 2, screen_settings.screen_size[1])):
        """
        :param screem: square = 0, circle = 1, hexagon = 2, triangle = 3
        :param int display_type: fullscreen = 0, half screen = 1, quarter_screen
        :param bool graph_bool: if True displays the graph of the maze; delfault = True
        :param bool step_bool: if True displays steps of generation; default = False
        :param int delay: delay between steps in ms; default = 100
        :param tuple position: center of position; default: middle of screen
        """

        if graph_bool == True:
            pygame.draw.line(screen, Color.navy, (screen_settings.screen_size[0] // 2, 50), position, 5)

        for cell in self.cell_list:
            cell.color_grid(screen, Color.white, graph_bool)

            #cell.text_display(screen, str(cell.index), 12)

        MazeFunctions.system_pause()

        for wall in self.frame_list:
            pygame.draw.line(screen, Color.black, wall[0], wall[1], 3)

        for edge in self.maze_order:
            MazeFunctions.edge_color(screen, edge, Color.white, graph_bool)
            MazeFunctions.system_pause()

            # pygame.draw.line(screen, Color.green, edge[0].position, edge[1].position)
            if step_bool == True:
                MazeFunctions.updete_delay(delay)

        self.start.color(screen, Color.green_light)
        self.end.color(screen, Color.salmon)

        if graph_bool == True:
            pygame.draw.circle(screen, Color.green_light, self.start.graph_position, self.graph_cell_size + 2)
            pygame.draw.circle(screen, Color.salmon, self.end.graph_position, self.graph_cell_size + 2)


        for wall in self.frame_list:
            pygame.draw.line(screen, Color.black, wall[0], wall[1], 3)

        MazeFunctions.system_pause()

    def solve(self, algorithm):
        maze_list = self.maze_list.copy()
        cell_list = self.cell_list.copy()

        if algorithm == 'astar':
            self.solution_path, self.visited = Solving.astar(self.type_value, cell_list, maze_list, self.start, self.end)
        elif algorithm == 'endfiller':
            self.solution_path, self.visited = Solving.endfiller(self.type_value, cell_list, maze_list, self.start, self.end)
        elif algorithm == 'backtracker':
            return []
        elif algorithm == 'eller':
            return []
        else:
            print('error: wrong type of algorithm')
            return None

        return self.solution_path, self.visited

    def show(self, screen):
        color_visited = Color.yellow_light
        color_deadend = Color.grey_light
        color_path = Color.blue_light
        delay = 10

        #del self.visited[-1]

        for block in self.highlight:
            visited = block[0]
            deadend = block[1]

            for cell in visited:
                cell.color(screen, color_visited)
                pygame.draw.circle(screen, color_visited, cell.graph_position, self.graph_cell_size + 2)
                MazeFunctions.updete_delay(delay)
                MazeFunctions.system_pause()

            for cell in deadend:
                cell.color(screen, color_deadend)
                pygame.draw.circle(screen, color_deadend, cell.graph_position, self.graph_cell_size + 2)
                MazeFunctions.updete_delay(delay)
                MazeFunctions.system_pause()

        #del self.solution_path[0]

        for cell in self.solution_path:
            cell.color(screen, color_path)
            pygame.draw.circle(screen, color_path, cell.graph_position, self.graph_cell_size + 2)
            MazeFunctions.updete_delay(delay)
            MazeFunctions.system_pause()

        self.start.color(screen, Color.green_light)
        self.end.color(screen, Color.salmon)

        for wall in self.frame_list:
            pygame.draw.line(screen, Color.black, wall[0], wall[1], 3)
        MazeFunctions.updete_delay(1000)
        MazeFunctions.system_pause()
