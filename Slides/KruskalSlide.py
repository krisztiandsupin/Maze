import Functions
import MazeFunctions

from Color import Color
from Maze import Maze
from Slides import SlideFunctions
from Text import Text
from Settings import screen as screen_settings

screen_size = screen_settings.screen_size

def kruskal_slide(screen, display_settings):
    text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'Kruskal Algorithm',
                      int(display_settings.title_size), display_settings.text_color)
    screen.fill(Color.white)
    text_title.show(screen)
    kruskal_slide1(screen)

    # screen.fill(Color.white)
    # text_title.show(screen)
    # kruskal_slide2(screen)

def kruskal_slide1(screen):
    """

    """
    maze_kruskal = Maze(8, 'square', 'kruskal')
    maze_kruskal.create((screen_size[0] // 4, screen_size[1] // 2), graph_bool=True)
    maze_kruskal.draw_grid(screen, graph_bool=True, cell_text_bool=True, cell_text_type=1)

    maze_kruskal.draw_frame(screen)

    SlideFunctions.slide_animation(screen, maze_kruskal, candidates_bool=False)


    Functions.update_delay(500)
    maze_kruskal.draw(screen, True, False)


def kruskal_slide2(screen):
    """

    """
    maze_kruskal_hexagon = Maze(5, 'hexagon', 'kruskal')
    maze_kruskal_hexagon.create((screen_size[0] // 4, screen_size[1] // 2),
                                graph_bool=False)
    maze_kruskal_hexagon.draw_grid(screen, graph_bool=False, cell_text_bool=True, cell_text_type=1)
    maze_kruskal_hexagon.draw_frame(screen)

    maze_kruskal_circle = Maze(5, 'circle', 'kruskal')
    maze_kruskal_circle.create(((3 * screen_size[0]) // 4, screen_size[1] // 2),
                               graph_bool=False)
    maze_kruskal_circle.draw_grid(screen, graph_bool=False, cell_text_bool=True, cell_text_type=1)
    maze_kruskal_circle.draw_frame(screen)

    highlight_color = Color.red_light
    delay = 10
    index_text_size = 15

    for i in range(0, min(len(maze_kruskal_hexagon.maze_order), len(maze_kruskal_circle.maze_order))):
        cell0_hexagon, cell1_hexagon = maze_kruskal_hexagon.maze_order[i][0], maze_kruskal_hexagon.maze_order[i][1]

        MazeFunctions.highlight_edge_delete(screen, maze_kruskal_hexagon, cell0_hexagon, cell1_hexagon, highlight_color,
                              False, index_text_size, i)

        cell0_circle, cell1_circle = maze_kruskal_circle.maze_order[i][0], maze_kruskal_circle.maze_order[i][1]

        MazeFunctions.highlight_edge_delete(screen, maze_kruskal_circle, cell0_circle, cell1_circle, highlight_color,
                              False, index_text_size, i)

        Functions.update_delay(delay)

        MazeFunctions.edge_color(screen, (cell0_hexagon, cell1_hexagon), highlight_color, graph=False)

        MazeFunctions.highlight_edge_delete(screen, maze_kruskal_hexagon, cell0_hexagon, cell1_hexagon,
                              maze_kruskal_hexagon.color_background, False,
                              index_text_size, i)
        MazeFunctions.edge_color(screen, (cell0_hexagon, cell1_hexagon),
                                 maze_kruskal_hexagon.color_background, graph=False)

        maze_kruskal_hexagon.draw_frame(screen)

        MazeFunctions.edge_color(screen, (cell0_circle, cell1_circle), highlight_color, graph=False)

        MazeFunctions.highlight_edge_delete(screen, maze_kruskal_circle, cell0_circle, cell1_circle,
                              maze_kruskal_circle.color_background, False,
                              index_text_size, i)
        MazeFunctions.edge_color(screen, (cell0_circle, cell1_circle), maze_kruskal_circle.color_background,
                                 graph=False)

        maze_kruskal_circle.draw_frame(screen)

        Functions.update_delay(delay)
        Functions.buttonpress_detect()

    for i in range(min(len(maze_kruskal_hexagon.maze_order), len(maze_kruskal_circle.maze_order)),
                   len(maze_kruskal_circle.maze_order)):
        cell0_circle, cell1_circle = maze_kruskal_circle.maze_order[i][0], maze_kruskal_circle.maze_order[i][1]

        MazeFunctions.highlight_edge_delete(screen, maze_kruskal_circle, cell0_circle, cell1_circle, highlight_color,
                              False,
                              index_text_size, i)
        Functions.update_delay(delay)
        MazeFunctions.edge_color(screen, (cell0_circle, cell1_circle), highlight_color, graph=False,
                                 )

        MazeFunctions.highlight_edge_delete(screen, maze_kruskal_circle, cell0_circle, cell1_circle,
                              maze_kruskal_circle.color_background, False, index_text_size, i)
        MazeFunctions.edge_color(screen, (cell0_circle, cell1_circle), maze_kruskal_circle.color_background,
                                 graph=False)

        maze_kruskal_circle.draw_frame(screen)

        Functions.update_delay(delay)
