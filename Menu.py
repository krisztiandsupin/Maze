import pygame

import Functions
import Algorithms
import GameSettings
from Color import Color
from Settings import screen as screen_settings
import Settings
from Text import Text
from Maze import Maze

import MazeFunctions

screen_size = screen_settings.screen_size

#Screen size
gameDisplay = pygame.display.set_mode(screen_size)
#gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Maze')
pygame.init()

print('\nMAZE_MENU\n--------------')

text_color = Color.navy
text_color_light = Color.navy_light
text_size = 50

gameDisplay.fill(Color.white)
text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'Mazes', int(text_size * 1.5), text_color, text_color_light)
text_algorithm = Text((screen_size[0] // 2, int(screen_size[1] * 0.3)), 'Algorithms', text_size, text_color, text_color_light)
text_game = Text((screen_size[0] // 2, int(screen_size[1] * 0.4)), 'Game', text_size, text_color, text_color_light)
text_exit = Text((screen_size[0] // 2, int(screen_size[1] * 0.8)), 'Exit', text_size, text_color, text_color_light)

Algorithms.settings()

def menu_set():
    gameDisplay.fill(Color.white)
    maze_background = Maze(15, 'circle', 'kruskal')
    maze_background.color_line = Color.grey_light
    maze_background.color_start = Color.white
    maze_background.color_end = Color.white

    maze_background.create((screen_size[0] // 2, screen_size[1] // 2), 1, graph_bool=False)
    maze_background.draw(gameDisplay, graph_bool=False, visibility_bool=False)

    text_title.show(gameDisplay)
    text_algorithm.show(gameDisplay)
    text_game.show(gameDisplay)
    text_exit.show(gameDisplay)


menu_set()
Algorithms.settings()
# Algorithms.test()

while True:
    Functions.buttonpress_detect()

    if text_algorithm.is_clicked():
        text_algorithm.show_click(gameDisplay)
        Functions.mouse_reset()
        Algorithms.settings()

    if text_game.is_clicked():
        text_game.show_click(gameDisplay)
        Functions.mouse_reset()
        GameSettings.settings()

    if text_exit.is_clicked():
        pygame.quit()
        raise SystemExit

    if Settings.back_to_menu:
        menu_set()
        Settings.back_to_menu = False

    Functions.mouse_reset()
    MazeFunctions.updete_delay(10)