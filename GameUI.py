import MazeFunctions
import Settings

def single_player(type, position_cell, maze_size):
    """
    :param type:
    :param position_cell:
    :param maze_size:
    :return:
    """
    # is square
    if type == 'square':
        if (Settings.keyboard_down_press or Settings.keyboard_s_press) and position_cell.coordinate[0] < maze_size - 1:
            new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0] + 1, \
                                                                  position_cell.coordinate[1]), maze_size)

        elif (Settings.keyboard_up_press or Settings.keyboard_w_press) and position_cell.coordinate[0] > 0:
            new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0] - 1, \
                                                                  position_cell.coordinate[1]), maze_size)

        elif (Settings.keyboard_left_press or Settings.keyboard_a_press) and position_cell.coordinate[1] > 0:
            new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0], \
                                                                  position_cell.coordinate[1] - 1), maze_size)

        elif Settings.keyboard_right_press or Settings.keyboard_d_press and position_cell.coordinate[1] < maze_size:
            new_index = MazeFunctions.coordinate_to_index_square((position_cell.coordinate[0], \
                                                                  position_cell.coordinate[1] + 1), maze_size)
        else:
            new_index = -1

        return new_index

    # is hexagon
    elif type == 'hexagon':
        position_transformed = MazeFunctions.coordinate_transform_hexagon(position_cell.coordinate)
        if (not Settings.keyboard_up_press and not Settings.keyboard_down_press and \
            Settings.keyboard_right_press and not Settings.keyboard_left_press):
            new_position = (position_transformed[0] + 2, position_transformed[1])

        elif (not Settings.keyboard_up_press and Settings.keyboard_down_press and \
            Settings.keyboard_right_press and not Settings.keyboard_left_press):
            new_position = (position_transformed[0] + 1, position_transformed[1] - 1)


        elif (not Settings.keyboard_up_press and Settings.keyboard_down_press and \
              not Settings.keyboard_right_press and Settings.keyboard_left_press):
            new_position = (position_transformed[0] - 1, position_transformed[1] - 1)


        elif (not Settings.keyboard_up_press and not Settings.keyboard_down_press and \
              not Settings.keyboard_right_press and Settings.keyboard_left_press):
            new_position = (position_transformed[0] - 2, position_transformed[1])


        elif (Settings.keyboard_up_press and not Settings.keyboard_down_press and \
              not Settings.keyboard_right_press and Settings.keyboard_left_press):
            new_position = (position_transformed[0] - 1, position_transformed[1] + 1)

        elif (Settings.keyboard_up_press and not Settings.keyboard_down_press and \
            Settings.keyboard_right_press and not Settings.keyboard_left_press):
            new_position = (position_transformed[0] + 1, position_transformed[1] + 1)
        else:
            new_index = -1
            return new_index

        new_index = MazeFunctions.coordinate_to_index_hexagonal(MazeFunctions.coordinate_transform_inverse_hexagon(new_position))
        return new_index

# player1 movments with w,s,a,d
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
        new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0] + 1, \
                                                              player1_position.coordinate[1]), maze_size)

    if Settings.keyboard_w_press and player1_position.coordinate[0] > 0:
        new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0] - 1, \
                                                              player1_position.coordinate[1]), maze_size)

    if Settings.keyboard_a_press and player1_position.coordinate[1] > 0:
        new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0], \
                                                              player1_position.coordinate[1] - 1), maze_size)

    if Settings.keyboard_d_press and player1_position.coordinate[1] < maze_size:
        new_index = MazeFunctions.coordinate_to_index_square((player1_position.coordinate[0], \
                                                              player1_position.coordinate[1] + 1), maze_size)

    # player2 movements with arrows
    if Settings.keyboard_down_press and player2_position.coordinate[0] < maze_size - 1:
        new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0] + 1, \
                                                              player2_position.coordinate[1]), maze_size)

    if Settings.keyboard_up_press and player2_position.coordinate[0] > 0:
        new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0] - 1, \
                                                               player2_position.coordinate[1]), maze_size)

    if Settings.keyboard_left_press and player2_position.coordinate[1] > 0:
        new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0], \
                                                               player2_position.coordinate[1] - 1), maze_size)

    if Settings.keyboard_right_press and player2_position.coordinate[1] < maze_size:
        new_index2 = MazeFunctions.coordinate_to_index_square((player2_position.coordinate[0] , \
                                                               player2_position.coordinate[1] + 1), maze_size)


    return new_index, new_index2