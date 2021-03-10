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
maze_size = 10

start_time = 0
current_time = 0

player_mode = True          # singele_player = True; multiplayer = False
invisible_mode = True       # if all cell is visible by default; visible = False, invisible = True
maze_type = 'square'        # square = True, hexagon = False
ai_mode = True              # True: ai solution on other maze
ai_level = 3               # int; 1 <= ai_level <= 10: delay in displays of the algorithms

game_mode = 0

def game_mode_calculate():
    """
    :param bool player_mode: singele_player = True; multiplayer = False
    :param bool ai_mode: with AI search = True; without AI search = False
    :param bool invisible_mode: invible cells = True; visible cells = False
    :return int: game_mode
    0: + single player - Invisible - AI
    1: + single player - Invisible + AI
    2: - single player - Invisible
    3: + single player + Invisible + AI
    4: + single player + Invisible + AI
    5: - single player + Invisible
    """
    if player_mode and not ai_mode and not invisible_mode:
        return 0
    elif player_mode and ai_mode and not invisible_mode:
        return 1
    elif not player_mode and not invisible_mode:
        return 2
    elif player_mode and not ai_mode and invisible_mode:
        return 3
    elif player_mode and ai_mode and invisible_mode:
        return 4
    elif not player_mode and invisible_mode:
        return 5
    else:
        print('error: invalid game_mode in game mode calculation')

game_mode = game_mode_calculate()

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