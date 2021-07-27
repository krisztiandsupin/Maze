import Functions
import MazeFunctions
import Settings
from Color import Color
from Settings import maze as maze_settings


def highlight_edge_delete(display, maze, cell0, cell1, highlight_color, graph_bool, index_text_size, step):
    """

    :maze_type highlight_color: tuple
    :param display:
    :param maze:
    :param cell0:
    :param cell1:
    :param highlight_color:
    :param graph_bool:
    :param index_text_size:
    :param step:
    """
    cell0.color_grid(display, highlight_color, graph_bool, line_color=Color.black,
                     coordinate_text_bool=False, walls_bool=maze.maze_cell_borders[step][0])
    cell1.color_grid(display, highlight_color, graph_bool, line_color=Color.black, coordinate_text_bool=False,
                     walls_bool=maze.maze_cell_borders[step][1])
    cell0.text_display(display, str(cell0.index), index_text_size, background_color=highlight_color)
    cell1.text_display(display, str(cell1.index), index_text_size, background_color=highlight_color)


def highlight_edge(screen, maze, step, highlight_color, index_text_size, delay):
    cell0, cell1 = maze.maze_order[step][0], maze.maze_order[step][1]

    highlight_edge_delete(screen, maze, cell0, cell1, highlight_color, True, index_text_size,
                          step)

    Functions.update_delay(delay)


def delete_edge(screen, maze, step, highlight_color, index_text_size, delay):
    cell0, cell1 = maze.maze_order[step][0], maze.maze_order[step][1]
    MazeFunctions.edge_color(screen, (cell0, cell1), highlight_color, graph=True,
                             graph_color=maze.color_line)
    highlight_edge_delete(screen, maze, cell0, cell1, maze.color_background, True,
                          index_text_size, step)
    MazeFunctions.edge_color(screen, (cell0, cell1), maze.color_background, graph=True,
                             graph_color=maze.color_line)

    maze.draw_frame(screen)

    if delay > 0:
        Functions.update_delay(delay)


def redraw_edge(screen, maze, step, highlight_color, index_text_size, delay):
    cell0, cell1 = maze.maze_order[step - 1][0], maze.maze_order[step - 1][1]

    MazeFunctions.edge_color(screen, (cell0, cell1), maze.color_line, graph=True,
                             graph_color=maze.color_background)

    cell0.color_border_points(screen, maze.color_line)
    cell0.color_graph(screen, maze.color_line, maze_settings.graph_cell_size)
    cell1.color_border_points(screen, maze.color_line)
    cell1.color_graph(screen, maze.color_line, maze_settings.graph_cell_size)
    maze.draw_frame(screen)

    if delay > 0:
        Functions.update_delay(delay)


def draw_candidates(screen, maze, step, highlight_color, index_text_size, delay):
    for (cell_index, cell_walls_bool) in maze.maze_candidates[step]:
        cell = maze.cell_list[cell_index]
        cell.color_grid(screen, highlight_color, graph_bool=True, line_color=Color.black,
                        coordinate_text_bool=False, walls_bool=cell_walls_bool)
        cell.text_display(screen, str(cell.index), index_text_size, background_color=highlight_color)

    maze.draw_frame(screen)
    if delay > 0:
        Functions.update_delay(delay)


def slide_manual(screen, maze, step, highlight_color, index_text_size, delay, candidates_bool=True):
    Functions.buttonpress_reset()
    highlight_counter = 0

    while not Settings.keyboard_space_press:
        Functions.buttonpress_detect()
        if candidates_bool:
            if (Settings.keyboard_right_press or Settings.keyboard_d_press) and step < len(maze.maze_order):
                if highlight_counter % 3 == 0 and (step < len(maze.maze_order) - 1):
                    draw_candidates(screen, maze, step, Color.salmon_light, index_text_size, delay)
                elif highlight_counter % 3 == 1 and (step < len(maze.maze_order) - 1):
                    highlight_edge(screen, maze, step, highlight_color, index_text_size, delay)
                else:
                    delete_edge(screen, maze, step, highlight_color, index_text_size, delay)
                    draw_candidates(screen, maze, step, Color.white, index_text_size, delay=0)
                    delete_edge(screen, maze, step, Color.white, index_text_size, delay=0)
                    step += 1

                highlight_counter += 1
                Functions.buttonpress_reset()

            elif Settings.keyboard_left_press or Settings.keyboard_a_press:
                if step < len(maze.maze_order) and highlight_counter % 2 == 1:
                    delete_edge(screen, maze, step, highlight_color, index_text_size, 0)
                draw_candidates(screen, maze, step, Color.white, index_text_size, delay)
                draw_candidates(screen, maze, step - 1, Color.salmon_light, index_text_size, delay)

                redraw_edge(screen, maze, step, highlight_color, index_text_size, delay)
                if step > 1:
                    step -= 1
                Functions.buttonpress_reset()

        else:
            if (Settings.keyboard_right_press or Settings.keyboard_d_press) and step < len(maze.maze_order):
                if highlight_counter % 2 == 0 and (step < len(maze.maze_order) - 1):
                    highlight_edge(screen, maze, step, highlight_color, index_text_size, delay)
                else:
                    delete_edge(screen, maze, step, highlight_color, index_text_size, delay)

                    step += 1

                highlight_counter += 1
                Functions.buttonpress_reset()

            elif Settings.keyboard_left_press or Settings.keyboard_a_press:
                if step < len(maze.maze_order) and highlight_counter % 2 == 1:
                    delete_edge(screen, maze, step, highlight_color, index_text_size, 0)
                draw_candidates(screen, maze, step, Color.white, index_text_size, delay)
                draw_candidates(screen, maze, step - 1, Color.salmon_light, index_text_size, delay)

                redraw_edge(screen, maze, step, highlight_color, index_text_size, delay)
                if step > 1:
                    step -= 1
                Functions.buttonpress_reset()

    return step


def slide_animation(screen, maze, highlight_color=Color.red_light, index_text_size=15, delay=100, candidates_bool=True):
    step = 0
    while step < len(maze.maze_order):
        Functions.buttonpress_detect()
        # manual displaying
        if Settings.keyboard_space_press or Settings.keyboard_arrows_pressed() or Settings.keyboard_wsad_pressed():
            slide_manual(screen, maze, step, highlight_color, index_text_size, delay, candidates_bool)

        Functions.buttonpress_reset()

        # automatic displaying
        if step < len(maze.maze_order):
            if candidates_bool:
                draw_candidates(screen, maze, step, Color.salmon_light, index_text_size, delay)
            highlight_edge(screen, maze, step, highlight_color, index_text_size, 5 * delay)
            delete_edge(screen, maze, step, highlight_color, index_text_size, delay)
            Functions.update_delay(delay)

            if candidates_bool:
                draw_candidates(screen, maze, step, maze.color_background, index_text_size, delay=0)
                delete_edge(screen, maze, step, highlight_color, index_text_size, delay=0)

            step += 1

    Functions.update_delay(500)
    maze.draw(screen, True, False)

def highlight_color_change(actual_index, limit_index, first_color=Color.gold_light, second_color=Color.blue_light):
    if actual_index >= limit_index:
        return second_color
    return first_color