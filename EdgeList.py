from Edge import Edge
import MazeFunctions
import time
import timeit
import math

def generate(type_int, size):
    """
    :param int type_int: square = 0, circle = 1, hexagon = 2, triangle = 3
    :param int size: size of the maze
    :return: edge list with list of indexes of edge cells in the cell list
    """
    if type_int == 0:
        return square(size)
    elif type_int == 1:
        return circle(size)
    elif type_int == 2:
        return hexagon(size)
    elif type_int == 3:
        return triangle(size)
    elif type_int == 4:
        return octagon(size)
    else:
        print(f"ERROR: invalid maze type {type_int}")

# edge list data type
def square(n):
    """

    :param n:
    :return:
    """
    edge_list = [[] for _ in range(0, n ** 2)]

    # corners
    edge_list[0].extend((1, n))
    edge_list[n - 1].extend((n - 2, 2*n - 1))
    edge_list[n ** 2 - n].extend((n ** 2 - 2 * n, n ** 2 - n + 1))
    edge_list[n ** 2 - 1].extend((n ** 2 - n - 1, n ** 2 - 2))

    # frames
    # i = 0
    for j in range(1, n - 1):
        edge_list[j].extend((j - 1, j + 1, n + j))

    # i = n - 1
    for j in range(1, n - 1):
        edge_list[n ** 2 - n + j].extend((n ** 2 - 2 * n + j, n ** 2 - n + j - 1, n ** 2 - n + j + 1))

    # j = 0
    for i in range(1, n - 1):
        edge_list[i * n].extend(((i - 1) * n, i * n + 1, (i + 1) * n))

    # j = n - 1
    for i in range(1, n - 1):
        edge_list[(i + 1) * n - 1].extend((i * n - 1, (i + 1) * n - 2, (i + 2) * n - 1))

    # else
    for i  in range(1, n - 1):
        for j in range(1, n - 1):
            edge_list[i * n + j].extend(((i - 1) * n + j, i * n + j - 1, i * n + j + 1, (i + 1) * n + j))

    return edge_list

