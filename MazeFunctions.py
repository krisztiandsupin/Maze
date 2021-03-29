import math
import pygame
from Color import Color
from Settings import screen as screen_settings
from Settings import maze as maze_settings


def text_display(screen, x, y, string, size, color=Color.black, background=Color.white,
                 allign='center'):  # centered text display
    """

    :param screen:
    :param x:
    :param y:
    :param string:
    :param size:
    :param color:
    :param background:
    :param allign:
    """
    myfont = pygame.font.SysFont('cabria', size)
    text = myfont.render(string, True, color, background)

    if allign == 'center':  # text display in center allignment
        textrect = text.get_rect()  # center of textbox
        textrect.centerx = x
        textrect.centery = y
        screen.blit(text, textrect)

    elif allign == 'left':
        text = myfont.render(string, True, color, background)  # (x,y): upper left corner of textbox
        screen.blit(text, (x, y))


def graph_position(position):
    """

    :param position:
    :return:
    """
    x = position[0] + screen_settings.screen_size[0] // 2
    y = position[1]
    return (x, y)


def wall_between(cell1, cell2):
    """

    :param cell1:
    :param cell2:
    :return:
    """
    for wall in cell1.walls:
        if wall in cell2.walls:
            return wall

    print('error: not adjacent cells')


def sort(cell1, cell2):
    """

    :param cell1:
    :param cell2:
    :return:
    """
    if cell1.coordinate[0] < cell2.coordinate[0]:
        return cell1, cell2
    elif cell1.coordinate[0] == cell2.coordinate[0]:
        if cell1.coordinate[1] < cell2.coordinate[1]:
            return cell1, cell2
        else:
            return cell2, cell1
    else:
        return cell2, cell1


'''def cell_with_coordinate(cell_list, coordinate):
    for cell in cell_list:
        if cell.coordinate == coordinate:
            return cell'''


def max_ring_index(n):  # return the index of the first element of the n-th ring in a circle
    """

    :param n:
    :return:
    """
    k = math.floor(math.log(n + 1, 2))
    # 1 + sum of complete rings + remained rings
    return 1 + 8 * (4 ** k - 1) // 3 + ((n + 1) - 2 ** k) * (2 ** (k + 3))


def first_index_circle(n):  # return the first index of the n + 1-th ring
    """

    :param n:
    :return:
    """
    k = math.floor(math.log(n + 1, 2))
    # 1 + sum of complete rings + remained rings
    return 1 + 8 * (4 ** k - 1) // 3 + ((n + 1) - 2 ** k) * (2 ** (k + 3))


def adjacent_cells(type, cell, cell_list):
    """

    :param type:
    :param cell:
    :param cell_list:
    :return:
    """
    if type == 0:
        return adjacent_cells_square(cell, cell_list)
    elif type == 1:
        return adjacent_cells_circle(cell, cell_list)
    elif type == 2:
        return adjacent_cells_hexagon(cell, cell_list)
    elif type == 3:
        return adjacent_cells_triangle(cell, cell_list)
    else:
        print('error: not adjacent cells')
        return []


