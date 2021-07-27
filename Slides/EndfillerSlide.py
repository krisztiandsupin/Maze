import Functions
import MazeFunctions
import Settings

from Color import Color
from Text import Text
from Settings import screen as screen_settings
from Slides import SlideFunctions

screen_size = screen_settings.screen_size


def endfiller_slide(screen, display_settings, maze_solve):
    text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'A* Algorithm',
                      int(display_settings.title_size), display_settings.text_color)
    screen.fill(Color.white)
    text_title.show(screen)
    endfiller_slide1(screen, maze_solve)


def endfiller_slide1(screen, maze_solve):
    """

    """
    maze_solve.draw(screen, visibility_bool=False)
    MazeFunctions.update_delay(1000)
    maze_solve.solve(algorithm='endfiller')

    maze_solve_highlight_cells = maze_solve.visited + maze_solve.solution_path

    step = 0
    while step < len(maze_solve_highlight_cells):
        Functions.buttonpress_detect()
        color = SlideFunctions.highlight_color_change(step, len(maze_solve.visited), Color.grey_light, Color.blue_light)

        if Settings.keyboard_space_press or Settings.keyboard_arrows_pressed() or Settings.keyboard_wsad_pressed():
            Functions.buttonpress_reset()

            while not Settings.keyboard_space_press:
                color = SlideFunctions.highlight_color_change(step, len(maze_solve.visited),
                                                              Color.grey_light, Color.blue_light)

                if (Settings.keyboard_right_press or Settings.keyboard_d_press) and \
                        step < len(maze_solve_highlight_cells):
                    maze_solve_highlight_cells[step].color(screen, color, graph_bool=True)
                    step += 1

                elif (Settings.keyboard_left_press or Settings.keyboard_a_press) and step > 0:
                    maze_solve_highlight_cells[step - 1].color(screen, maze_solve.color_background, graph_bool=True)
                    step -= 1

                Functions.buttonpress_reset()
                maze_solve.draw_frame(screen)
                MazeFunctions.update_delay(100)
                Functions.buttonpress_detect()

        Functions.buttonpress_reset()
        maze_solve_highlight_cells[step].color(screen, color, graph_bool=True)
        maze_solve.draw_frame(screen)
        MazeFunctions.update_delay(100)
        step += 1
