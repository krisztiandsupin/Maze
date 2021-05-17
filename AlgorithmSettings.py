import pygame

import AlgorithmSlides
import Settings
from Box import Box
from Color import Color
from Text import Text
import Functions
from Settings import screen as screen_settings
from DisplaySettings import DisplaySettings

screen_size = screen_settings.screen_size

game_display = pygame.display.set_mode(screen_size)
# gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Maze')
pygame.init()


def algorithms_set():
    """

    """
    display_settings = DisplaySettings()

    game_display.fill(Color.white)
    text_title = Text((int(screen_size[0] * 0.5), int(screen_size[1] * 0.1)), 'Algorithm settings',
                      int(display_settings.title_size),
                      display_settings.text_color, display_settings.text_color_light)
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

    display_settings.text_size_column_title = int(display_settings.text_size * 2)

    # 1. row
    text_generation_algorithms = Text((column_title1_position, row1_position), 'Generation algorithms',
                                      display_settings.text_size_column_title,
                                      display_settings.text_color, display_settings.text_color_light)
    text_solving_algoriths = Text((column_title2_position, row1_position), 'Solving algorithms',
                                  display_settings.text_size_column_title,
                                  display_settings.text_color, display_settings.text_color_light)

    # 2. row
    text_kruskal = Text((column1_position, row2_position), 'Kruskal', display_settings.text_size,
                        display_settings.text_color, display_settings.text_color_light)
    box_kruskal = Box((column2_position, row2_position), display_settings.text_size,
                      display_settings.text_color, display_settings.text_color_light, is_active=True)
    text_astar = Text((column3_position, row2_position), 'A*', display_settings.text_size,
                      display_settings.text_color, display_settings.text_color_light)
    box_astar = Box((column4_position, row2_position), display_settings.text_size,
                    display_settings.text_color, display_settings.text_color_light, is_active=False)

    # 2. row
    text_prim = Text((column1_position, row3_position), 'Prim', display_settings.text_size,
                     display_settings.text_color, display_settings.text_color_light)
    box_prim = Box((column2_position, row3_position), display_settings.text_size,
                   display_settings.text_color, display_settings.text_color_light, is_active=True)
    text_lefthand = Text((column3_position, row3_position), 'Lefthands rule', display_settings.text_size,
                         display_settings.text_color, display_settings.text_color_light)
    box_lefthand = Box((column4_position, row3_position), display_settings.text_size,
                       display_settings.text_color, display_settings.text_color_light, is_active=False)

    # 4. row
    text_backtracker = Text((column1_position, row4_position), 'Backtracker', display_settings.text_size,
                            display_settings.text_color, display_settings.text_color_light)
    box_backtracker = Box((column2_position, row4_position), display_settings.text_size,
                          display_settings.text_color, display_settings.text_color_light, is_active=True)
    text_tremaux = Text((column3_position, row4_position), 'Tremaux', display_settings.text_size,
                        display_settings.text_color_inprogress, display_settings.text_color_light)
    box_tremaux = Box((column4_position, row4_position), display_settings.text_size,
                      display_settings.text_color_inprogress, display_settings.text_color_light, is_active=False)

    # 5. row
    text_eller = Text((column1_position, row5_position), 'Eller', display_settings.text_size,
                      display_settings.text_color_inprogress, display_settings.text_color_light)
    box_eller = Box((column2_position, row5_position), display_settings.text_size,
                    display_settings.text_color_inprogress, display_settings.text_color_light, is_active=False)
    text_endfiller = Text((column3_position, row5_position), 'Endfiller', display_settings.text_size,
                          display_settings.text_color_inprogress, display_settings.text_color_light)
    box_endfiller = Box((column4_position, row5_position), display_settings.text_size,
                        display_settings.text_color_inprogress, display_settings.text_color_light, is_active=False)

    text_start = Text((screen_size[0] // 2, int(screen_size[1] * 0.8)), 'Start', int(display_settings.text_size * 2.5),
                      display_settings.text_color, display_settings.text_color_light)
    text_back = Text((screen_size[0] // 8, int(screen_size[1] * 0.9)), 'Back', display_settings.text_size,
                     display_settings.text_color,
                     display_settings.text_color_light)

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

    # clickable boxes
    box_list = (box_kruskal, box_prim, box_backtracker, box_astar)
    Functions.mouse_reset()

    while True:
        Functions.buttonpress_detect()

        if text_start.is_clicked():
            text_start.show_click(game_display)
            Functions.mouse_reset()

            selected_algorithms = {
                'generation': {
                    'kruskal': box_kruskal.is_active,
                    'prim': box_prim.is_active,
                    'backtracker': box_backtracker.is_active,
                    'eller': box_eller.is_active},
                'solving': {
                    'astar': box_astar.is_active,
                    'lefthand_rule': box_lefthand.is_active,
                    'tremaux': box_tremaux.is_active,
                    'endfiller': box_endfiller.is_active,
                }
            }

            AlgorithmSlides.slides_set(selected_algorithms, display_settings)

        for box in box_list:
            if box.is_clicked():
                box.change_active()
                box.show_click(game_display)

        if text_back.is_clicked() or Settings.back_to_menu:
            text_back.show_click(game_display)
            Settings.back_to_menu = True
            break

        Functions.mouse_reset()
        Functions.update_delay(10)