def adjacent_cells_square(cell, cell_list):
    """

    :param cell:
    :param cell_list:
    :return:
    """
    size = cell_list[-1].coordinate[0] + 1
    adjacent_list = []

    if cell.coordinate[0] == 0 or cell.coordinate[0] == size - 1 or \
            cell.coordinate[1] == 0 or cell.coordinate[1] == size - 1:  # in the first or last row or coolumn
        # first row
        if cell.coordinate[0] == 0:
            if cell.coordinate[1] == 0:
                adjacent_list.append(cell_list[cell.index + 1])
            elif cell.coordinate[1] == size - 1:
                adjacent_list.append(cell_list[cell.index - 1])
            else:
                adjacent_list.append(cell_list[cell.index - 1])
                adjacent_list.append(cell_list[cell.index + 1])
            adjacent_list.append(cell_list[cell.index + size])

        # last row
        elif cell.coordinate[0] == size - 1:
            if cell.coordinate[1] == 0:
                adjacent_list.append(cell_list[cell.index + 1])
            elif cell.coordinate[1] == size - 1:
                adjacent_list.append(cell_list[cell.index - 1])
            else:
                adjacent_list.append(cell_list[cell.index - 1])
                adjacent_list.append(cell_list[cell.index + 1])
            adjacent_list.append(cell_list[cell.index - size])

        # in first or last column
        else:
            if cell.coordinate[1] == 0:  # first column
                adjacent_list.append(cell_list[cell.index + 1])
            elif cell.coordinate[1] == size - 1:  # last column
                adjacent_list.append(cell_list[cell.index - 1])
            adjacent_list.append(cell_list[cell.index - size])
            adjacent_list.append(cell_list[cell.index + size])

    else:
        adjacent_list.append(cell_list[cell.index - 1])
        adjacent_list.append(cell_list[cell.index + 1])
        adjacent_list.append(cell_list[cell.index - size])
        adjacent_list.append(cell_list[cell.index + size])

    return adjacent_list


