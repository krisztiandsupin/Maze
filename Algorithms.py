import pygame

import Settings
from Color import Color
from Text import Text
import Functions
from Settings import screen as screen_settings

from Maze import Maze

screen_size = screen_settings.screen_size

algorithm_display = pygame.display.set_mode(screen_size)
#gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Maze')
pygame.init()

text_color = Color.navy
text_color_light = Color.navy_light
text_size = 50

import MazeFunctions

def settings():
    algorithm_display.fill(Color.white)
    text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'Algorithms', int(text_size * 1.5), text_color, text_color_light)
    text_title.show(algorithm_display)

    while True:
        kruskal_slide1()
        kruskal_slide2()
        Functions.update_delay(10000)

def kruskal_slide1():
    algorithm_display.fill(Color.white)
    text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'Kruskal Algorithm', int(text_size * 1.5), text_color,
                      text_color_light)
    text_title.show(algorithm_display)

    maze_kruskal = Maze(8, 'square', 'kruskal')
    maze_kruskal.create((screen_settings.screen_size[0] // 4, screen_settings.screen_size[1] //2), graph_bool=True)
    maze_kruskal.draw_grid(algorithm_display, graph_bool=True, cell_text_bool=True, cell_text_type=1)

    highlight_color = Color.red_light
    delay = 100
    index_text_size = 15

    maze_kruskal.draw_frame(algorithm_display)

    for i in range(0, len(maze_kruskal.maze_order)):
        cell0, cell1 = maze_kruskal.maze_order[i][0], maze_kruskal.maze_order[i][1]

        highlight_edge_delete(algorithm_display, maze_kruskal, cell0, cell1, highlight_color, True, index_text_size, i)

        Functions.update_delay(delay)
        MazeFunctions.edge_color(algorithm_display, (cell0, cell1), highlight_color, graph = True, graph_color = maze_kruskal.color_line)


        highlight_edge_delete(algorithm_display, maze_kruskal, cell0, cell1, maze_kruskal.color_background, True, index_text_size, i)
        MazeFunctions.edge_color(algorithm_display, (cell0, cell1), maze_kruskal.color_background, graph=True,
                             graph_color=maze_kruskal.color_line)

        maze_kruskal.draw_frame(algorithm_display)

        Functions.update_delay(delay)
        Functions.buttonpress_detect()


def kruskal_slide2():
    algorithm_display.fill(Color.white)
    text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'Kruskal Algorithm', int(text_size * 1.5),
                      text_color,
                      text_color_light)
    text_title.show(algorithm_display)

    maze_kruskal_hexagon = Maze(5, 'hexagon', 'kruskal')
    maze_kruskal_hexagon.create((screen_settings.screen_size[0] // 4, screen_settings.screen_size[1] // 2), graph_bool=False)
    maze_kruskal_hexagon.draw_grid(algorithm_display, graph_bool=False, cell_text_bool=True, cell_text_type=1)
    maze_kruskal_hexagon.draw_frame(algorithm_display)

    maze_kruskal_circle = Maze(5, 'circle', 'kruskal')
    maze_kruskal_circle.create(((3 * screen_settings.screen_size[0]) // 4, screen_settings.screen_size[1] // 2), graph_bool=False)
    maze_kruskal_circle.draw_grid(algorithm_display, graph_bool=False, cell_text_bool=True, cell_text_type=1)
    maze_kruskal_circle.draw_frame(algorithm_display)

    highlight_color = Color.red_light
    delay = 100
    index_text_size = 15

    for i in range(0, min(len(maze_kruskal_hexagon.maze_order), len(maze_kruskal_circle.maze_order))):
        cell0_hexagon, cell1_hexagon = maze_kruskal_hexagon.maze_order[i][0], maze_kruskal_hexagon.maze_order[i][1]

        highlight_edge_delete(algorithm_display, maze_kruskal_hexagon, cell0_hexagon, cell1_hexagon, highlight_color, False, index_text_size, i)

        cell0_circle, cell1_circle = maze_kruskal_circle.maze_order[i][0], maze_kruskal_circle.maze_order[i][1]

        highlight_edge_delete(algorithm_display, maze_kruskal_circle, cell0_circle, cell1_circle, highlight_color, False, index_text_size, i)

        Functions.update_delay(delay)

        MazeFunctions.edge_color(algorithm_display, (cell0_hexagon, cell1_hexagon), highlight_color, graph=False)

        highlight_edge_delete(algorithm_display, maze_kruskal_hexagon, cell0_hexagon, cell1_hexagon, maze_kruskal_hexagon.color_background, False,
                              index_text_size, i)
        MazeFunctions.edge_color(algorithm_display, (cell0_hexagon, cell1_hexagon), maze_kruskal_hexagon.color_background, graph=False)

        maze_kruskal_hexagon.draw_frame(algorithm_display)

        MazeFunctions.edge_color(algorithm_display, (cell0_circle, cell1_circle), highlight_color, graph=False)

        highlight_edge_delete(algorithm_display, maze_kruskal_circle, cell0_circle, cell1_circle, maze_kruskal_circle.color_background, False,
                              index_text_size, i)
        MazeFunctions.edge_color(algorithm_display, (cell0_circle, cell1_circle), maze_kruskal_circle.color_background, graph=False)

        maze_kruskal_circle.draw_frame(algorithm_display)

        Functions.update_delay(delay)
        Functions.buttonpress_detect()

    for i in range(min(len(maze_kruskal_hexagon.maze_order), len(maze_kruskal_circle.maze_order)), len(maze_kruskal_circle.maze_order)):
        cell0_circle, cell1_circle = maze_kruskal_circle.maze_order[i][0], maze_kruskal_circle.maze_order[i][1]

        highlight_edge_delete(algorithm_display, maze_kruskal_circle, cell0_circle, cell1_circle, highlight_color, False,
                              index_text_size, i)
        Functions.update_delay(delay)
        MazeFunctions.edge_color(algorithm_display, (cell0_circle, cell1_circle), highlight_color, graph=False,
                                 )

        highlight_edge_delete(algorithm_display, maze_kruskal_circle, cell0_circle, cell1_circle,
                              maze_kruskal_circle.color_background, False, index_text_size, i)
        MazeFunctions.edge_color(algorithm_display, (cell0_circle, cell1_circle), maze_kruskal_circle.color_background,
                                 graph=False)

        maze_kruskal_circle.draw_frame(algorithm_display)

        Functions.update_delay(delay)

def highlight_edge_delete(screen, maze, cell0, cell1, highlight_color, graph_bool, index_text_size, step):
    cell0.color_grid(screen, highlight_color, graph_bool, line_color=Color.black, \
                     coordinate_text_bool=False, walls_bool = maze.maze_cell_borders[step][0])
    cell1.color_grid(screen, highlight_color, graph_bool, line_color=Color.black, \
                     coordinate_text_bool=False, walls_bool=maze.maze_cell_borders[step][1])
    cell0.text_display(screen, str(cell0.index), index_text_size, background_color= highlight_color)
    cell1.text_display(screen, str(cell1.index), index_text_size, background_color= highlight_color)