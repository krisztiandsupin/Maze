import pygame.display

import Functions
from Slides import SlideFunctions
import Settings

from Color import Color
from Maze import Maze
from Text import Text
from Settings import screen as screen_settings

screen_size = screen_settings.screen_size

def prim_slide(screen, display_settings):
    text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'Prim Algorithm',
                      int(display_settings.title_size), display_settings.text_color)
    screen.fill(Color.white)
    text_title.show(screen)
    prim_slide1(screen)
    
def prim_slide1(screen):
    """

    """
    maze_prim = Maze(8, 'square', 'prim')
    maze_prim.create((screen_size[0] // 4, screen_size[1] // 2), graph_bool=True)
    maze_prim.draw_grid(screen, graph_bool=True, cell_text_bool=True, cell_text_type=1)
    maze_prim.draw_frame(screen)
    pygame.display.update()

    SlideFunctions.slide_animation(screen, maze_prim)

    Functions.update_delay(500)
    maze_prim.draw(screen, True, False)