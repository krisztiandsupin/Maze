import MazeFunctions
import Settings


def single_player_square(position_cell, maze_size):
    if (Settings.keyboard_down_press or Settings.keyboard_s_press) and position_cell.coordinate[0] < maze_size - 1:
        new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0] + 1,
                                                              position_cell.coordinate[1]), maze_size)

    elif (Settings.keyboard_up_press or Settings.keyboard_w_press) and position_cell.coordinate[0] > 0:
        new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0] - 1,
                                                              position_cell.coordinate[1]), maze_size)

    elif (Settings.keyboard_left_press or Settings.keyboard_a_press) and position_cell.coordinate[1] > 0:
        new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0],
                                                              position_cell.coordinate[1] - 1), maze_size)

    elif Settings.keyboard_right_press or Settings.keyboard_d_press and position_cell.coordinate[1] < maze_size:
        new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0],
                                                              position_cell.coordinate[1] + 1), maze_size)
    else:
        new_index = -1

    return new_index


def single_player_octagon(position_cell, maze_size):
    print((Settings.keyboard_down_press or Settings.keyboard_s_press),
          (Settings.keyboard_right_press or Settings.keyboard_d_press),
          (position_cell.coordinate[0] < maze_size - 1),
          (position_cell.coordinate[1] < maze_size - 1),
          ((Settings.keyboard_down_press or Settings.keyboard_s_press) and
           (Settings.keyboard_right_press or Settings.keyboard_d_press) and position_cell.coordinate[
               0] < maze_size - 1 and position_cell.coordinate[1] < maze_size - 1))

    # up
    if (Settings.keyboard_up_press or Settings.keyboard_w_press) and \
            not (Settings.keyboard_left_press or Settings.keyboard_a_press) and \
            not (Settings.keyboard_right_press or Settings.keyboard_d_press) and \
            position_cell.coordinate[0] > 0:
        new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0] - 1,
                                                              position_cell.coordinate[1]),
                                                             maze_size)

    # down
    elif (Settings.keyboard_down_press or Settings.keyboard_s_press) and \
            not (Settings.keyboard_left_press or Settings.keyboard_a_press) and \
            not (Settings.keyboard_right_press or Settings.keyboard_d_press) and \
            position_cell.coordinate[0] < maze_size - 1:
        new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0] + 1,
                                                              position_cell.coordinate[1]),
                                                             maze_size)

    # left
    elif (Settings.keyboard_left_press or Settings.keyboard_a_press) and \
            not (Settings.keyboard_up_press or Settings.keyboard_w_press) and \
            not (Settings.keyboard_down_press or Settings.keyboard_s_press) and \
            position_cell.coordinate[1] > 0:
        new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0],
                                                              position_cell.coordinate[1] - 1),
                                                             maze_size)

    # right
    elif (Settings.keyboard_right_press or Settings.keyboard_d_press) and \
            not (Settings.keyboard_up_press or Settings.keyboard_w_press) and \
            not (Settings.keyboard_down_press or Settings.keyboard_s_press) and \
            position_cell.coordinate[1] < maze_size - 1:
        new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0],
                                                              position_cell.coordinate[1] + 1),
                                                             maze_size)

    # up-right
    elif (Settings.keyboard_up_press or Settings.keyboard_w_press) and \
            (Settings.keyboard_right_press or Settings.keyboard_d_press) and \
            position_cell.coordinate[0] > 0 and \
            position_cell.coordinate[1] < maze_size - 1:
        new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0] - 1,
                                                              position_cell.coordinate[1] + 1),
                                                             maze_size)

    # up-left
    elif (Settings.keyboard_up_press or Settings.keyboard_w_press) and \
            (Settings.keyboard_left_press or Settings.keyboard_a_press) and \
            position_cell.coordinate[0] > 0 and \
            position_cell.coordinate[1] > 0:
        new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0] - 1,
                                                              position_cell.coordinate[1] - 1),
                                                             maze_size)

    # down-right
    elif (Settings.keyboard_down_press or Settings.keyboard_s_press) and \
            (Settings.keyboard_right_press or Settings.keyboard_d_press) and \
            position_cell.coordinate[0] < maze_size - 1 and \
            position_cell.coordinate[1] < maze_size - 1:
        new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0] + 1,
                                                              position_cell.coordinate[1] + 1),
                                                             maze_size)

    # down-left
    elif (Settings.keyboard_down_press or Settings.keyboard_s_press) and \
            (Settings.keyboard_left_press or Settings.keyboard_a_press) and \
            position_cell.coordinate[0] < maze_size - 1 and \
            position_cell.coordinate[1] > 0:
        new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0] + 1,
                                                              position_cell.coordinate[1] - 1),
                                                             maze_size)

    else:
        new_index = -1

    print()
    return new_index


def single_player(maze_type, position_cell, maze_size):

    """
    :param maze_type:
    :param position_cell: current position of cell; type cell
    :param maze_size:
    :return:
    """

    # is square
    if maze_type == 'square':
        return single_player_square(position_cell, maze_size)

    # is hexagon
    elif maze_type == 'octagon':
        maze_size = maze_size * 2 - 1  # number of cells in a row differs from maze size (number of octagons in a row)

        # position_cell is octagon
        if (position_cell.coordinate[0] + position_cell.coordinate[1]) % 2 == 0:
            return single_player_octagon(position_cell, maze_size)

        # position_cell is square
        else:
            return single_player_square(position_cell, maze_size)


# player1 movements with w,s,a,d
def multi_player(player1_position, player2_position, maze_size):
    """

    :param player1_position:
    :param player2_position:
    :param maze_size:
    :return:
    """
    new_index = -1
    new_index2 = -1

    if Settings.keyboard_s_press and player1_position.coordinate[0] < maze_size - 1:
        new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0] + 1,
                                                              player1_position.coordinate[1]), maze_size)

    if Settings.keyboard_w_press and player1_position.coordinate[0] > 0:
        new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0] - 1,
                                                              player1_position.coordinate[1]), maze_size)

    if Settings.keyboard_a_press and player1_position.coordinate[1] > 0:
        new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0],
                                                              player1_position.coordinate[1] - 1), maze_size)

    if Settings.keyboard_d_press and player1_position.coordinate[1] < maze_size:
        new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0],
                                                              player1_position.coordinate[1] + 1), maze_size)

    # player2 movements with arrows
    if Settings.keyboard_down_press and player2_position.coordinate[0] < maze_size - 1:
        new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0] + 1,
                                                               player2_position.coordinate[1]), maze_size)

    if Settings.keyboard_up_press and player2_position.coordinate[0] > 0:
        new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0] - 1,
                                                               player2_position.coordinate[1]), maze_size)

    if Settings.keyboard_left_press and player2_position.coordinate[1] > 0:
        new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0],
                                                               player2_position.coordinate[1] - 1), maze_size)

    if Settings.keyboard_right_press and player2_position.coordinate[1] < maze_size:
        new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0],
                                                               player2_position.coordinate[1] + 1), maze_size)

    return new_index, new_index2
