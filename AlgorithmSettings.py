import pygame

import AlgorithmSlides
import Settings
from Box import Box
from Color import Color
from Text import Text
import Functions
from Settings import screen as screen_settings

screen_size = screen_settings.screen_size

game_display = pygame.display.set_mode(screen_size)
#gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Maze')
pygame.init()

text_color = Color.navy
text_color_light = Color.navy_light
text_color_inprogress = Color.grey
text_size = 25

def set():
    """

    """
    maze_size = Settings.maze_size

    game_display.fill(Color.white)
    text_title = Text((int(screen_size[0] * 0.5), int(screen_size[1] * 0.1)), 'Algorithm settings', int(text_size * 3), text_color, text_color_light)
    #       column1     column2     column3     column4
    # row1 generation algoritms | solving algorithms
    # row2  kruskal |   box     | A*        |    box
    # row3  prim    |   box     | lefthand  |    box
    # row4  backtr. |   box     | tremaux   |    box
    # row5  eller   |   box     | endfiller |    box

    column_title1_position = int(screen_size[0] * 0.325)
    column_title2_position = int(screen_size[0] * 0.7)
    column1_position = int(screen_size[0] * 0.25)
    column2_position = int(screen_size[0] * 0.4)
    column3_position = int(screen_size[0] * 0.65)
    column4_position = int(screen_size[0] * 0.8)

    row1_position = int(screen_size[1] * 0.25)
    row2_position = int(screen_size[1] * 0.35)
    row3_position = int(screen_size[1] * 0.45)
    row4_position = int(screen_size[1] * 0.55)
    row5_position = int(screen_size[1] * 0.65)

    text_size_column_title = int(text_size * 2)
    text_algorithm_size = int(text_size * 1.5)

    # 1. row
    text_generation_algorithms = Text((column_title1_position, row1_position), 'Generation algorithms', text_size_column_title, text_color, text_color_light)
    text_solving_algoriths = Text((column_title2_position, row1_position), 'Solving algorithms', text_size_column_title, text_color, text_color_light)

    # 2. row
    text_kruskal = Text((column1_position, row2_position), 'Kruskal', text_size, text_color, text_color_light)
    box_kruskal = Box((column2_position, row2_position), text_size, text_color, text_color_light, is_active=True)
    text_astar = Text((column3_position, row2_position), 'A*', text_size, text_color, text_color_light)
    box_astar = Box((column4_position, row2_position), text_size, text_color, text_color_light, is_active=True)

    # 2. row
    text_prim = Text((column1_position, row3_position), 'Prim', text_size, text_color, text_color_light)
    box_prim = Box((column2_position, row3_position), text_size, text_color, text_color_light, is_active=True)
    text_lefthand = Text((column3_position, row3_position), 'Lefthands rule', text_size, text_color, text_color_light)
    box_lefthand = Box((column4_position, row3_position), text_size, text_color, text_color_light, is_active=True)

    # 4. row
    text_backtracker = Text((column1_position, row4_position), 'Backtracker', text_size, text_color, text_color_light)
    box_backtracker = Box((column2_position, row4_position), text_size, text_color, text_color_light, is_active=True)
    text_tremaux = Text((column3_position, row4_position), 'Tremaux', text_size, text_color_inprogress, text_color_light)
    box_tremaux = Box((column4_position, row4_position), text_size, text_color_inprogress, text_color_light, is_active=True)

    # 5. row
    text_eller = Text((column1_position, row5_position), 'Eller', text_size, text_color_inprogress, text_color_light)
    box_eller = Box((column2_position, row5_position), text_size, text_color_inprogress, text_color_light, is_active=True)
    text_endfiller = Text((column3_position, row5_position), 'Endfiller', text_size, text_color_inprogress, text_color_light)
    box_endfiller = Box((column4_position, row5_position), text_size, text_color_inprogress, text_color_light, is_active=True)


    text_start = Text((screen_size[0] // 2, int(screen_size[1] * 0.8)), 'Start', int(text_size * 2.5), text_color, text_color_light)
    text_back = Text((screen_size[0] // 8, int(screen_size[1] * 0.9)), 'Back', text_size, text_color,
                     text_color_light)

    text_title.show(game_display)

    text_generation_algorithms.show(game_display)
    text_solving_algoriths.show(game_display)

    text_kruskal.show(game_display)
    box_kruskal.show(game_display)
    text_astar.show(game_display)
    box_astar.show(game_display)

    text_prim.show(game_display)
    box_prim.show(game_display)
    text_lefthand.show(game_display)
    box_lefthand.show(game_display)

    text_backtracker.show(game_display)
    box_backtracker.show(game_display)
    text_tremaux.show(game_display)
    box_tremaux.show(game_display)

    text_eller.show(game_display)
    box_eller.show(game_display)
    text_endfiller.show(game_display)
    box_endfiller.show(game_display)

    text_start.show(game_display)
    text_back.show(game_display)


    Functions.mouse_reset()

    slides_list = []

    while True:
        Functions.buttonpress_detect()

        if text_start.is_clicked():
            text_start.show_click(game_display)
            Functions.mouse_reset()
            AlgorithmSlides.set()

        if text_back.is_clicked() or Settings.back_to_menu:
            text_back.show_click(game_display)
            Settings.back_to_menu = True
            break

        Functions.mouse_reset()
        Functions.update_delay(10)




