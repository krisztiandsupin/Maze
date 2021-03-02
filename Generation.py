import random
import math
from Edge import Edge
import MazeFunctions

def region_index(cell, region_list):
    length = len(region_list)
    i = 0

    while i < length:
        if cell in region_list[i]:
            return i
        i += 1

def edge_modify(edge_list, maze_edge, maze_order, cell_list, start_cell, end_cell, maze_type):
    edge_list[start_cell].remove(end_cell)
    edge_list[end_cell].remove(start_cell)

    maze_edge[start_cell].append(end_cell)

    maze_edge[end_cell].append(start_cell)

    MazeFunctions.border_update(maze_type, cell_list[start_cell], cell_list[end_cell])

    maze_order.append((cell_list[start_cell], cell_list[end_cell]))

#################################
# Algorithms
def generate(algorithm, type_value, cell_list, edge_list):
    if algorithm == 'kruskal':
        return kruskal(type_value, cell_list, edge_list)
    elif algorithm == 'prim':
        return prim(type_value, cell_list, edge_list)
    elif algorithm == 'backtracker':
        return backtracker(type_value, cell_list, edge_list)
    elif algorithm == 'eller':
        return None
    else:
        print('error: wrong type of algorithm')
        return None

def kruskal(maze_type, cell_list, edge_list):
    maze_edge = [[] for _ in range(0, len(edge_list))]
    maze_order = []
    cell_number = len(cell_list)
    edge_number = 0

    region_list = [[i] for i in range(0, cell_number)]

    while edge_number != cell_number - 1:
        start_cell = random.randint(0, cell_number - 1)

        if bool(edge_list[start_cell]):
            end_cell = random.choice(edge_list[start_cell])

            start_region = region_index(start_cell, region_list)
            end_region = region_index(end_cell, region_list)

        else:
            start_region = False
            end_region = False

        if start_region != end_region:
            '''maze_edge[start_cell].append(end_cell)
            maze_edge[end_cell].append(start_cell)

            edge_list[start_cell].remove(end_cell)
            edge_list[end_cell].remove(start_cell)

            maze_order.append((cell_list[start_cell], cell_list[end_cell]))'''
            edge_modify(edge_list, maze_edge, maze_order, cell_list, start_cell, end_cell, maze_type)

            edge_number += 1

            if start_region > end_region:
                start_region, end_region = end_region, start_region

            region_list[start_region] += region_list[end_region]
            region_list.remove(region_list[end_region])
            # border_update(edge_random.start_cell, edge_random.end_cell)

    return maze_edge, maze_order

def prim(type, cell_list, edge_list):
    maze_edge = [[] for _ in range(0, len(edge_list))]
    maze_order = []
    cell_number = len(cell_list)

    start = MazeFunctions.cell_endpoints_calculate(type, cell_list[-1].coordinate[0] - 1)[0]
    visited_cells = set()

    candidates = set()
    temp_cell = start

    while len(visited_cells) != cell_number - 1:
        visited_cells.add(temp_cell)

        neighbor_cells = set(edge_list[temp_cell])
        candidates = candidates.union(neighbor_cells.difference(visited_cells))

        end_cell = random.choice(tuple(candidates))
        start_cell = random.choice(tuple(set(edge_list[end_cell]).intersection(visited_cells)))

        edge_modify(edge_list, maze_edge, maze_order, cell_list, start_cell, end_cell)
        '''edge_list[start_cell].remove(end_cell)
        edge_list[end_cell].remove(start_cell)

        maze_edge[start_cell].append(end_cell)
        maze_edge[end_cell].append(start_cell)

        MazeFunctions.border_update(cell_list, cell_list[start_cell], cell_list[end_cell])

        maze_order.append((cell_list[start_cell], cell_list[end_cell]))'''
        candidates.remove(end_cell)
        temp_cell = end_cell

    return maze_edge, maze_order

def backtracker(type, cell_list, edge_list):
    maze_edge = [[] for _ in range(0, len(edge_list))]
    maze_order = []
    cell_number = len(cell_list)

    start = MazeFunctions.cell_endpoints_calculate(type, cell_list[-1].coordinate[0] - 1)[0]
    visited_cells = set()
    temp_cell = start

    while len(visited_cells) < cell_number:
        neighbor_cells = set(edge_list[temp_cell])
        candidates = neighbor_cells.difference(visited_cells)

        while bool(candidates) == True:
            visited_cells.add(temp_cell)
            start_cell = temp_cell
            end_cell = random.choice(tuple(candidates))

            '''edge_list[start_cell].remove(end_cell)
            edge_list[end_cell].remove(start_cell)

            maze_edge[start_cell].append(end_cell)
            maze_edge[end_cell].append(start_cell)
            maze_order.append((cell_list[start_cell], cell_list[end_cell]))'''
            edge_modify(edge_list, maze_edge, maze_order, cell_list, start_cell, end_cell)

            temp_cell = end_cell

            neighbor_cells = set(edge_list[temp_cell])

            visited_cells.add(temp_cell)
            candidates = neighbor_cells.difference(visited_cells)

        # backtracking
        i = 0
        while bool(candidates) == False and len(visited_cells) < cell_number:
            temp_cell = maze_order[-1 - i][0].index
            neighbor_cells = set(edge_list[temp_cell])
            candidates = neighbor_cells.difference(visited_cells)
            i += 1

    return maze_edge, maze_order