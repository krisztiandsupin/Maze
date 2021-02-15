import math

# mouse and keyboard
mouse_click_position = (0, 0)
keyboard_space_press = None
keyboard_left_press = None
keyboard_right_press = None
keyboard_up_press = None
keyboard_down_press = None
keyboard_r_press = None
keyboard_back_press = None
keyboard_w_press = None
keyboard_a_press = None
keyboard_s_press = None
keyboard_d_press = None


back_to_menu = False
maze_size = 20

start_time = 0
current_time = 0

game_mode = 0   # singele_player = 0; multiplayer = 1
ai_bool = True  # bool; True: ai solution on other maze
ai_level = 3    # int; 1 <= ai_level <= 10: delay in displays of the algorithms


class screen:
    screen_size = (1440, 790)
    labelsize = 75
    marginsize = 15
    line_thickness = 1
    delay = 500
    statBool = True
    fullscreen = False

class maze:
    n = 20
    a = (math.floor((min(screen.screen_size[0], screen.screen_size[1]) / 2 - screen.marginsize - screen.labelsize) / n))
    location = ((screen.screen_size[0] / 2 - n * a) / 2, screen.labelsize)

    graph_size = 0
    graph_cell_size = 0

    step_bool = True
    graph_bool = True

    delay = 500