def circle(n):
    """

    :param n:
    :return:
    """
    edge_list = [[] for _ in range(0, MazeFunctions.first_index_circle(n - 1))]
    edge_list[0].extend((i for i in range(1, 9)))

    #first ring
    edge_list[1].extend((0, 2, 8, 9, 10))
    for j in range(2, 9):
        edge_list[j].extend((0, j - 1, j % 8 + 1, 2 * j + 7, 2 * j + 8))

    levels = math.floor(math.log(n - 1, 2))
    for i in range(1, levels):
        first_level_index = MazeFunctions.first_index_circle(2 ** i - 1)  # first index in new level
        rings_in_level = 2 ** i
        cells_in_ring = 2 ** (i + 3)

        # first ring in a level (j = 0)
        for k in range(0, cells_in_ring):
            cell_index = first_level_index + k
            edge_list[cell_index].extend((MazeFunctions.first_index_circle(2 ** i - 2) + k // 2, \
                                          cell_index + cells_in_ring))
            if k == 0:
                edge_list[cell_index].extend((cell_index + 1, \
                                              cell_index + cells_in_ring - 1))
            else:
                edge_list[cell_index].extend((cell_index - 1, \
                                              first_level_index + (k + 1) % cells_in_ring))

        # middle rings (j = 1 ..)
        for j in range(1, rings_in_level - 1): # circles with same cell number
            for k in range(0, cells_in_ring):
                cell_index = first_level_index + j * cells_in_ring + k
                edge_list[cell_index].extend((cell_index - cells_in_ring, \
                                              cell_index + cells_in_ring))
                if k == 0:
                    edge_list[cell_index].extend((cell_index + 1, \
                                                  cell_index + cells_in_ring - 1))
                else:
                    edge_list[cell_index].extend((cell_index - 1, \
                                                  first_level_index + j * cells_in_ring + \
                                                  (k + 1) % cells_in_ring))

        # last ring in a level (j = circle in level - 1)
        for k in range(0, cells_in_ring):
            cell_index = first_level_index + (rings_in_level - 1) * cells_in_ring  + k

            # cell below
            edge_list[cell_index].append(cell_index - cells_in_ring)
            if k == 0:
                edge_list[cell_index].extend((cell_index + 1, \
                                              cell_index + cells_in_ring - 1))
            else:
                edge_list[cell_index].extend((cell_index - 1, \
                                              first_level_index + (rings_in_level - 1) * cells_in_ring + \
                                              (k + 1) % cells_in_ring))

            if (2 ** (i + 1) - 1) != (n - 1):  # NOT last ring in the whole maze
                # cells below and above
                edge_list[cell_index].extend((MazeFunctions.first_index_circle(2 ** (i + 1) - 1) + 2 * k, \
                                              MazeFunctions.first_index_circle(2 ** (i + 1) - 1) + 2 * k + 1))


    # after complete rings
    first_level_index = MazeFunctions.first_index_circle(2 ** levels - 1)  # first index in the incomplete new level
    rings_in_level = n - (2 ** levels)
    cells_in_ring = 2 ** (levels + 3)

    # first ring in a level (j = 0)
    for k in range(0, cells_in_ring):
        cell_index = first_level_index + k
        edge_list[cell_index].append(MazeFunctions.first_index_circle(2 ** levels - 2) + k // 2)

        if k == 0:
            edge_list[cell_index].extend((cell_index + 1, \
                                          cell_index + cells_in_ring - 1))
        else:
            edge_list[cell_index].extend((cell_index - 1, \
                                          first_level_index + (k + 1) % cells_in_ring))

        if rings_in_level != 1:
            edge_list[cell_index].append(cell_index + cells_in_ring)

    # middle rings (j = 1 ..)
    if rings_in_level != 1:
        for j in range(1, rings_in_level - 1):  # circles with same cell number
            for k in range(0, cells_in_ring):
                cell_index = first_level_index + j * cells_in_ring + k
                edge_list[cell_index].extend((cell_index - cells_in_ring, \
                                              cell_index + cells_in_ring))
                if k == 0:
                    edge_list[cell_index].extend((cell_index + 1, \
                                                  cell_index + cells_in_ring - 1))
                else:
                    edge_list[cell_index].extend((cell_index - 1, \
                                                  first_level_index + j * cells_in_ring + \
                                                  (k + 1) % cells_in_ring))

        # last ring in a level (j = circle in level - 1)
        for k in range(0, cells_in_ring):
            cell_index = first_level_index + (rings_in_level - 1) * cells_in_ring + k

            # cell below
            edge_list[cell_index].append(cell_index - cells_in_ring)
            if k == 0:
                edge_list[cell_index].extend((cell_index + 1, \
                                              cell_index + cells_in_ring - 1))
            else:
                edge_list[cell_index].extend((cell_index - 1, \
                                              first_level_index + (rings_in_level - 1) * cells_in_ring + \
                                              (k + 1) % cells_in_ring))

    return edge_list

def hexagon(n):
    """

    :param n:
    :return:
    """
    edge_list = [[] for _ in range(0, 3 * ((n - 1) ** 2 + n  - 1) + 1)]

    # edges from center cell to first ring
    edge_list[0].extend((i for i in range(1, 7)))
    edge_list[1].extend((0, 2, 6, 7, 8, 18))
    edge_list[6].extend((0, 1, 5, 16, 17, 18))
    # first ring

    for j in range(2, 6):
        edge_list[j].extend((0, j - 1, j + 1, 2*j + 4, 2*j + 5, 2*j + 6))

    for i in range(2, n - 1):
        # edges between rings
        first_index = 3 * ((i - 1) ** 2 + i - 1) + 1

        # first cell of the ring
        edge_list[first_index].extend((first_index - 6 * (i - 1), first_index + 1, first_index + 6 * i - 1, \
                                      first_index + 6 * i, first_index + 6 * i + 1, first_index + 12 * i + 5))

        for j in range(1, 6 * i - 1):
            if j % i == 0: # corner cell
                edge_list[first_index + j].extend((first_index - 6 * (i - 1) + j - j // i, \
                                                   first_index + j - 1, first_index + j + 1, \
                                                   first_index + 6 * i + j + j // i - 1, \
                                                   first_index + 6 * i + j + j // i, \
                                                   first_index + 6 * i + j + j // i + 1))
            else:
                edge_list[first_index + j].extend((first_index - 6 * (i - 1) + j - j // i - 1, \
                                                   first_index - 6 * (i - 1) + j - j // i,
                                                   first_index + j - 1, first_index + j + 1, \
                                                   first_index + 6 * i + j + j // i, \
                                                   first_index + 6 * i + j + j // i + 1))

        # last element of a ring
        edge_list[first_index + 6 * i - 1].extend((first_index - 6 * (i - 1), \
                                                   first_index - 1, \
                                                   first_index, \
                                                   first_index + 6 * i - 2, \
                                                   first_index + 12 * i + 4, \
                                                   first_index + 12 * i + 5))

    # last ring
    i = n - 1
    first_index = 3 * (i ** 2 - i) + 1

    # first cell of the ring
    edge_list[first_index].extend((first_index - 6 * (i - 1), first_index + 1, first_index + 6 * i - 1))

    for j in range(1, 6 * i - 1):
        if j % i == 0:  # corner cell
            edge_list[first_index + j].extend((first_index - 6 * (i - 1) + j - j // i, \
                                               first_index + j - 1, first_index + j + 1))

        else:
            edge_list[first_index + j].extend((first_index - 6 * (i - 1) + j - j // i - 1, \
                                               first_index - 6 * (i - 1) + j - j // i,
                                               first_index + j - 1, first_index + j + 1))

    edge_list[first_index + 6 * i - 1].extend((first_index - 6 * (i - 1), \
                                               first_index - 1, \
                                               first_index, \
                                               first_index + 6 * i - 2))

    return edge_list

def triangle(n):
    """

    :param n:
    :return:
    """
    edge_list = [[] for _ in range(0, n ** 2)]

    edge_list[0].append(2)

    for i in range(1, n - 1):
        # first cell of the row
        edge_list[i ** 2].extend((i ** 2 + 1, (i + 1) ** 2 + 1))

        # middle cells
        for j in range(1, 2 * i):
            edge_list[i ** 2 + j].extend((i ** 2 + j - 1, i ** 2 + j + 1))
            if j % 2 == 1:
                edge_list[i ** 2 + j].append((i - 1) ** 2 + j - 1)
            else:
                edge_list[i ** 2 + j].append((i + 1) ** 2 + j + 1)

        # last cell of the row
        edge_list[(i + 1) ** 2 - 1].extend(((i + 1) ** 2 - 2, (i + 2) ** 2 - 2))

    # last row
    edge_list[(n - 1) ** 2].append((n - 1) ** 2 + 1)

    for j in range(1, 2 * (n - 1)):
        edge_list[(n - 1) ** 2 + j].extend(((n - 1) ** 2 + j - 1, (n - 1) ** 2 + j + 1))
        if j % 2 == 1:
            edge_list[(n - 1) ** 2 + j].append(((n - 2) ** 2 + j - 1))

    edge_list[n ** 2 - 1].append(n ** 2 - 2)

    return edge_list

def octagon(n):
    k = 2*n - 1 # number of cells in a row (and column)
    edge_list = [[] for _ in range(k**2)]

    # corners
    edge_list[0].extend((1, k, k+1))
    edge_list[k-1].extend((k-2, 2*k - 2, 2*k - 1))
    edge_list[k**2 - k].extend((k**2 - 2*k, k**2 - 2*k + 1,  k**2 - k + 1))
    edge_list[k**2 - 1].extend((k**2 - k - 2, k**2 - k - 1, k**2 - 2))

    # frames
    # i = 0 first row
    for j in range(1, k - 1):
        edge_list[j].extend((j - 1, j + 1, k + j))
        if j % 2 == 0: # octagon
            edge_list[j].extend((j + k - 1, j + k + 1))

    # i = k - 1 last row
    for j in range(1, k - 1):
        edge_list[k**2 - k + j].extend((k**2 - 2*k + j, k**2 - k + j - 1, k** 2 - k + j + 1))
        if j % 2 == 0:  # octagon
            edge_list[k**2 - k + j].extend((k**2 - 2*k + j - 1, k**2 - 2*k + j + 1))

    # j = 0 first column
    for i in range(1, k - 1):
        edge_list[i * k].extend(((i - 1)*k, i*k + 1, (i + 1)*k))
        if i % 2 == 0:  # octagon
            edge_list[i * k].extend(((i - 1)*k + 1, (i + 1)*k + 1))

    # j = k - 1 last column
    for i in range(1, k - 1):
        edge_list[(i + 1)*k - 1].extend((i*k - 1, (i + 1)*k - 2, (i + 2)*k - 1))
        if i % 2 == 0:  # octagon
            edge_list[(i + 1) * k - 1].extend((i*k - 2, (i + 2)*k - 2))

    # else
    for i  in range(1, k - 1):
        for j in range(1, k - 1):
            edge_list[i*k + j].extend(((i - 1)*k + j, i*k + j - 1, i*k + j + 1, (i + 1)*k + j))
            if  (i + j) % 2 == 0: # octagon
                edge_list[i * k + j].extend(((i - 1)*k + j - 1, (i - 1)*k + j + 1, (i + 1)*k + j - 1, (i + 1)*k + j + 1))

    return edge_list