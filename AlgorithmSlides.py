import pygame

import Functions

from Color import Color
from Settings import screen
from Text import Text
import KruskalSlide

screen_size = screen.screen_size

algorithm_display = pygame.display.set_mode(screen_size)
# gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Maze')
pygame.init()

text_color = Color.navy
text_color_light = Color.navy_light
text_size = 50


def set():
    """

    """
    algorithm_display.fill(Color.white)
    text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'Algorithms', int(text_size * 1.5), text_color,
                      text_color_light)
    text_title.show(algorithm_display)

    while True:
        KruskalSlide.kruskal_slide1(algorithm_display)
        KruskalSlide.kruskal_slide2(algorithm_display)
        Functions.update_delay(1000)


