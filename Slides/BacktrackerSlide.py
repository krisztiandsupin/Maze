import pygame.display

import Functions

from Color import Color
from Maze import Maze
from Slides import SlideFunctions
from Text import Text
from Settings import screen as screen_settings

screen_size = screen_settings.screen_size

def backtracker_slide(screen, display_settings):
    text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'Backtracker Algorithm',
                      int(display_settings.title_size), display_settings.text_color)
    screen.fill(Color.white)
    text_title.show(screen)
    backtracker_slide1(screen)


def backtracker_slide1(screen):
    """

    """
    maze_backtracker = Maze(8, 'square', 'backtracker')
    maze_backtracker.create((screen_size[0] // 4, screen_size[1] // 2), graph_bool=True)
    maze_backtracker.draw_grid(screen, graph_bool=True, cell_text_bool=True, cell_text_type=1)
    pygame.display.update()

    maze_backtracker.draw_frame(screen)

    SlideFunctions.slide_animation(screen, maze_backtracker)

    Functions.update_delay(500)
    maze_backtracker.draw(screen, True, False)