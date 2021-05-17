import Functions
import MazeFunctions

from Color import Color
from Maze import Maze
from Text import Text
from Settings import screen as screen_settings

screen_size = screen_settings.screen_size

def backtracker_slide(screen, display_settings):
    text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'Backtracker Algorithm',
                      int(display_settings.title_size), display_settings.text_color)
    screen.fill(Color.white)
    text_title.show(screen)

    screen.fill(Color.white)
    text_title.show(screen)