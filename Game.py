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

import Algorithms

screen_size = screen_settings.screen_size

game_display = pygame.display.set_mode(screen_size)
#gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Maze')
pygame.init()

text_color = Color.navy
text_color_light = Color.navy_light
text_size = 50


def generation():
    game_display.fill(Color.white)
    text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'Maze game', int(text_size * 1.5), text_color, text_color_light)
    text_title.show(game_display)

    maze_test = Maze(Settings.maze_size, Settings.maze_type, 'kruskal')

    if Settings.game_mode % 3 == 0: # single player - AI
        maze_position = (Settings.screen.screen_size[0] // 2, Settings.screen.screen_size[1] // 2)
        maze_test2 = None

    else:
        maze_position = (Settings.screen.screen_size[0] // 4, Settings.screen.screen_size[1] // 2)
        maze_test2 = copy.deepcopy(maze_test)
        maze_position2 = (3 * Settings.screen.screen_size[0] // 4, Settings.screen.screen_size[1] // 2)

    # create and display mazes
    maze_test.create(maze_position, 1, graph_bool=False)
    maze_test.draw(game_display, graph_bool=False, step_bool=False, visibility_bool=Settings.invisible_mode, delay=0)
    maze_test.solve('astar')

    if maze_test2 != None:
        maze_test2.create(maze_position2, 1, graph_bool=False)
        maze_test2.draw(game_display, graph_bool=False, step_bool=False, visibility_bool=Settings.invisible_mode, delay=0)
        maze_test2.solve('astar')

    while True:
        maze_game(maze_test, maze_test2)

        Settings.back_to_menu
        break

def maze_game(maze1, maze2):
    maze_sign_size = int(maze1.cell_size * 0.3)

    player1_position = maze1.start
    player_color = Color.blue_dark
    player1_position.draw_sign(game_display, player_color, maze_sign_size)

    player2_position = maze2.start
    if not Settings.player_mode: # multiplayer
        player2_color = Color.green_dark
        player2_position.draw_sign(game_display, player2_color, maze_sign_size)

    timer_position = (int(screen_size[0] * 0.5), int(screen_size[1] * 0.9))

    text_time = Text(timer_position, '0:00', int(text_size * 0.8), text_color, text_color_light)
    text_time.show(game_display)

    text_start = Text((int(screen_size[0] * 0.5), int(screen_size[1] * 0.5)), 'Press any arrow to start', \
                      int(text_size * 1), text_color, text_color_light)

    text_start.show_box(game_display, 3)
    text_start.show(game_display)
    pygame.display.update()

    while True:
        Functions.buttonpress_detect()
        if Functions.wait_for_arrow():
            break

    text_start.color = Color.white
    text_start.show(game_display)

    text_start.show_box(game_display, Color.white, 3)

    maze1.draw(game_display, graph_bool=False, step_bool=False, visibility_bool=Settings.invisible_mode, delay=0)
    pygame.draw.circle(game_display, player_color, player1_position.position, int(maze1.cell_size * 0.3))

    if Settings.game_mode % 3 != 0:
        maze2.draw(game_display, graph_bool=False, step_bool=False, visibility_bool=Settings.invisible_mode, delay=0)
        ai_index = 0

    if not Settings.player_mode:
        pygame.draw.circle(game_display, player2_color, player2_position.position, int(maze2.cell_size * 0.3))

    time_start = time.time()
    time_sec = 0

    if Settings.invisible_mode:
        visible_list1 = MazeFunctions.visible_cells(maze1, player1_position)

        for cell in visible_list1:
            cell.color(game_display, Color.white, graph_bool = False, line_color = Color.black)

        visible_list1 = visible_list1.union(set((maze1.start, maze1.end)))

        if not Settings.player_mode:
            visible_list2 = MazeFunctions.visible_cells(maze2, player2_position)

            for cell in visible_list2:
                cell.color(game_display, Color.white, graph_bool=False, line_color=Color.black)

            visible_list2 = visible_list2.union(set((maze2.start, maze2.end)))
            
        pygame.display.update()




    # game start
    while True:
        time_current = time.time() - time_start
        time_temp = int(time_current)

        if time_temp > time_sec:
            time_sec = time_temp

            text_time = Text(timer_position, Functions.timer_string(time_sec), int(text_size * 0.8),
                              text_color, text_color_light)
            text_time.show(game_display)

        Functions.buttonpress_detect()

        new_index = player1_position.index
        if not Settings.player_mode:
            new_index2 = player2_position.index

        # sigleplayer mode
        if Settings.player_mode:
            if (Settings.keyboard_down_press or Settings.keyboard_s_press) and player1_position.coordinate[0] < maze1.size - 1:
                new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0] + 1, \
                                                                      player1_position.coordinate[1]), maze1.size)

            if (Settings.keyboard_up_press or Settings.keyboard_w_press) and player1_position.coordinate[0] > 0:
                new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0] - 1, \
                                                                      player1_position.coordinate[1]), maze1.size)

            if (Settings.keyboard_left_press or Settings.keyboard_a_press) and player1_position.coordinate[1] > 0:
                new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0], \
                                                                      player1_position.coordinate[1] - 1), maze1.size)

            if Settings.keyboard_right_press or Settings.keyboard_d_press and player1_position.coordinate[1] < maze1.size:
                new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0], \
                                                                      player1_position.coordinate[1] + 1), maze1.size)

        # multiplayer
        elif not Settings.player_mode:
            # player1 movments with w,s,a,d
            if Settings.keyboard_s_press and player1_position.coordinate[0] < maze1.size - 1:
                new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0] + 1, \
                                                                      player1_position.coordinate[1]), maze1.size)

            if Settings.keyboard_w_press and player1_position.coordinate[0] > 0:
                new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0] - 1, \
                                                                      player1_position.coordinate[1]), maze1.size)

            if Settings.keyboard_a_press and player1_position.coordinate[1] > 0:
                new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0], \
                                                                      player1_position.coordinate[1] - 1), maze1.size)

            if Settings.keyboard_d_press and player1_position.coordinate[1] < maze1.size:
                new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0], \
                                                                      player1_position.coordinate[1] + 1), maze1.size)

            # player2 movements with arrows
            if Settings.keyboard_down_press and player2_position.coordinate[0] < maze2.size - 1:
                new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0] + 1, \
                                                                      player2_position.coordinate[1]), maze2.size)

            if Settings.keyboard_up_press and player2_position.coordinate[0] > 0:
                new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0] - 1, \
                                                                       player2_position.coordinate[1]), maze2.size)

            if Settings.keyboard_left_press and player2_position.coordinate[1] > 0:
                new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0], \
                                                                       player2_position.coordinate[1] - 1), maze2.size)

            if Settings.keyboard_right_press and player2_position.coordinate[1] < maze1.size:
                new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0] , \
                                                                       player2_position.coordinate[1] + 1), maze2.size)

        else:
            print('error: invalid game mode type in Game')

        if new_index in maze1.maze_list[player1_position.index]:
            pygame.draw.circle(game_display, Color.yellow_light, player1_position.position, int(maze1.cell_size * 0.3))
            player1_position = maze1.cell_list[new_index]
            pygame.draw.circle(game_display, player_color, player1_position.position,
                               int(maze1.cell_size * 0.3))

            if Settings.invisible_mode:
                visible_new = MazeFunctions.visible_cells(maze1, player1_position).difference(visible_list1)
                for cell in visible_new:
                    cell.color(game_display, Color.white, graph_bool=False, line_color=Color.black)

                visible_list1 = visible_list1.union(visible_new)

            # check end conditions
            if player1_position == maze1.end:
                text_won = Text((int(screen_size[0] * 0.25), int(screen_size[1] * 0.9)), 'You won', int(text_size * 1.5),
                                  text_color, text_color_light)
                text_won.show(game_display)
                break

        if not Settings.player_mode and (new_index2 in maze2.maze_list[player2_position.index]):
            pygame.draw.circle(game_display, Color.yellow_light, player2_position.position, int(maze2.cell_size * 0.3))
            player2_position = maze2.cell_list[new_index2]
            pygame.draw.circle(game_display, player2_color, player2_position.position,
                               int(maze2.cell_size * 0.3))

            if Settings.invisible_mode:
                visible_new2 = MazeFunctions.visible_cells(maze2, player2_position).difference(visible_list2)
                for cell in visible_new2:
                    cell.color(game_display, Color.white, graph_bool=False, line_color=Color.black)

                visible_list2 = visible_list2.union(visible_new2)

            # check end conditions
            if player2_position == maze2.end:
                text_won2 = Text((int(screen_size[0] * 0.75), int(screen_size[1] * 0.9)), 'You won', int(text_size * 1.5),
                                  player2_color, text_color_light)
                text_won2.show(game_display)
                maze_end(maze1, maze2, player1_position, player2_position)

        if Settings.player_mode and Settings.ai_mode:
            maze2.visited[ai_index][0][0].color(game_display, Color.green_extra_light)

            if time_current > (1 / Settings.ai_level * ai_index):
                ai_index += 1

            if ai_index == len(maze2.visited):
                text_won = Text((int(screen_size[0] * 0.75), int(screen_size[1] * 0.9)), 'AI won', int(text_size * 1.5),
                                  text_color, text_color_light)
                text_won.show(game_display)
                maze_end(maze1, maze2, player1_position, player2_position)

        Functions.buttonpress_reset()
        Functions.update_delay(10)

def maze_end(maze1, maze2, player1_position, player2_position):
    solution_list = maze1.solution_path
    solution_list.reverse()

    for i in solution_list:
        if i != player1_position.index:
            maze1.cell_list[i].color(game_display, Color.white)
            maze1.cell_list[i].draw_sign(game_display, Color.blue_light, int(maze1.cell_size * 0.3))

        if Settings.game_mode % 3 == 1: # single player + AI
            maze2.cell_list[i].color(game_display, Color.blue_light)

        elif Settings.game_mode % 3 == 2: # mulfiplayer
            if i != player2_position:
                maze2.cell_list[i].color(game_display, Color.white)
                maze2.cell_list[i].draw_sign(game_display, Color.green_extra_light, int(maze1.cell_size * 0.3))
        Functions.update_delay(50)

    Functions.buttonpress_reset()
    while True:
        Functions.buttonpress_detect()

        if Settings.keyboard_r_press:
            generation()

        if Settings.keyboard_back_press:
            Settings.back_to_menu = True
            break

        Functions.update_delay(10)