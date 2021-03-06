import math
import MazeFunctions

from Cell import Cell
from Settings import screen as screen_settings

PI = math.pi

def graph_position(cell_position):
    return (cell_position[0] + screen_settings.screen_size[0] // 2, cell_position[1])

def generate(type_value, size):
    if type_value == 0:
        return generate_square(size)
    elif type_value == 1:
        return generate_circle(size)
    elif type_value == 2:
        return generate_hexagon(size)
    elif type_value == 3:
        return generate_triangle(size)
    else:
        print('error: invalid maze type in cell list generation, cell type:', type_value)
        return []

def create(cell_list, type_value, maze_position, display_type, graph_bool, cell_size):
    if type_value == 0:
        return create_square(cell_list, maze_position, display_type, graph_bool, cell_size)
    elif type_value == 1:
        return create_circle(cell_list, maze_position, display_type, graph_bool, cell_size)
    elif type_value == 2:
        return create_hexagon(cell_list, maze_position, display_type, graph_bool, cell_size)
    elif type_value == 3:
        return generate_triangle(10)
    else:
        print('error: invalid maze type in cell list creation, cell type:', type_value)
        return []


def generate_square(n):
    cell_list = []

    for row in range(0, n):
        for column in range(0, n):
            cell_walls_bool = [True, True, True, True]  # order: [left, up, right, down]
            cell_index = row * n + column
            cell = Cell((row, column), cell_index, cell_walls_bool)

            cell_list.append(cell)  # list of cell type objects

    return cell_list

def create_square(cell_list, maze_position, display_type, graph_bool, cell_size):
    if bool(cell_list):
        maze_size = int(math.sqrt(len(cell_list))) # number of rows and columns

        half_size = cell_size // 2

        # upper left corner of the grid
        grid_start_horizontal = int((maze_position[0] - maze_size * cell_size / 2))
        grid_start_vertical = int((maze_position[1] - maze_size * cell_size / 2))

        for cell in cell_list:
            cell_center_horizontal = grid_start_horizontal + int((cell.coordinate[1]+ 0.5) * cell_size)
            cell_center_vertical = grid_start_vertical + int((cell.coordinate[0] + 0.5) * cell_size)
            cell.position = (cell_center_horizontal, cell_center_vertical)

            if graph_bool == True:
                translation = int(screen_settings.screen_size[0] / (2 ** (display_type + 1)))
                graph_center = (cell_center_horizontal + translation, cell_center_vertical)
                cell.graph_position = graph_center

            border_point0 = (cell_center_horizontal - half_size, cell_center_vertical + half_size)
            border_point1 = (cell_center_horizontal - half_size, cell_center_vertical - half_size)
            border_point2 = (cell_center_horizontal + half_size, cell_center_vertical - half_size)
            border_point3 = (cell_center_horizontal + half_size, cell_center_vertical + half_size)

            cell.border_points = (border_point0, border_point1, border_point2, border_point3)
            cell.walls = ((border_point0, border_point1), (border_point1, border_point2),
                          (border_point3, border_point2), (border_point0, border_point3))

    else:
        print('maze is not generated')

def generate_circle(n):
    cell_index = 0

    center_walls_bool = [True for _ in range(0, 8)]
    cell_center = Cell((0, 0), cell_index, center_walls_bool)

    cell_list = [cell_center]
    cell_index += 1

    for i in range(1, n):
        cell_number = 2 ** (math.ceil(math.log(i + 1, 2)) + 2)  # cell number in a ring

        for j in range(0, cell_number):
            if math.log(i, 2).is_integer() == True and i > 1:
                cell_walls_bool = [True for _ in range(0, 4)]

            else:
                if math.log(i + 1, 2).is_integer() == True:  # pentagon
                     cell_walls_bool = [True for _ in range(0, 5)]

                else:  # Quadrilateral
                    cell_walls_bool = [True for _ in range(0, 4)]

            cell = Cell((i, j), cell_index, cell_walls_bool)
            cell_list.append(cell)  # list of cell type objects

            cell_index += 1

    return cell_list

def create_circle(cell_list, maze_position, display_type, graph_bool, cell_size):
    # center cell
    n = cell_list[-1].coordinate[0] + 1
    (x,y) = maze_position

    center_walls = []
    center_border_points = []
    cell_number = 8

    # rotation angle: plus rotation to guarantee adjacency
    if math.log(n, 2).is_integer() == True:
        rotation_angle = PI / (2 ** (math.floor(math.log(n, 2)) + 2))
    else:
        rotation_angle = PI / (2 ** (math.floor(math.log(n, 2)) + 3))

    for i in range(0, cell_number):
        ring_angle = 1 / cell_number * 2 * PI
        angle = i * ring_angle - (ring_angle / 2) - rotation_angle
        start_wall_point = (round(x + 0.5 * cell_size * math.cos(angle)), round(y + 0.5 * cell_size * math.sin(angle)))

        angle = (i + 1) % cell_number * ring_angle - (ring_angle / 2) - rotation_angle
        end_wall_point = (round(x + 0.5 * cell_size * math.cos(angle)), round(y + 0.5 * cell_size * math.sin(angle)))

        center_walls.append((start_wall_point, end_wall_point))
        center_border_points.append(start_wall_point)

    cell_list[0].position = (x,y)
    if graph_bool == True:
        translation = int(screen_settings.screen_size[0] / (2 ** (display_type + 1)))
        graph_center = (x + translation, y)
        cell_list[0].graph_position = graph_center

    cell_list[0].border_points = center_border_points
    cell_list[0].walls = center_walls

    cell_index = 1
    for i in range(1, n):
        cell_number = 2 ** (math.ceil(math.log(i + 1, 2)) + 2)  # cell number in a ring

        for j in range(0, cell_number):
            ring_angle = 1 / cell_number * 2 * PI

            if math.log(i, 2).is_integer() == True and i > 1:
                angle = j * ring_angle - (ring_angle / 2) - rotation_angle
                cell_center = (round(x + i * cell_size * math.cos(angle)), round(y + i * cell_size * math.sin(angle)))
                graph_center = graph_position(cell_center)

                angle = j * ring_angle - 2 * (ring_angle / 2) - rotation_angle
                border_point1 = (round(x + (i - 0.5) * cell_size * math.cos(angle)), round(y + (i - 0.5) * cell_size * math.sin(angle)))
                border_point2 = (round(x + (i + 0.5) * cell_size * math.cos(angle)), round(y + (i + 0.5) * cell_size * math.sin(angle)))

                angle = j * ring_angle + 0 * (ring_angle / 2) - rotation_angle
                border_point3 = (round(x + (i + 0.5) * cell_size * math.cos(angle)), round(y + (i + 0.5) * cell_size * math.sin(angle)))
                border_point4 = (round(x + (i - 0.5) * cell_size * math.cos(angle)), round(y + (i - 0.5) * cell_size * math.sin(angle)))

                cell_border_points = [border_point1, border_point2, border_point3, border_point4]
                cell_walls = [(border_point1, border_point2), (border_point2, border_point3),
                              (border_point4, border_point3), (border_point1, border_point4)]
                cell_walls_bool = [True for _ in range(0, 4)]

            else:
                angle = j * ring_angle - rotation_angle
                cell_center = (round(x + i * cell_size * math.cos(angle)), round(y + i * cell_size * math.sin(angle)))

                angle = j * ring_angle - 1 * (1 / cell_number * PI) - rotation_angle
                border_point1 = (round(x + (i - 0.5) * cell_size * math.cos(angle)), round(y + (i - 0.5) * cell_size * math.sin(angle)))
                border_point2 = (round(x + (i + 0.5) * cell_size * math.cos(angle)), round(y + (i + 0.5) * cell_size * math.sin(angle)))

                angle = j * ring_angle + 1 * (1 / cell_number * PI) - rotation_angle
                border_point3 = (round(x + (i + 0.5) * cell_size * math.cos(angle)), round(y + (i + 0.5) * cell_size * math.sin(angle)))
                border_point4 = (round(x + (i - 0.5) * cell_size * math.cos(angle)), round(y + (i - 0.5) * cell_size * math.sin(angle)))

                if math.log(i + 1, 2).is_integer() == True:  # pentagon
                    angle = j * ring_angle - 0 * (1 / cell_number * PI) - rotation_angle
                    border_point5 = (
                    round(x + (i + 0.5) * cell_size * math.cos(angle)), round(y + (i + 0.5) * cell_size * math.sin(angle)))
                    cell_border_points = [border_point1, border_point2, border_point5, border_point3, border_point4]
                    cell_walls = [(border_point1, border_point2), (border_point2, border_point5),
                                  (border_point5, border_point3), (border_point4, border_point3),
                                  (border_point1, border_point4)]

                else:  # Quadrilateral
                    cell_border_points = [border_point1, border_point2, border_point3, border_point4]
                    cell_walls = [(border_point1, border_point2), (border_point2, border_point3),
                                  (border_point4, border_point3), (border_point1, border_point4)]

            cell_list[cell_index].position = cell_center
            if graph_bool == True:
                translation = int(screen_settings.screen_size[0] / (2 ** (display_type + 1)))
                graph_center = (cell_center[0] + translation, cell_center[1])
                cell_list[cell_index].graph_position = graph_center

            cell_list[cell_index].border_points = cell_border_points
            cell_list[cell_index].walls = cell_walls

            cell_index += 1
        if math.log(i, 2).is_integer() == True and i > 1:
            rotation_angle += (1 / cell_number * PI)

    return cell_list

def cell_border_points_hexagon(cell_center, a):
    base_angle = 150 * PI / 180
    return [(round(cell_center[0] + a * math.cos(base_angle + j * PI / 3)), \
            round(cell_center[1] + a * math.sin(base_angle + j * PI / 3))) for j in range(0, 6)]

def cell_wall_hexagon(cell_border_points):
    return [(cell_border_points[0], cell_border_points[1]), (cell_border_points[1], cell_border_points[2]), \
            (cell_border_points[3], cell_border_points[2]), (cell_border_points[4], cell_border_points[3]), \
            (cell_border_points[5], cell_border_points[4]), (cell_border_points[5], cell_border_points[0])]

def generate_hexagon(n):
    cell_list = []

    walls_bool = [True for _ in range(0, 6)]
    cell = Cell((0, 0), 0, walls_bool)

    cell_list.append(cell)

    for ring in range(1, n):
        for j in range(0, 6*ring):
            walls_bool = [True for _ in range(0, 6)]
            cell_coordinate = (ring, j)
            index = (ring * (ring + 1)) // 2 + j
            cell = Cell(cell_coordinate, index, walls_bool)
            cell_list.append(cell)
    return cell_list

def create_hexagon(cell_list, maze_position, display_type, graph_bool, cell_size):
    A = math.sqrt(3) / 2 * cell_size

    # center cell
    (x, y) = maze_position

    cell_position_list = []  # elements [tuple]: (coordinate [tuple], position [position])

    # center cell
    cell_position_list.append((x, y))

    n = cell_list[-1].coordinate[0] + 1
    for ring in range(1, n):
        for j in range(0, ring + 1):
            cell_position = (x + (2 * ring - j) * A, y + j * 1.5 * cell_size)
            cell_position_list.append(cell_position)

        for j in range(1, ring + 1):
            cell_position = (x + (ring - j * 2) * A, y + ring * 1.5 * cell_size)
            cell_position_list.append(cell_position)

        for j in range(1, ring):
            cell_position = (x + (- 1 * ring - j) * A, y + (ring - j) * 1.5 * cell_size)
            cell_position_list.append(cell_position)

        # (-1) * first three
        for j in range(0, ring + 1):
            cell_position = (x - (2 * ring - j) * A, y - j * 1.5 * cell_size)
            cell_position_list.append(cell_position)

        for j in range(1, ring + 1):
            cell_position = (x - (ring - j * 2) * A, y - ring * 1.5 * cell_size)
            cell_position_list.append(cell_position)

        for j in range(1, ring):
            cell_position = (x - (- 1 * ring - j) * A, y - (ring - j) * 1.5 * cell_size)
            cell_position_list.append(cell_position)

    for i in range(0, len(cell_list)):
        element = cell_position_list[i]

        if graph_bool == True:
            translation = int(screen_settings.screen_size[0] / (2 ** (display_type + 1)))
            graph_center = (int(element[0] + translation), int(element[1]))
            cell_list[i].graph_position = graph_center

        cell_list[i].position = (round(element[0]), round(element[1]))
        cell_list[i].border_points = cell_border_points_hexagon(element, cell_size)
        cell_list[i].walls = cell_wall_hexagon(cell_list[i].border_points)


def generate_triangle(n, a):
    A = math.sqrt(3) / 2 * a
    B = 2 * A / 3
    grid_upper_center = (screen_settings.screen_size[0]  // 4, \
                        (screen_settings.screen_size[1] - n * A) // 2)

    cell_list = []

    for i in range(0, n):
        for j in range(0, 2 * i + 1):
            cell_center = (grid_upper_center[0] + ((j - i) * a / 2), \
                           grid_upper_center[1] + (i  + 0.5) * A)

            graph_center = graph_position(cell_center)
            cell_index = i ** 2 + j

            if j % 2 == 0:
                border_point0 = (round(cell_center[0] - a / 2), round(cell_center[1] + A / 2))
                border_point1 = (round(cell_center[0]), round(cell_center[1] - A / 2))
                border_point2 = (round(cell_center[0] + a / 2), round(cell_center[1] + A / 2))
            else:
                border_point0 = (round(cell_center[0] - a / 2), round(cell_center[1] - A / 2))
                border_point1 = (round(cell_center[0]), round(cell_center[1] + A / 2))
                border_point2 = (round(cell_center[0] + a / 2), round(cell_center[1] - A / 2))


            cell_border_points = [border_point0, border_point1, border_point2]

            cell_walls = [(cell_border_points[k], cell_border_points[(k + 1) % 3]) for k in range(0, 3)]
            cell_walls_bool = [True for _ in range(0, 3)]

            cell = Cell((i, j), (round(cell_center[0]), round(cell_center[1])), \
                        (round(graph_center[0]), round(graph_center[1])), cell_index, cell_walls,cell_walls_bool, \
                        cell_border_points)
            cell_list.append(cell)  # list of cell type objects

    return cell_list
