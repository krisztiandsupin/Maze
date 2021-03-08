import math
import MazeFunctions
class cell_astar:
    def __init__(self, cell, parent, step, distance):
        self.cell = cell
        self.parent = parent
        self.step = step
        self.distance = distance

def distance(type, cell1, cell2):
    if type == 0:
        return distance_square(cell1, cell2)
    elif type == 1:
        return distance_circle(cell1, cell2)
    elif type == 2:
        return distance_hexagon(cell1, cell2)
    elif type == 3:
        return distance_triangle(cell1, cell2)

def distance_square(cell1, cell2):
    return abs(cell1.coordinate[0] - cell2.coordinate[0]) + abs(cell1.coordinate[1] - cell2.coordinate[1])

def elements_in_ring(k): #number of elements of k-th ring
    if k == 0:
        return 1
    else:
        return 2 ** (math.floor(math.log(k, 2))  + 3)

def distance_circle(cell1, cell2):
    if cell1.coordinate[0] >= cell2.coordinate[0]:
        outer_cell = cell1
        inner_cell = cell2
    else:
        outer_cell = cell2
        inner_cell = cell1

    distance_list = []

    if inner_cell.coordinate != (0, 0):
        for i in range(0, math.floor(math.log(inner_cell.coordinate[0], 2)) + 1):  # path through k = 2**i - 1 th ring
            dist_temp = 0
            k = (2 ** i) - 1
            dist_temp += inner_cell.coordinate[0] - k
            dist_temp += outer_cell.coordinate[0] - k

            cell_increase_inner = int(math.log(elements_in_ring(inner_cell.coordinate[0]) // elements_in_ring(k), 2))
            cell_increase_outer = int(math.log(elements_in_ring(outer_cell.coordinate[0]) // elements_in_ring(k), 2))

            greater_ring_item = max(outer_cell.coordinate[1] // 2 ** cell_increase_outer,
                                    inner_cell.coordinate[1] // 2 ** cell_increase_inner)
            smaller_ring_item = min(outer_cell.coordinate[1] // 2 ** cell_increase_outer,
                                    inner_cell.coordinate[1] // 2 ** cell_increase_inner)

            distance3 = min(greater_ring_item - smaller_ring_item,
                            elements_in_ring(k) - greater_ring_item + smaller_ring_item)
            dist_temp += distance3

            distance_list.append(dist_temp)

    dist_temp = 0
    k = inner_cell.coordinate[0]
    dist_temp += inner_cell.coordinate[0] - k
    dist_temp += outer_cell.coordinate[0] - k

    cell_increase_inner = int(math.log(elements_in_ring(inner_cell.coordinate[0]) // elements_in_ring(k), 2))
    cell_increase_outer = int(math.log(elements_in_ring(outer_cell.coordinate[0]) // elements_in_ring(k), 2))

    greater_ring_item = max(outer_cell.coordinate[1] // 2 ** cell_increase_outer,
                            inner_cell.coordinate[1] // 2 ** cell_increase_inner)
    smaller_ring_item = min(outer_cell.coordinate[1] // 2 ** cell_increase_outer,
                            inner_cell.coordinate[1] // 2 ** cell_increase_inner)

    distance3 = min(greater_ring_item - smaller_ring_item, elements_in_ring(k) - greater_ring_item + smaller_ring_item)
    dist_temp += distance3

    distance_list.append(dist_temp)

    return (min(distance_list))

def distance_hexagon(cell1, cell2):
    # transform coordinates
    cell1_coordinate = MazeFunctions.coordinate_transform_hexagon(cell1.coordinate)
    cell2_coordinate = MazeFunctions.coordinate_transform_hexagon(cell2.coordinate)
    distance_vertical = cell1_coordinate[1] - cell2_coordinate[1]

    vertical_inliner1 = cell1_coordinate[0] - distance_vertical
    vertical_inliner2 = cell1_coordinate[0] + distance_vertical

    '''print('coordinates:')
    print('cell1', cell1.coordinate, '->', cell1_coordinate)
    print('cell2', cell2.coordinate, '->', cell2_coordinate)
    print('vertical dist:', distance_vertical)

    print('vertical inliners:', (vertical_inliner1, vertical_inliner2))'''

    if cell2_coordinate[0] >= min(vertical_inliner1, vertical_inliner2) and \
            cell2_coordinate[0] <= max(vertical_inliner1, vertical_inliner2):


        '''print('between inliners')
        print('distance:', abs(distance_vertical))'''
        return abs(distance_vertical)

    else:
        distance_horizontal = min(abs((cell2_coordinate[0] - vertical_inliner1) // 2), \
                                abs((cell2_coordinate[0] - vertical_inliner2) // 2))

        '''print('outside inliners')
        print('horizonal dist:', distance_horizontal)
        print('distance:', abs(distance_vertical) + distance_horizontal)
        print()'''

        return abs(distance_vertical) + distance_horizontal

def distance_triangle(cell1, cell2):
    distance_vertical =  abs(2 * (cell1.coordinate[0] - cell2.coordinate[0]))

    vertical_inliner1 = cell1.coordinate[1]
    vertical_inliner2 = cell1.coordinate[1] + distance_vertical

    '''    print('coordinates:')
    print('cell1', cell1.coordinate)
    print('cell2', cell2.coordinate)
    print('vertical dist:', distance_vertical)

    print('vertical inliners:', (vertical_inliner1, vertical_inliner2))'''

    if cell2.coordinate[1] >= min(vertical_inliner1, vertical_inliner2) and \
            cell2.coordinate[1] <= max(vertical_inliner1, vertical_inliner2):

        dist = distance_vertical + ((cell1.coordinate[1] - cell2.coordinate[1]) % 2)
        '''        print('between inliners')
        print('distance:', dist)
        print()'''
        return dist

    else:
        distance_horizontal = min(abs((cell2.coordinate[0] - vertical_inliner1)), \
                                  abs((cell2.coordinate[0] - vertical_inliner2)))

        '''print('outside inliners')
        print('horizonal dist:', distance_horizontal)
        print('distance:', abs(distance_vertical) + distance_horizontal)
        print()'''

        return distance_vertical + distance_horizontal

# Algorithms
def astar(type, cell_list, edges, start, end):
    weight = 2 # parameter for distance importance
    end_index = end.index
    start_astar = cell_astar(start.index, -1, 0, distance(type, start, end))

    '''print(start.index, end.index)
    print(edges)'''

    visited_index = set()
    visited_cells = []
    candidates = [start_astar]
    temp_cell = candidates.pop()

    while temp_cell.cell != end_index:
        print(temp_cell.cell)
        '''print('temp cell:', temp_cell.cell)'''

        visited_index.add(temp_cell.cell)
        visited_cells.append(temp_cell)

        neighbor_edges = edges[temp_cell.cell] # with indexes

        neighbor_set = set(neighbor_edges)
        '''print('visited:', visited_index)'''
        '''print('neighbors:', neighbor_set)'''

        next_cells = neighbor_set.difference(visited_index)
        '''print('next:', next_cells)'''

        for next in next_cells:
            candidates.append(cell_astar(cell_list[next].index, cell_list[temp_cell.cell].index, temp_cell.step + 1,
                                         weight * distance(type, cell_list[next], end) + temp_cell.step + 1))


        candidates.sort(key=lambda x: x.distance, reverse=True)
        temp_cell = candidates.pop()

    visited_cells.append(temp_cell)

    '''for a in visited_cells:
        print(a.cell, a.parent)'''

    temp_cell = visited_cells.pop()
    shortest_path = [cell_list[temp_cell.cell].index]

    highlight = []

    while temp_cell.parent != start.index or temp_cell.cell != shortest_path[-1]:
        highlight.append(([cell_list[temp_cell.cell]], [] ))
        '''print('cell:', temp_cell.cell, temp_cell.parent, shortest_path[-1].index)'''
        if temp_cell.cell == shortest_path[-1]:
            shortest_path.append(cell_list[temp_cell.parent].index)

        temp_cell = visited_cells.pop()
        '''print('next', temp_cell.cell, temp_cell.parent, start.index)'''

    highlight.append(([cell_list[temp_cell.cell]], []))
    '''for c in shortest_path:
        print(c.index)'''
    highlight.reverse()

    del highlight[-1]
    del shortest_path[0]

    return shortest_path, highlight

def endfiller(type, cell_list, edges, start, end):
    start_index = start.index
    end_index = end.index

    highlight = [] # list of tuples [([visited_list], [deadends])]
    shortest_path = []
    cell_number = len(cell_list)


    for i in range(0, cell_number):
        start_cell = i

        while len(edges[start_cell]) == 1 and start_cell != start_index and start_cell != end_index:
            end_cell = edges[start_cell][0]

            edges[start_cell].remove(end_cell)
            edges[end_cell].remove(start_cell)
            highlight.append(([], [cell_list[start_cell]]))

            start_cell = end_cell


    temp_index = start_index
    while temp_index != end_index:
        edges[edges[temp_index][0]].remove(temp_index)
        temp_index = edges[temp_index][0]
        shortest_path.append(cell_list[temp_index])

    del shortest_path[-1]

    return shortest_path, highlight