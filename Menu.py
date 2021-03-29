import time

import pygame

import AlgorithmSettings
import Functions
import GameSettings
import MazeFunctions
import Settings
from Color import Color
from Maze import Maze
from Settings import screen as screen_settings
from Text import Text

screen_size = screen_settings.screen_size

# Screen size
gameDisplay = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Maze')
pygame.init()

print('\nMAZE_MENU\n--------------')

text_color = Color.navy
text_color_light = Color.navy_light
text_size = 50

gameDisplay.fill(Color.white)
text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'Mazes', int(text_size * 1.5),
                  text_color, text_color_light)
text_algorithm = Text((screen_size[0] // 2, int(screen_size[1] * 0.3)), 'Algorithms', text_size,
                      text_color, text_color_light)
text_game = Text((screen_size[0] // 2, int(screen_size[1] * 0.4)), 'Game', text_size,
                 text_color, text_color_light)
text_exit = Text((screen_size[0] // 2, int(screen_size[1] * 0.8)), 'Exit', text_size,
                 text_color, text_color_light)


def menu_set():
    """

    """
    gameDisplay.fill(Color.white)
    start_time = time.time()
    maze_background1 = Maze(15, 'hexagon', 'kruskal')
    maze_background1.color_line = Color.grey_light
    maze_background1.color_start = Color.white
    maze_background1.color_end = Color.white
    maze_background1.color_frame = Color.grey_dark

    maze_background2 = Maze(15, 'circle', 'kruskal')
    maze_background2.color_line = Color.grey_extra_light
    maze_background2.color_start = Color.white
    maze_background2.color_end = Color.white
    maze_background2.color_frame = Color.grey_light

    maze_background3 = Maze(15, 'square', 'kruskal')
    maze_background3.color_line = Color.grey_extra_light
    maze_background3.color_start = Color.white
    maze_background3.color_end = Color.white
    maze_background3.color_frame = Color.grey_light

    maze_background2.create((int(screen_size[0] * 0.3), screen_size[1] // 2), 1, graph_bool=False,
                            cell_size_constant=1.25)
    maze_background2.draw(gameDisplay, graph_bool=False, visibility_bool=False)

    maze_background3.create((int(screen_size[0] * 0.7), screen_size[1] // 2), 1, graph_bool=False,
                            cell_size_constant=1.25)
    maze_background3.draw(gameDisplay, graph_bool=False, visibility_bool=False)

    maze_background1.create((screen_size[0] // 2, screen_size[1] // 2), 1, graph_bool=False, cell_size_constant=1.6)
    maze_background1.draw(gameDisplay, graph_bool=False, visibility_bool=False)

    end_time = time.time()
    print(f"runtime: {end_time - start_time:.2f}")

    text_title.show(gameDisplay)
    text_algorithm.show(gameDisplay)
    text_game.show(gameDisplay)
    text_exit.show(gameDisplay)


'''def menu_set_from_file():
    gameDisplay.fill(Color.white)
    maze_background2 = MazeFromFile.read_from_file("maze_background.txt")
    maze_background2.color_line = Color.red_light
    maze_background2.color_start = Color.white
    maze_background2.color_end = Color.white

    maze_background2.create((screen_size[0] // 2, screen_size[1] // 2), 1, graph_bool=False)
    maze_background2.draw(gameDisplay, graph_bool=False, visibility_bool=False)

    text_title.show(gameDisplay)
    text_algorithm.show(gameDisplay)
    text_game.show(gameDisplay)
    text_exit.show(gameDisplay)'''

# Algorithms.kruskal_slide1()
menu_set()

while True:
    Functions.buttonpress_detect()

    if text_algorithm.is_clicked():
        text_algorithm.show_click(gameDisplay)
        Functions.mouse_reset()
        AlgorithmSettings.set()

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
