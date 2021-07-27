import pygame

import Functions

from Color import Color
from Maze import Maze
from Settings import screen
from Text import Text

# used in slide evaluation
from Slides import KruskalSlide
from Slides import PrimSlide
from Slides import BacktrackerSlide
from Slides import AstarSlide
from Slides import EndfillerSlide

screen_size = screen.screen_size

algorithm_display = pygame.display.set_mode(screen_size)
# gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Maze')
pygame.init()


def slides_set(selected_algorithms, display_settings):
    """

    """
    algorithm_display.fill(Color.white)
    text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'Algorithms',
                      int(display_settings.text_size * 1.5), display_settings.text_color,
                      display_settings.text_color_light)
    text_title.show(algorithm_display)

    generation_algoritms = selected_algorithms['generation']
    solving_algoritms = selected_algorithms['solving']

    while True:
        # generation algorithms
        for algorithm in generation_algoritms.keys():
            if generation_algoritms[algorithm]:
                slidename = f"{str(algorithm).capitalize()}Slide.{algorithm}_slide(algorithm_display, display_settings)"
                print(slidename)
                eval(slidename)

                Functions.update_delay(1000)

        for algorithm in solving_algoritms.keys():
            maze_solve = Maze(8, 'square', 'kruskal')
            maze_solve.create((screen_size[0] // 4, screen_size[1] // 2), graph_bool=True)
            if solving_algoritms[algorithm]:
                slidename = f"{str(algorithm).capitalize()}Slide.{algorithm}_slide(algorithm_display, display_settings, maze_solve)"
                print(slidename)
                eval(slidename)

                Functions.update_delay(1000)