def adjacent_cells_circle(cell, cell_list):
    """

    :param cell:
    :param cell_list:
    :return:
    """
    size = cell_list[-1].coordinate[0] + 1
    adjacent_list = []

    if cell.coordinate[0] == 0:
        adjacent_list = cell_list[1:9]

    else:
        # elements from the same ring
        if cell.coordinate[1] == 0:  # first in the ring
            adjacent_list.append(cell_list[cell.index + 1])
            adjacent_list.append(cell_list[max_ring_index(cell.coordinate[0]) - 1])
        elif 2 ** (math.floor(math.log(cell.coordinate[0], 2)) + 3) == cell.coordinate[1] + 1:  # last element of a ring
            adjacent_list.append(cell_list[cell.index - 1])
            adjacent_list.append(cell_list[max_ring_index(cell.coordinate[0] - 1)])
        else:
            adjacent_list.append(cell_list[cell.index - 1])
            adjacent_list.append(cell_list[cell.index + 1])

        # elements from other rings
        if cell.coordinate[0] == 1:
            adjacent_list.append(cell_list[0])
            adjacent_list.append(cell_list[max_ring_index(cell.coordinate[0]) + 2 * cell.coordinate[1]])
            adjacent_list.append(cell_list[max_ring_index(cell.coordinate[0]) + 2 * cell.coordinate[1] + 1])

        elif cell.coordinate[0] == 2:
            adjacent_list.append(cell_list[max_ring_index(cell.coordinate[0] - 2) + cell.coordinate[1] // 2])
            adjacent_list.append(cell_list[max_ring_index(cell.coordinate[0]) + cell.coordinate[1]])

        elif cell.coordinate[0] == 3:
            adjacent_list.append((cell_list[cell.index - 16]))
            adjacent_list.append(cell_list[max_ring_index(cell.coordinate[0]) + 2 * cell.coordinate[1]])
            adjacent_list.append(cell_list[max_ring_index(cell.coordinate[0]) + 2 * cell.coordinate[1] + 1])

        else:
            if math.log((cell.coordinate[0]), 2).is_integer() == True:
                adjacent_list.append(cell_list[max_ring_index(cell.coordinate[0] - 2) + cell.coordinate[1] // 2])
                if cell.coordinate[0] != size - 1:
                    adjacent_list.append(cell_list[max_ring_index(cell.coordinate[0]) + cell.coordinate[1]])


            elif math.log((cell.coordinate[0] + 1), 2).is_integer() == True:
                adjacent_list.append(cell_list[max_ring_index(cell.coordinate[0] - 2) + cell.coordinate[1]])
                if cell.coordinate[0] != size - 1:
                    adjacent_list.append(cell_list[max_ring_index(cell.coordinate[0]) + 2 * cell.coordinate[1]])
                    adjacent_list.append(cell_list[max_ring_index(cell.coordinate[0]) + 2 * cell.coordinate[1] + 1])

            else:
                adjacent_list.append(cell_list[max_ring_index(cell.coordinate[0] - 2) + cell.coordinate[1]])
                if cell.coordinate[0] != size - 1:
                    adjacent_list.append(cell_list[max_ring_index(cell.coordinate[0]) + cell.coordinate[1]])

    return adjacent_list


def coordinate_to_index_square(cell_coordinate, maze_size):
    """

    :param cell_coordinate:
    :param maze_size:
    :return:
    """
    return cell_coordinate[0] * maze_size + cell_coordinate[1]


def coordinate_to_index_hexagonal(cell_coordinate: tuple) -> int:
    """

    :param cell_coordinate:
    :return:
    """
    return ((12 + 6 * (cell_coordinate[0] - 2)) * (cell_coordinate[0] - 1)) // 2 + cell_coordinate[1] + \
           math.ceil(cell_coordinate[0] / (cell_coordinate[0] + 1))


def coordinate_to_index_circle(cell_coordinate):
    """

    :param cell_coordinate:
    :return:
    """
    if cell_coordinate[0] == 0:
        return 0
    else:
        k = math.floor(math.log(cell_coordinate[0], 2))
        return 1 + 8 * (4 ** k - 1) // 3 + ((cell_coordinate[0]) - 2 ** k) * (2 ** (k + 3)) + cell_coordinate[1]


def adjacent_cells_hexagon(cell, cell_list):
    """

    :param cell:
    :param cell_list:
    :return:
    """
    size = cell_list[-1].coordinate[0] + 1
    adjacent_list = []

    if cell.coordinate[0] == 0:
        adjacent_list = cell_list[1:7]

    else:
        # elements from same ring
        temp_index = coordinate_to_index_hexagonal(
            (cell.coordinate[0], (cell.coordinate[1] - 1) % (cell.coordinate[0] * 6)))
        adjacent_list.append(cell_list[temp_index])

        temp_index = coordinate_to_index_hexagonal(
            (cell.coordinate[0], (cell.coordinate[1] + 1) % (cell.coordinate[0] * 6)))
        adjacent_list.append(cell_list[temp_index])

        # elements from other rings
        if cell.coordinate[1] % cell.coordinate[0] == 0:
            temp_index = coordinate_to_index_hexagonal((cell.coordinate[0] - 1, \
                                                        (cell.coordinate[0] - 1) * (
                                                                cell.coordinate[1] // cell.coordinate[0])))
            adjacent_list.append(cell_list[temp_index])

        else:
            temp_index = coordinate_to_index_hexagonal((cell.coordinate[0] - 1, \
                                                        (cell.coordinate[1] // cell.coordinate[0]) * (
                                                                cell.coordinate[0] - 1) + \
                                                        cell.coordinate[1] % cell.coordinate[0] - 1))
            adjacent_list.append(cell_list[temp_index])

            temp_index = coordinate_to_index_hexagonal((cell.coordinate[0] - 1, \
                                                        ((cell.coordinate[1] // cell.coordinate[0]) * (
                                                                cell.coordinate[0] - 1) + \
                                                         cell.coordinate[1] % cell.coordinate[0]) % (
                                                                (cell.coordinate[0] - 1) * 6)))
            adjacent_list.append(cell_list[temp_index])

        if cell.coordinate[0] != size - 1:
            temp_index = coordinate_to_index_hexagonal((cell.coordinate[0] + 1, \
                                                        (cell.coordinate[1] // cell.coordinate[0]) * (
                                                                cell.coordinate[0] + 1) + \
                                                        cell.coordinate[1] % cell.coordinate[0]))
            adjacent_list.append(cell_list[temp_index])

            temp_index = coordinate_to_index_hexagonal((cell.coordinate[0] + 1, \
                                                        (cell.coordinate[1] // cell.coordinate[0]) * (
                                                                cell.coordinate[0] + 1) + \
                                                        cell.coordinate[1] % cell.coordinate[0] + 1))
            adjacent_list.append(cell_list[temp_index])

            if cell.coordinate[1] % cell.coordinate[0] == 0:
                temp_index = coordinate_to_index_hexagonal((cell.coordinate[0] + 1, \
                                                            ((cell.coordinate[1] // cell.coordinate[0]) * (
                                                                    cell.coordinate[0] + 1) + \
                                                             cell.coordinate[1] % cell.coordinate[0] - 1) % (
                                                                    (cell.coordinate[0] + 1) * 6)))
                adjacent_list.append(cell_list[temp_index])

    return adjacent_list


def coordinate_transform_hexagon(coordinate):
    """
    transform from (ring, enum) -> (x: horizontal, y: vertical) form
    :param tuple coordinate: (ring, enum)
    :return tuplle (x,y): X: horizontal position in vertical level (increases by 2), y: vertical level
    """
    #
    if coordinate == (0, 0):
        return coordinate

    ring = coordinate[0]
    enum = coordinate[1]
    interval = enum // ring

    if interval == 0:
        x = 2 * ring - enum
        y = enum

    elif interval == 1:
        x = 3 * ring - 2 * enum
        y = ring

    elif interval == 2:
        x = -2 * ring + (3 * ring - enum)
        y = 3 * ring - enum

    elif interval == 3:
        x = -2 * ring + (enum - 3 * ring)
        y = 3 * ring - enum

    elif interval == 4:
        x = 2 * (enum % (3 * ring)) - 3 * ring
        y = - ring

    elif interval == 5:
        x = (enum % (3 * ring)) - ring
        y = -6 * ring + enum

    return (x, -1 * y)


def coordinate_transform_inverse_hexagon(points):
    """
    inverse transform (x,y) -> (ring, enum)
    :param tuple points: (x,y) pair
    :return tuple coordinate: (ring, enum) format
    """
    (x, y) = points

    ring_cand = (abs(x) + abs(y)) // 2
    if ring_cand <= abs(x):
        ring = ring_cand
    else:
        ring = abs(y)

    if x == 0 and y == 0:
        enum = 0
    elif x > 0 and y <= 0 and abs(x) > abs(y):
        case = 'case1'
        enum = abs(y)
    elif (y == -1 * ring) and x != y:
        case = 'case2'
        enum = ring + (ring - x) // 2
    elif x < 0 and y < 0 and abs(x) >= abs(y):
        case = 'case3'
        enum = 2 * ring + (-1 * x + y) // 2
    elif x < 0 and y >= 0 and abs(x) > abs(y):
        case = 'case4'
        enum = 3 * ring + y
    elif y == ring and x != y:
        case = 'case5'
        enum = 4 * ring + (ring + x) // 2
    elif x > 0 and y > 0 and x >= y:
        case = 'case6'
        enum = 5 * ring + ring - y
    else:
        enum = -1
        case = 'case7'
        print("error: invalid else case")

    coordinate = (ring, enum)
    return coordinate


def adjacent_cells_triangle(cell, cell_list):
    """

    :param cell:
    :param cell_list:
    :return:
    """
    size = cell_list[-1].coordinate[0] + 1
    adjacent_list = []

    if cell.coordinate[0] == 0:
        adjacent_list.append(cell_list[2])

    else:
        if cell.coordinate[1] != 0:
            # cell in the right
            adjacent_list.append(cell_list[cell.index - 1])

        if cell.coordinate[1] != 2 * cell.coordinate[0]:
            # cell on the left
            adjacent_list.append(cell_list[cell.index + 1])

        if cell.coordinate[1] % 2 == 1:
            # cell above
            adjacent_list.append(cell_list[cell.index - 2 * cell.coordinate[0]])

        elif cell.coordinate[0] != size - 1:
            # cell below
            adjacent_list.append(cell_list[cell.index + 2 * (cell.coordinate[0] + 1)])

    return adjacent_list


def edge_wall(edge):
    """

    :param edge:
    :return:
    """
    start_cell_walls = set(edge[0].walls)
    end_cell_walls = set(edge[1].walls)

    return list(start_cell_walls.intersection(end_cell_walls))[0]


def edge_color(screen, edge, color, graph=True, graph_color=Color.black):
    """
    :param int screen: display
    :param tuple edge: edge = (start_cell [cell type], end_cell [cell_type])
    :return: None, color the given edge
    """
    wall = edge_wall(edge)
    pygame.draw.line(screen, color, wall[0], wall[1])
    pygame.draw.line(screen, graph_color, wall[0], wall[0])
    pygame.draw.line(screen, graph_color, wall[1], wall[1])

    if graph == True:
        pygame.draw.line(screen, graph_color, edge[0].graph_position, edge[1].graph_position)


def updete_delay(milisecond):
    """

    :param milisecond:
    """
    pygame.display.flip()
    pygame.time.delay(milisecond)


def system_pause():
    """

    """
    RUNNING, PAUSE = 0, 1
    state = RUNNING
    while True:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    raise SystemExit
                elif e.key == pygame.K_SPACE:
                    if state == RUNNING:
                        state = PAUSE

        while state == PAUSE:
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        raise SystemExit
                    elif e.key == pygame.K_SPACE:
                        state = RUNNING
        break


def cell_endpoints_calculate(type, size):
    """
    :param int type: square = 0, circle = 1, hexagon = 2, triangle = 3
    :param int size: size of the maze
    :return: tuple of (start_index, end_index)
    """
    if type == 0:
        return (0, size ** 2 - 1)
    elif type == 1:
        k = int(math.log(size - 1, 2))
        return (coordinate_to_index_circle((size - 1, (2 ** (k + 2)) + k)), \
                coordinate_to_index_circle((size - 1, k)))
    elif type == 2:
        return (coordinate_to_index_hexagonal((size - 1, 3 * (size - 1))), \
                coordinate_to_index_hexagonal((size - 1, 0)))
    elif type == 3:
        return (0, (size - 1) ** 2 + size - 1)
    else:
        print('error: invalid type in cell endpoint calculator')
        return []


# border update
def border_update(maze_type, start_cell, end_cell):
    """

    :param maze_type:
    :param start_cell:
    :param end_cell:
    :return:
    """
    if maze_type == 0:
        border_update_square(start_cell, end_cell)
    elif maze_type == 1:
        border_update_circle(start_cell, end_cell)
    elif maze_type == 2:
        border_update_hexagon(start_cell, end_cell)
    elif maze_type == 3:
        border_update_triangle(start_cell, end_cell)
    else:
        print('error: wrong type in border update')
        return None


def border_update_square(cell1, cell2):  # suppose that they are adjacent, and cell1 < cell2
    """

    :param cell1:
    :param cell2:
    """
    # in the same row

    if cell1.coordinate[0] == cell2.coordinate[0]:
        if cell1.coordinate[1] < cell2.coordinate[1]:
            cell1.walls_bool[2] = False
            cell2.walls_bool[0] = False
        else:
            cell1.walls_bool[0] = False
            cell2.walls_bool[2] = False

    # in the same column
    else:
        if cell1.coordinate[0] < cell2.coordinate[0]:
            cell1.walls_bool[3] = False
            cell2.walls_bool[1] = False
        else:
            cell1.walls_bool[1] = False
            cell2.walls_bool[3] = False


def border_update_circle(cell1, cell2):  # suppose that they are adjacent, and cell1 < cell2
    """

    :param cell1:
    :param cell2:
    """
    # in the same ring
    if cell2.coordinate[0] < cell1.coordinate[0] or (cell2.coordinate[0] == cell1.coordinate[0] and
                                                     cell2.coordinate[1] < cell1.coordinate[1]):
        cell1, cell2 = cell2, cell1

    if cell1.coordinate[0] == cell2.coordinate[0]:
        if math.log(cell2.coordinate[0] + 1, 2).is_integer() == True:
            cell1.walls_bool[3] = False
            cell2.walls_bool[0] = False
        else:
            cell1.walls_bool[2] = False
            cell2.walls_bool[0] = False

    # in different rings
    else:
        if cell1.coordinate == (0, 0):
            cell1.walls_bool[cell2.coordinate[1]] = False
            cell2.walls_bool[-1] = False

        elif math.log(cell2.coordinate[0], 2).is_integer() and cell1.coordinate != (0, 0):
            if cell2.coordinate[1] - (2 * cell1.coordinate[1]) == 0:
                cell1.walls_bool[1] = False
                cell2.walls_bool[3] = False
            else:
                cell1.walls_bool[2] = False
                cell2.walls_bool[3] = False

        elif math.log(cell2.coordinate[0] + 1, 2).is_integer() and cell1.coordinate != (0, 0):
            cell1.walls_bool[1] = False
            cell2.walls_bool[4] = False

        else:
            cell1.walls_bool[1] = False
            cell2.walls_bool[3] = False


def border_update_hexagon(cell1, cell2):
    """

    :param cell1:
    :param cell2:
    """
    coordinate1 = coordinate_transform_hexagon(cell1.coordinate)
    coordinate2 = coordinate_transform_hexagon(cell2.coordinate)

    if coordinate1[1] == coordinate2[1]:  # in the same vertical line
        if coordinate1[0] < coordinate2[0]:
            cell1.walls_bool[3] = False
            cell2.walls_bool[0] = False
        else:
            cell1.walls_bool[0] = False
            cell2.walls_bool[3] = False

    elif coordinate1[1] > coordinate2[1]:
        if coordinate1[0] > coordinate2[0]:  # increasing diagonal
            cell1.walls_bool[5] = False
            cell2.walls_bool[2] = False

        else:  # decreasing diagonal
            cell1.walls_bool[4] = False
            cell2.walls_bool[1] = False

    elif coordinate1[1] < coordinate2[1]:
        if coordinate1[0] > coordinate2[0]:  # decreasing diagonal
            cell1.walls_bool[1] = False
            cell2.walls_bool[4] = False

        else:  # decreasing diagonal
            cell1.walls_bool[2] = False
            cell2.walls_bool[5] = False


def border_update_triangle(cell1, cell2):
    """

    :param cell1:
    :param cell2:
    :return:
    """
    # triangle walls_bool order
    #                           2.
    #       / \               -----
    #   0./    \ 1.        0. \   /  1.
    #     -----                \/
    #       2.

    if cell1.coordinate[0] == cell2.coordinate[0]:   # in same row
        if cell1.coordinate[1] < cell2.coordinate[1]:
            cell1.walls_bool[1] = False
            cell2.walls_bool[0] = False
        else:
            cell1.walls_bool[0] = False
            cell2.walls_bool[1] = False
    else:
        cell1.walls_bool[2] = False
        cell2.walls_bool[2] = False


'''def border_update(start_cell, end_cell):
    wall = wall_between(start_cell, end_cell)

    start_wall_index = start_cell.walls.index(wall)
    end_wall_index = end_cell.walls.index(wall)

    start_cell.walls_bool[start_wall_index] = False
    end_cell.walls_bool[end_wall_index] = False'''


def cell_size_calculate(display_type, type_value, maze_size, graph_bool):
    """
    :param int display_type: fullscreen = 0, halfscreen = 1, quarterscreen = 2
    :param int type:value: square = 0, circle = 1, hexagon = 2, triangle = 3
    :param int maze_size: square = number of rows, circle = number of rings, hexagon = number of rings, \
    triangle = number of rows
    :param bool graph_bool: if True graph is also displayed
    :return: size of the side (square) / radius (circle) / side (hexagon) / side (triangle)
    """

    division = 1
    if (display_type == 1 and graph_bool == True) or display_type == 2:
        division *= 2

    if type_value == 0:
        return int(((screen_settings.screen_size[0] / 2) * 0.7 / maze_size) // 2 * 2 / division)
    elif type_value == 1:
        return int((screen_settings.screen_size[0] / 2) * 0.8 / (maze_size * 2 - 1) / division)
    elif type_value == 2:
        return int((screen_settings.screen_size[0] / 2) * 0.8 / (maze_size * 2 - 1) * (1 / math.sqrt(3)) / division)
    elif type_value == 3:
        return int((screen_settings.screen_size[0] * 0.8) / (maze_size * 2 + 1) / division)


def graph_cell_size_calculate(type, cell_size):
    """

    :param type:
    :param cell_size:
    :return:
    """
    if type == 0:
        graph_cell_size = int(math.sqrt(0.8 * cell_size))
    elif type == 1:
        graph_cell_size = int(math.sqrt(0.8 * cell_size))
    elif type == 2:
        graph_cell_size = int(math.sqrt(0.7 * cell_size))
    elif type == 3:
        graph_cell_size = int(math.sqrt(0.8 * cell_size)) - 1

    maze_settings.graph_cell_size = graph_cell_size
    return graph_cell_size


def visible_cells(Maze, cell):
    """

    :param Maze:
    :param cell:
    :return:
    """
    if Maze.type_value == 0:
        return visible_cells_square(Maze, cell)

    else:
        print('error: wrong type in visible cells')


def visible_cells_square(maze, cell):
    """

    :param maze:
    :param cell:
    :return:
    """
    visible_cells_list = []

    # search downwards
    temp_cell = cell
    while temp_cell.walls_bool[3] == False:
        new_index = coordinate_to_index_square((temp_cell.coordinate[0] + 1, temp_cell.coordinate[1]), maze.size)
        temp_cell = maze.cell_list[new_index]
        visible_cells_list.append(temp_cell)

    # search upward
    temp_cell = cell
    while temp_cell.walls_bool[1] == False:
        new_index = coordinate_to_index_square((temp_cell.coordinate[0] - 1, temp_cell.coordinate[1]), maze.size)
        temp_cell = maze.cell_list[new_index]
        visible_cells_list.append(temp_cell)

    # search right
    temp_cell = cell
    while temp_cell.walls_bool[2] == False:
        new_index = coordinate_to_index_square((temp_cell.coordinate[0], temp_cell.coordinate[1] + 1), maze.size)
        temp_cell = maze.cell_list[new_index]
        visible_cells_list.append(temp_cell)

    # search left
    temp_cell = cell
    while temp_cell.walls_bool[0] == False:
        new_index = coordinate_to_index_square((temp_cell.coordinate[0], temp_cell.coordinate[1] - 1), maze.size)
        temp_cell = maze.cell_list[new_index]
        visible_cells_list.append(temp_cell)

    return set(visible_cells_list)

def highlight_edge_delete(display, maze, cell0, cell1, highlight_color, graph_bool, index_text_size, step):
    """

    :type highlight_color: tuple
    :param display:
    :param maze:
    :param cell0:
    :param cell1:
    :param highlight_color:
    :param graph_bool:
    :param index_text_size:
    :param step:
    """
    cell0.color_grid(display, highlight_color, graph_bool, line_color=Color.black,
                     coordinate_text_bool=False, walls_bool=maze.maze_cell_borders[step][0])
    cell1.color_grid(display, highlight_color, graph_bool, line_color=Color.black, coordinate_text_bool=False,
                     walls_bool=maze.maze_cell_borders[step][1])
    cell0.text_display(display, str(cell0.index), index_text_size, background_color=highlight_color)
    cell1.text_display(display, str(cell1.index), index_text_size, background_color=highlight_color)