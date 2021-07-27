import pygame

import Settings
from Box import Box
from Color import Color
from Text import Text
import Functions
import Game
from Settings import screen as screen_settings

screen_size = screen_settings.screen_size

game_display = pygame.display.set_mode(screen_size)
#gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Maze')
pygame.init()

text_color = Color.navy
text_color_light = Color.navy_light
text_size = 25


def settings():
    """

    """
    maze_size = Settings.maze_size

    game_display.fill(Color.white)
    text_title = Text((int(screen_size[0] * 0.5), int(screen_size[1] * 0.1)), 'Maze game', int(text_size * 3), text_color, text_color_light)

    game_mode_vertical = int(screen_size[1] * 0.3)

    text_mode = Text((int(screen_size[0] * 0.3), game_mode_vertical), 'Game mode', int(text_size * 1.5), text_color,
                          text_color_light)
    text_single_player = Text((int(screen_size[0] * 0.58), game_mode_vertical), 'Single player', int(text_size * 1.25),
                     text_color,
                     text_color_light)

    text_multiplayer = Text((int(screen_size[0] * 0.72), game_mode_vertical), 'Multiplayer', int(text_size * 1.25),
                     text_color,
                     text_color_light)
    text_slash = Text((int(screen_size[0] * 0.65), game_mode_vertical), '/', int(text_size * 1.35), text_color,
                            text_color_light)


    text_computer = Text((int(screen_size[0] * 0.3), int(screen_size[1] * 0.4)), 'Computer', int(text_size * 1.5), text_color, text_color_light)
    ai_box = Box((int(screen_size[0] * 0.65), int(screen_size[1] * 0.4)), int(text_size * 1.25), text_color, text_color_light, Settings.ai_mode)

    text_visibility_vertical = int(screen_size[1] * 0.5)

    text_visibility = Text((int(screen_size[0] * 0.3), text_visibility_vertical), 'Invisible mode', int(text_size * 1.5),
                         text_color, text_color_light)
    visibility_box = Box((int(screen_size[0] * 0.65), text_visibility_vertical), int(text_size * 1.25), text_color,
                         text_color_light, Settings.invisible_mode)

    # maze maze_type
    maze_type_vertical = int(screen_size[1] * 0.6)

    text_type = Text((int(screen_size[0] * 0.3), maze_type_vertical), 'Maze maze_type', int(text_size * 1.5), text_color,
                     text_color_light)
    text_square = Text((int(screen_size[0] * 0.58), maze_type_vertical), 'Square', int(text_size * 1.25),
                              text_color,
                              text_color_light)

    text_hexagon = Text((int(screen_size[0] * 0.72), maze_type_vertical), 'Hexagon', int(text_size * 1.25),
                            text_color_light,
                            text_color)
    text_slash2 = Text((int(screen_size[0] * 0.65), maze_type_vertical), '/', int(text_size * 1.35), text_color,
                      text_color_light)

    # maze size line
    maze_size_vertical = int(screen_size[1] * 0.7)
    text_maze_size = Text((int(screen_size[0] * 0.3), maze_size_vertical), 'Maze size', int(text_size * 1.5), text_color, text_color_light)
    text_maze_size_actual = Text((int(screen_size[0] * 0.65), maze_size_vertical), '{0}'.format(maze_size), int(text_size * 1.5),
                          text_color, text_color_light)
    text_maze_minus = Text((int(screen_size[0] * 0.62), maze_size_vertical), '-', int(text_size * 1.6),
                          text_color_light, text_color)
    text_maze_plus = Text((int(screen_size[0] * 0.68), maze_size_vertical), '+', int(text_size * 1.6),
                           text_color_light, text_color)

    text_start = Text((screen_size[0] // 2, int(screen_size[1] * 0.8)), 'Start', int(text_size * 2.5), text_color, text_color_light)
    text_back = Text((screen_size[0] // 8, int(screen_size[1] * 0.9)), 'Back', text_size, text_color,
                     text_color_light)

    text_title.show(game_display)
    text_mode.show(game_display)
    text_single_player.show(game_display)
    text_slash.show(game_display)
    text_multiplayer.show(game_display, text_color_light)

    text_computer.show(game_display)
    ai_box.show(game_display)
    text_visibility.show(game_display)
    visibility_box.show(game_display)

    text_type.show(game_display)
    text_square.show(game_display)
    text_slash2.show(game_display)
    text_hexagon.show(game_display)

    text_maze_size.show(game_display)
    text_maze_size_actual.show(game_display)
    text_maze_plus.show(game_display)
    text_maze_minus.show(game_display)

    text_start.show(game_display)
    text_back.show(game_display)

    Functions.mouse_reset()

    while True:
        Functions.buttonpress_detect()

        if text_maze_minus.is_clicked() and Settings.maze_size > 10  and Settings.maze_size <= 50:
            text_maze_minus.show_click(game_display)
            Settings.maze_size -= 1
            text_maze_size_actual.text = '{0}'.format(Settings.maze_size)
            text_maze_size_actual.show(game_display)
            Functions.mouse_reset()

        if text_maze_plus.is_clicked() and Settings.maze_size >= 10 and Settings.maze_size < 50:
            text_maze_plus.show_click(game_display)
            Settings.maze_size += 1
            text_maze_size_actual.text = '{0}'.format(Settings.maze_size)
            text_maze_size_actual.show(game_display)
            Functions.mouse_reset()

        if text_single_player.is_clicked() and not Settings.player_mode:
            text_single_player.show(game_display, text_color)
            text_multiplayer.show(game_display, text_color_light)

            text_computer.show(game_display, text_color)
            ai_box.show_click(game_display)

            Settings.player_mode = True
            Settings.game_mode = Settings.game_mode_calculate()

        if text_multiplayer.is_clicked() and Settings.player_mode:
            text_single_player.show(game_display, text_color_light)
            text_multiplayer.show(game_display, text_color)

            text_computer.show(game_display, Color.grey)
            ai_box.show(game_display, Color.grey)

            Settings.player_mode = False
            Settings.game_mode = Settings.game_mode_calculate()

        if ai_box.is_clicked() and Settings.player_mode:
            Settings.ai_mode = not Settings.ai_mode
            ai_box.is_active = not ai_box.is_active

            ai_box.show_click(game_display)
            Settings.game_mode = Settings.game_mode_calculate()

        if visibility_box.is_clicked():
            Settings.invisible_mode = not Settings.invisible_mode
            visibility_box.is_active = not visibility_box.is_active

            visibility_box.show_click(game_display)
            Settings.game_mode = Settings.game_mode_calculate()

        if text_start.is_clicked():
            text_start.show_click(game_display)
            Functions.mouse_reset()
            Game.generation()

        if text_back.is_clicked() or Settings.back_to_menu:
            text_back.show_click(game_display)
            Settings.back_to_menu = True
            break

        if text_square.is_clicked() and Settings.maze_type != 'square':
            text_hexagon.show(game_display, text_color_light)
            text_square.show(game_display, text_color)

            Settings.maze_type = 'square'

        if text_hexagon.is_clicked() and Settings.maze_type != 'hexagon':
            text_hexagon.show(game_display, text_color)
            text_square.show(game_display, text_color_light)

            Settings.maze_type = 'hexagon'

        Functions.mouse_reset()
        Functions.update_delay(10)




