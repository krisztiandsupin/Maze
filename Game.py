import copy
import time

import pygame

import Settings
import MazeFunctions
from Color import Color
from Text import Text
import Functions
from Maze import Maze
from Settings import screen as screen_settings

screen_size = screen_settings.screen_size

game_display = pygame.display.set_mode(screen_size)
#gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Maze')
pygame.init()

text_color = Color.navy
text_color_light = Color.navy_light
text_size = 50


def generation():
    print(Settings.ai_bool)
    game_display.fill(Color.white)
    text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'Maze game', int(text_size * 1.5), text_color, text_color_light)
    text_title.show(game_display)

    maze_test = Maze(Settings.maze_size, 'square', 'kruskal')
    #maze_test = Maze(30, 'square', 'kruskal')

    if Settings.game_mode == 0 and Settings.ai_bool == False:
        maze_position = (Settings.screen.screen_size[0] // 2, Settings.screen.screen_size[1] // 2)

        maze_test.create(maze_position, 1, graph_bool=False)
        maze_test.draw(game_display, graph_bool=False, step_bool=False, delay=0)
        maze_test2 = None

    else:
        maze_position = (Settings.screen.screen_size[0] // 4, Settings.screen.screen_size[1] // 2)

        maze_test.create(maze_position, 1, graph_bool = False)
        maze_test.draw(game_display, graph_bool= False , step_bool = False, delay=0)

        maze_test2 = copy.deepcopy(maze_test)
        maze_position2 = (3 * Settings.screen.screen_size[0] // 4, Settings.screen.screen_size[1] // 2)
        maze_test2.create(maze_position2, 1, graph_bool=False)
        maze_test2.draw(game_display, graph_bool=False, step_bool=False, delay=0)

    while True:
        maze_game(maze_test, maze_test2)
        maze_end()

        Settings.back_to_menu
        break

def maze_game(maze_test, maze_test2):
    player_position = maze_test.start
    player_color = Color.blue_dark
    pygame.draw.circle(game_display, player_color, player_position.position, int(maze_test.cell_size * 0.3))

    if Settings.game_mode == 1:
        player2_position = maze_test2.start
        player2_color = Color.green_dark
        pygame.draw.circle(game_display, player2_color, player2_position.position, int(maze_test.cell_size * 0.3))

    timer_position = (int(screen_size[0] * 0.5), int(screen_size[1] * 0.9))

    text_time = Text(timer_position, '0:00', int(text_size * 0.8), text_color, text_color_light)
    text_time.show(game_display)

    text_start = Text((int(screen_size[0] * 0.5), int(screen_size[1] * 0.5)), 'Press any arrow to start', \
                      int(text_size * 1), text_color, text_color_light)
    text_start.show(game_display)
    pygame.display.update()

    while True:
        Functions.buttonpress_detect()

        if Settings.keyboard_left_press or \
            Settings.keyboard_right_press or \
            Settings.keyboard_up_press or \
            Settings.keyboard_down_press or \
            Settings.keyboard_w_press or \
            Settings.keyboard_s_press or \
            Settings.keyboard_a_press or \
            Settings.keyboard_d_press:
            break

    text_start = Text((int(screen_size[0] * 0.5), int(screen_size[1] * 0.5)), 'Press any arrow to start', \
                      int(text_size * 1), Color.white, text_color_light)

    text_start.show(game_display)
    maze_test.draw(game_display, maze_test.position)
    pygame.draw.circle(game_display, player_color, player_position.position, int(maze_test.cell_size * 0.3))



    if Settings.game_mode == 0 and Settings.ai_bool == True or Settings.game_mode == 1:
        maze_test2.draw(game_display, maze_test2.position)
        maze_test2.solve('astar')
        ai_index = 0

    if Settings.game_mode == 1:
        pygame.draw.circle(game_display, player2_color, player2_position.position, int(maze_test2.cell_size * 0.3))

    time_start = time.time()
    time_sec = 0

    while True:
        time_current = time.time() - time_start
        time_temp = int(time_current)

        if time_temp > time_sec:
            time_sec = time_temp

            timer_sec = str(time_sec % 60)
            if len(timer_sec) < 2:
                timer_sec = '0' + timer_sec

            timer_min = str(time_sec // 60)

            text_time = Text(timer_position, '{0}:{1}'.format(timer_min, timer_sec), int(text_size * 0.8),
                              text_color, text_color_light)
            text_time.show(game_display)

        Functions.buttonpress_detect()

        new_index = player_position.index
        if Settings.game_mode == 1:
            new_index2 = player2_position.index


        if Settings.game_mode == 0:
            if Settings.keyboard_down_press or Settings.keyboard_s_press:
                if player_position.coordinate[0] < maze_test.size - 1:
                    new_index = MazeFunctions.coordinate_to_index_square((player_position.coordinate[0] + 1, \
                                                                          player_position.coordinate[1]), maze_test.size)

            if Settings.keyboard_up_press or Settings.keyboard_w_press:
                if player_position.coordinate[0] > 0:
                    new_index = MazeFunctions.coordinate_to_index_square((player_position.coordinate[0] - 1, \
                                                                          player_position.coordinate[1]), maze_test.size)

            if Settings.keyboard_left_press or Settings.keyboard_a_press:
                if player_position.coordinate[1] > 0:
                    new_index = MazeFunctions.coordinate_to_index_square((player_position.coordinate[0], \
                                                                          player_position.coordinate[1] - 1), maze_test.size)

            if Settings.keyboard_right_press or Settings.keyboard_d_press:
                if player_position.coordinate[1] < maze_test.size:
                    new_index = MazeFunctions.coordinate_to_index_square((player_position.coordinate[0], \
                                                                          player_position.coordinate[1] + 1), maze_test.size)

        elif Settings.game_mode == 1:
            # player1 movments with w,s,a,d
            if Settings.keyboard_s_press:
                if player_position.coordinate[0] < maze_test.size - 1:
                    new_index = MazeFunctions.coordinate_to_index_square((player_position.coordinate[0] + 1, \
                                                                          player_position.coordinate[1]), maze_test.size)

            if Settings.keyboard_w_press:
                if player_position.coordinate[0] > 0:
                    new_index = MazeFunctions.coordinate_to_index_square((player_position.coordinate[0] - 1, \
                                                                          player_position.coordinate[1]), maze_test.size)
            if Settings.keyboard_a_press:
                if player_position.coordinate[1] > 0:
                    new_index = MazeFunctions.coordinate_to_index_square((player_position.coordinate[0], \
                                                                          player_position.coordinate[1] - 1), maze_test.size)

            if Settings.keyboard_d_press:
                if player_position.coordinate[1] < maze_test.size:
                    new_index = MazeFunctions.coordinate_to_index_square((player_position.coordinate[0], \
                                                                          player_position.coordinate[1] + 1), maze_test.size)

            # player2 movements with arrows
            if Settings.keyboard_down_press:
                if player2_position.coordinate[0] < maze_test2.size - 1:
                    new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0] + 1, \
                                                                          player2_position.coordinate[1]), maze_test2.size)

            if Settings.keyboard_up_press:
                if player2_position.coordinate[0] > 0:
                    new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0] - 1, \
                                                                           player2_position.coordinate[1]),
                                                                          maze_test2.size)

            if Settings.keyboard_left_press:
                if player2_position.coordinate[1] > 0:
                    new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0], \
                                                                           player2_position.coordinate[1] - 1),
                                                                          maze_test2.size)
            if Settings.keyboard_right_press:
                if player2_position.coordinate[1] < maze_test.size:
                    new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0] , \
                                                                           player2_position.coordinate[1] + 1),
                                                                          maze_test2.size)


        if new_index in maze_test.maze_list[player_position.index]:
            pygame.draw.circle(game_display, Color.gold_light, player_position.position, int(maze_test.cell_size * 0.3))
            player_position = maze_test.cell_list[new_index]
            pygame.draw.circle(game_display, player_color, player_position.position,
                               int(maze_test.cell_size * 0.3))

            # check end conditions
            if player_position == maze_test.end:
                text_won = Text((int(screen_size[0] * 0.2), int(screen_size[1] * 0.9)), 'You won', int(text_size * 1.5),
                                  text_color, text_color_light)
                text_won.show(game_display)
                break

        if Settings.game_mode == 1 and new_index2 in maze_test2.maze_list[player2_position.index]:
            pygame.draw.circle(game_display, Color.gold_light, player2_position.position, int(maze_test2.cell_size * 0.3))
            player2_position = maze_test2.cell_list[new_index2]
            pygame.draw.circle(game_display, player2_color, player2_position.position,
                               int(maze_test2.cell_size * 0.3))

            # check end conditions
            if player2_position == maze_test2.end:
                text_won2 = Text((int(screen_size[0] * 0.8), int(screen_size[1] * 0.9)), 'You won', int(text_size * 1.5),
                                  player2_color, text_color_light)
                text_won2.show(game_display)
                break

        if Settings.game_mode == 0 and Settings.ai_bool == True:
            maze_test2.visited[ai_index][0][0].color(game_display, Color.green_extra_light)

            if time_current > (1 / Settings.ai_level * ai_index):
                ai_index += 1

            if ai_index == len(maze_test2.visited):
                text_won = Text((int(screen_size[0] * 0.75), int(screen_size[1] * 0.9)), 'AI won', int(text_size * 1.5),
                                  text_color, text_color_light)
                text_won.show(game_display)
                break



        Functions.buttonpress_reset()
        Functions.update_delay(10)

def maze_end():
    Functions.buttonpress_reset()
    while True:
        Functions.buttonpress_detect()

        if Settings.keyboard_r_press:
            generation()

        if Settings.keyboard_back_press:
            Settings.back_to_menu = True
            break

        Functions.update_delay(10)

