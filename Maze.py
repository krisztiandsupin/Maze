import Frame
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
    """

    """

    maze_type_dict = {
        'square' : 0,
        'circle' : 1,
        'hexagon' : 2,
        'triangle' : 3
    }

    class Type:
        square = 0
        circle = 1
        hexagon = 2
        triangle = 3

    def __init__(self, size, maze_type, algorithm, auto_generation=True):
        self.size = size
        self.maze_type = maze_type
        self.type_value = getattr(self.Type, maze_type)
        self.position = None
        self.cell_size = None
        self.graph_cell_size = None
        self.algorithm = algorithm

        if auto_generation:
            self.cell_list = CellList.generate(self.type_value, self.size)
            self.edge_list = EdgeList.generate(self.type_value, self.size)

            self.maze_list, self.maze_order, self.maze_cell_borders = Generation.generate(algorithm, self.type_value,
                                                                                          self.cell_list,
                                                                                          self.edge_list)

        else:
            self.cell_list = None
            self.edge_list = None

            self.maze_list, self.maze_order, self.maze_cell_borders = None, None, None

        # solution lists
        self.solution_path = []
        self.visited = []

        self.graph_bool = False
        self.step_bool = False
        self.delay = False

        (start, end) = MazeFunctions.cell_endpoints_calculate(self.type_value, self.size)

        self.start = self.cell_list[start]
        self.end = self.cell_list[end]

        # maze colors
        self.color_background = Color.white
        self.color_line = Color.black
        self.color_start = Color.green_light
        self.color_end = Color.salmon
        self.color_frame = Color.black

    def copy(self):
        """

        :return:
        """
        return Maze(self.size, self.maze_type, self.algorithm)

    def print_statistics(self):
        """

        """
        print('size:', self.size)
        print('type: {0} ({1})'.format(type, self.type_value))
        print('algorithm:', self.algorithm)
        print('cell_size:', self.cell_size)
        print('cell list:', len(self.cell_list))
        print('edge list:', len(self.edge_list))
        print('frame number:', len(self.frame_list))
        print('graph number:', len(self.graph_list))
        print()

    def create(self, maze_position=(screen_settings.screen_size[0] // 2, screen_settings.screen_size[1]),
               display_type=0, graph_bool=False, cell_size_constant=1):
        """
        :param tuple maze_position: center of position; default: middle of screen
        :param int display_type: fullscreen = 0, half screen = 1, quarter_screen = 2
        :param bool graph_bool: if True displays the graph of the maze; delfault = True
        """
        self.position = maze_position

        self.cell_size = int(
            cell_size_constant * MazeFunctions.cell_size_calculate(display_type, self.type_value, self.size,
                                                                   graph_bool))

        self.graph_cell_size = MazeFunctions.graph_cell_size_calculate(self.type_value, self.cell_size)

        CellList.create(self.cell_list, self.type_value, maze_position, display_type, graph_bool, self.cell_size)

        (start, end) = MazeFunctions.cell_endpoints_calculate(self.type_value, self.size)

        self.start = self.cell_list[start]
        self.end = self.cell_list[end]
        self.frame_list = Frame.generation(self.type_value, self.cell_list)

    def draw_frame(self, screen, frame_size=3):
        """

        :param screen:
        :param frame_size:
        """
        for wall in self.frame_list:
            pygame.draw.line(screen, self.color_frame, wall[0], wall[1], frame_size)

    def draw_grid(self, screen, graph_bool=True, cell_text_bool=False, cell_text_type=0):
        """

        :param screen:
        :param graph_bool:
        :param cell_text_bool:
        :param cell_text_type:
        """
        for cell in self.cell_list:
            cell.color_grid(screen, self.color_background, graph_bool, self.color_line)
            if cell_text_bool:
                if cell_text_type == 0:
                    cell_text = str(cell.coordinate)
                elif cell_text_type == 1:
                    cell_text = str(cell.index)
                elif cell_text_type == 2 and self.type_value == 2:
                    cell_text = str(MazeFunctions.coordinate_transform_hexagon(cell.coordinate))
                else:
                    print("error: invalid cell_text_bool type")
                    cell_text = ''

                cell.text_display(screen, cell_text, 15)

    def draw(self, screen, graph_bool=True, visibility_bool=True, cell_text_bool=False, cell_text_type=0):
        """
        :param screem: square = 0, circle = 1, hexagon = 2, triangle = 3
        :param int display_type: fullscreen = 0, half screen = 1, quarter_screen
        :param bool graph_bool: if True displays the graph of the maze; delfault = True
        :param bool visibility_bool: if True all cells with walls can be seen
        :param bool cell_text_bool: display text in the middle of all the circles
        :param int cell_text_type: coordinate = 0, index = 1,
            hexagonal transformed cordinated = 2 (just in hexagonal type)
        """

        if visibility_bool:
            self.color_background = Color.grey_dark
            self.color_line = Color.grey_dark

        for cell in self.cell_list:
            cell.color(screen, self.color_background, graph_bool, self.color_line)

        self.start.color(screen, self.color_start, graph_bool, self.color_line)
        self.end.color(screen, self.color_end, graph_bool, self.color_line)

        if graph_bool:
            pygame.draw.circle(screen, self.color_start, self.start.graph_position, self.graph_cell_size + 2)
            pygame.draw.circle(screen, self.color_end, self.end.graph_position, self.graph_cell_size + 2)

        self.draw_frame(screen)

        MazeFunctions.system_pause()

    ############
    # maze solving visualisation
    def solve(self, algorithm):
        """

        :param algorithm:
        :return:
        """
        maze_list = self.maze_list.copy()
        cell_list = self.cell_list.copy()

        if algorithm == 'astar':
            self.solution_path, self.visited = Solving.astar(self.type_value, cell_list, maze_list, self.start,
                                                             self.end)
        elif algorithm == 'endfiller':
            self.solution_path, self.visited = Solving.endfiller(self.type_value, cell_list, maze_list, self.start,
                                                                 self.end)
        elif algorithm == 'backtracker':
            return []
        elif algorithm == 'eller':
            return []
        else:
            print('error: wrong type of algorithm')
            return None

        return self.solution_path, self.visited

    def show(self, screen, delay=10):
        """

        :param screen:
        :param delay:
        """
        color_visited = Color.yellow_light
        color_deadend = Color.grey_light
        color_path = Color.blue_light

        # del self.visited[-1]

        for block in self.visited:
            visited = block[0]
            deadend = block[1]

            for cell in visited:
                cell.color(screen, color_visited)
                if self.graph_bool:
                    cell.color_graph(screen, color_visited)
                # pygame.draw.circle(screen, color_visited, cell.graph_position, self.graph_cell_size + 2)
                if delay > 0:
                    MazeFunctions.updete_delay(delay)
                    MazeFunctions.system_pause()

            for cell in deadend:
                cell.color(screen, color_deadend)
                if self.graph_bool:
                    cell.color_graph(screen, color_deadend)
                # pygame.draw.circle(screen, color_deadend, cell.graph_position, self.graph_cell_size + 2)

                if delay > 0:
                    MazeFunctions.updete_delay(delay)
                    MazeFunctions.system_pause()

        # del self.solution_path[0]

        for cell in self.solution_path:
            self.cell_list[cell].color(screen, color_path)
            if self.graph_bool:
                cell.color_graph(screen, color_path)
            # pygame.draw.circle(screen, color_path, self.cell_list[cell].graph_position, self.graph_cell_size + 2)
            if delay > 0:
                MazeFunctions.updete_delay(delay)
                MazeFunctions.system_pause()

        self.start.color(screen, Color.green_light)
        self.end.color(screen, Color.salmon)

        for wall in self.frame_list:
            pygame.draw.line(screen, Color.black, wall[0], wall[1], 3)
        MazeFunctions.updete_delay(1000)
        MazeFunctions.system_pause()
