import math

def generation(type, cell_list):
    """
    :param int type: square = 0, circle = 1, hexagon = 2, triangle = 3
    :param list cell_list: size of the maze
    :return: list of coordinate pairs about the outer border of the cell list
    """
    if type == 0:
        return frame_square(cell_list)
    elif type == 1:
        return frame_circle(cell_list)
    elif type == 2:
        return frame_hexagon(cell_list)
    elif type == 3:
        return frame_triangle(cell_list)

def size_from_cell(cell_list):
    """

    :param cell_list:
    :return:
    """
    return cell_list[-1].coordinate[0] + 1

def frame_square(cell_list):
    """

    :param cell_list:
    :return:
    """
    size = size_from_cell(cell_list)
    frame_list = []

    # first row
    for j in range(0, size):
        frame_list.append(cell_list[j].walls[1])

    # sides
    for i in range(0, size):
        frame_list.append(cell_list[i * size].walls[0])       # left side
        frame_list.append(cell_list[(i + 1) * size - 1].walls[2]) # right side

    # last row
    for j in range(0, size):
        frame_list.append(cell_list[(size - 1) * size + j].walls[3])

    return frame_list

def frame_circle(cell_list):
    """

    :param cell_list:
    :return:
    """
    size = size_from_cell(cell_list)
    frame_list = []

    level = math.log(size, 2)
    cells_in_ring = 2 ** (math.floor(math.log(size - 1, 2)) + 3)

    if level.is_integer():
        for k in range(0, cells_in_ring):
            frame_list.extend((cell_list[-1 - k].walls[1], cell_list[-1 - k].walls[2]))

    else:
        for k in range(0, cells_in_ring):
            frame_list.append(cell_list[-1 - k].walls[1])

    return frame_list

def frame_hexagon(cell_list):
    """

    :param cell_list:
    :return:
    """
    size = size_from_cell(cell_list)
    frame_list = []

    first_of_ring = 3 * ((size - 2) ** 2 + (size - 2)) + 1
    first_of_next = 3 * ((size - 1) ** 2 + (size - 1)) + 1
    last_ring_side = (first_of_next - first_of_ring) // 6 # cell in a side of the last ring

    # i-th side of the grid
    for i in range(0, 6):
        frame_list.append(cell_list[first_of_ring + i * last_ring_side].walls[(2 + i) % 6])
        for j in range(0, last_ring_side):
            frame_list.append(cell_list[first_of_ring + i * last_ring_side + j].walls[(3 + i) % 6])
            frame_list.append(cell_list[first_of_ring + i * last_ring_side + j].walls[(4 + i) % 6])

    return frame_list

def frame_triangle(cell_list):
    """

    :param cell_list:
    :return:
    """
    size = size_from_cell(cell_list)
    frame_list = []

    # sides
    for i in range(0, size):
        first_of_row = i ** 2
        frame_list.append(cell_list[first_of_row].walls[0])
        frame_list.append(cell_list[first_of_row + 2 * i].walls[1])

    # last row
    for j in range(0, 2 * (size - 1) + 1, 2):
        frame_list.append(cell_list[i ** 2 + j].walls[2])

    return frame_list