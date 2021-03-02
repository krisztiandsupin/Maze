'''import pygame
import math
import random
import maze_functions as mf

from Color import Color as colors
from Cell import Cell
from settings import screen as screen_settings
from settings import maze as maze_settings

pi = math.pi

global coordinate_text_size
coordinate_text_size = 9




class CellCircle:
    def __init__(self, coord, pos, index, walls = -1, walls_bool = -1, border_points = -1):
        self.coordinate = coord
        self.position = pos
        self.index = index
        self.walls = walls                  #points of walls
        self.walls_bool = walls_bool        #tuple of walls, if they exists or not
        self.borders = border_points        #list of border points of a cell

    def generation(x, y, n, a):
        #center cell
        center_walls = []
        center_borders = []
        cell_number = 8
        cell_index = 0
        max_ring_index = [1] #index of the first element of each ring

        #rotation angle: plus rotation to guarantee adjacency
        if math.log(n, 2).is_integer() == True:
            rotation_angle = pi / (2 ** (math.floor(math.log(n, 2))  + 2))
        else:
            rotation_angle = pi / (2 ** (math.floor(math.log(n, 2)) + 3))


        for i in range(0, cell_number):
            ring_angle = 1 / cell_number * 2 * pi
            angle = i * ring_angle - (ring_angle / 2) - rotation_angle
            start_wall_point = (round(x + 0.5 * a * math.cos(angle)), round(y + 0.5 * a * math.sin(angle)))

            angle = (i + 1) % cell_number * ring_angle - (ring_angle / 2) - rotation_angle
            end_wall_point = (round(x + 0.5 * a * math.cos(angle)), round(y + 0.5 * a * math.sin(angle)))

            center_walls.append((start_wall_point, end_wall_point))
            center_borders.append(start_wall_point)

        center_wall_bool = [True for _ in range(0, 8)]
        cell_center = CellCircle((0, 0), (x, y), cell_index, center_walls, center_wall_bool, center_borders)
        cell_list = [cell_center]
        cell_index += 1

        for i in range(1, n):
            cell_number = 2 ** (math.ceil(math.log(i + 1, 2)) + 2) #cell number in a ring

            for j in range(0, cell_number):
                ring_angle = 1 / cell_number * 2 * pi

                if math.log(i, 2).is_integer() == True and i > 1:
                    angle = j * ring_angle - (ring_angle / 2) - rotation_angle
                    cell_center = (round(x + i * a * math.cos(angle)), round(y + i * a * math.sin(angle)))

                    angle = j * ring_angle - 2 * (ring_angle / 2) - rotation_angle
                    border_point1 = (round(x + (i - 0.5) * a * math.cos(angle)), round(y + (i - 0.5) * a * math.sin(angle)))
                    border_point2 = (round(x + (i + 0.5) * a * math.cos(angle)), round(y + (i + 0.5) * a * math.sin(angle)))

                    angle = j * ring_angle + 0 * (ring_angle / 2) - rotation_angle
                    border_point3 = (round(x + (i + 0.5) * a * math.cos(angle)), round(y + (i + 0.5) * a * math.sin(angle)))
                    border_point4 = (round(x + (i - 0.5) * a * math.cos(angle)), round(y + (i - 0.5) * a * math.sin(angle)))

                    cell_borders = [border_point1, border_point2, border_point3, border_point4]
                    cell_walls = [(border_point1, border_point2), (border_point2, border_point3),
                                  (border_point4, border_point3), (border_point1, border_point4)]
                    cell_walls_bool = [True for _ in range(0, 4)]

                else:
                    angle = j * ring_angle - rotation_angle
                    cell_center = (round(x + i * a * math.cos(angle)), round(y + i * a * math.sin(angle)))

                    angle = j * ring_angle - 1 * (1 / cell_number * pi) - rotation_angle
                    border_point1 = (round(x + (i - 0.5) * a * math.cos(angle)), round(y + (i - 0.5) * a * math.sin(angle)))
                    border_point2 = (round(x + (i + 0.5) * a * math.cos(angle)), round(y + (i + 0.5) * a * math.sin(angle)))

                    angle = j * ring_angle + 1 * (1 / cell_number * pi) - rotation_angle
                    border_point3 = (round(x + (i + 0.5) * a * math.cos(angle)), round(y + (i + 0.5) * a * math.sin(angle)))
                    border_point4 = (round(x + (i - 0.5) * a * math.cos(angle)), round(y + (i - 0.5) * a * math.sin(angle)))

                    if math.log(i + 1, 2).is_integer() == True:  # pentagon
                        angle = j * ring_angle - 0 * (1 / cell_number * pi) - rotation_angle
                        border_point5 = (round(x + (i + 0.5) * a * math.cos(angle)), round(y + (i + 0.5) * a * math.sin(angle)))
                        cell_borders = [border_point1, border_point2, border_point5, border_point3, border_point4]
                        cell_walls = [(border_point1, border_point2), (border_point2, border_point5),
                                      (border_point5, border_point3), (border_point4, border_point3),
                                      (border_point1, border_point4)]
                        cell_walls_bool = [True for _ in range(0, 5)]

                    else:  #Quadrilateral
                        cell_borders = [border_point1, border_point2, border_point3, border_point4]
                        cell_walls = [(border_point1, border_point2), (border_point2, border_point3),
                                      (border_point4, border_point3), (border_point1, border_point4)]
                        cell_walls_bool = [True for _ in range(0, 4)]

                cell = Cell(CellCircle((i, j), cell_center, cell_index, cell_walls, cell_walls_bool, cell_borders))
                cell_list.append(cell)  #list of cell type objects

                cell_index += 1

            if math.log(i, 2).is_integer() == True and i > 1:
                rotation_angle += (1 / cell_number * pi)

            max_ring_index.append(cell_index)

        return cell_list, max_ring_index

    def color_graph(self, screen, color, size = maze_settings.graph_vertex_size):
        pygame.draw.circle(screen, colors.white, mf.graph_position(self.position), maze_settings.graph_vertex_highlight_size)
        pygame.draw.circle(screen, color, mf.graph_position(self.position), size)

    def color(self, screen, color, coordinate_text_bool = False, graph_bool = False):
        pygame.draw.polygon(screen, color, self.borders)
        l = len(self.walls)

        for i in range(0, l):
            if self.walls_bool[i] == True:
                pygame.draw.line(screen, colors.black, self.walls[i][0], self.walls[i][1])
            else:
                pygame.draw.line(screen, color, self.walls[i][0], self.walls[i][1])

        if coordinate_text_bool == True:
            self.text_display(screen, str(self.coordinate), coordinate_text_size, colors.black, color)

        if graph_bool == True:
            self.color_graph(screen, color, maze_settings.graph_vertex_highlight_size)

    def text_display(self, screen, text, text_size, text_color = colors.black, highlight_color = colors.white):
        mf.text_display(screen, self.position[0], self.position[1], text, text_size, text_color, highlight_color)

    def border_update(cell1, cell2): #suppese that they are adjacent, and cell1 < cell2
        if cell1.coordinate[0] == cell2.coordinate[0]: #in the same ring
            if math.log(cell2.coordinate[0] + 1, 2).is_integer() == True:
                cell1.walls_bool[3] = False
                cell2.walls_bool[0] = False
            else:
                cell1.walls_bool[2] = False
                cell2.walls_bool[0] = False

        else:   #in different rings
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

class Edge:
    def __init__(self, edge):
        self.start_cell = edge.start_cell
        self.end_cell = edge.end_cell
        self.wall = edge.wall

    def color(self, screen, line_color):
        pygame.draw.line(screen, line_color, self.wall[0], self.wall[1])

    def color_graph(self, screen, line_color):
        pygame.draw.line(screen, line_color, mf.graph_position(self.start_cell.position), \
                                        mf.graph_position(self.end_cell.position))

    def draw_corners(self, screen):
        pygame.draw.line(screen, colors.black, self.wall[0], self.wall[0])
        pygame.draw.line(screen, colors.black, self.wall[1], self.wall[1])

class EdgeCircle:
    def __init__(self, start_cell, end_cell, wall_position):
        self.start_cell = start_cell
        self.end_cell = end_cell
        self.wall = wall_position

    def generation(n, cell_list, max_ring_index):
        edge_list = []

        #edges from center cell to first ring
        for i in range(1, 9):
            wall = [cell_list[i].borders[0], cell_list[i].borders[-1]]
            edge = Edge(EdgeCircle(cell_list[0], cell_list[i], wall))
            edge_list.append(edge)

        #edges between rings
        for i in range(1, n - 1):
            if (max_ring_index[i + 1] - max_ring_index[i]) == (max_ring_index[i] - max_ring_index[i - 1]): #same number of cells in rings
                difference = max_ring_index[i] - max_ring_index[i - 1]
                for j in range(max_ring_index[i - 1], max_ring_index[i]):
                    wall = [cell_list[j].borders[1], cell_list[j].borders[2]]
                    edge = Edge(EdgeCircle(cell_list[j], cell_list[j + difference], wall))
                    edge_list.append(edge)

            else:   #different number of cells in rings
                k = 0
                difference = max_ring_index[i] - max_ring_index[i - 1]
                for j in range(max_ring_index[i - 1], max_ring_index[i]):
                    wall = [cell_list[j].borders[1], cell_list[j].borders[2]]
                    edge = Edge(EdgeCircle(cell_list[j], cell_list[j + difference + k], wall))
                    edge_list.append(edge)

                    wall = [cell_list[j].borders[2], cell_list[j].borders[3]]
                    edge = Edge(EdgeCircle(cell_list[j], cell_list[j + difference + k + 1], wall))
                    edge_list.append(edge)
                    k += 1

        #edges in a ring
        for i in range(0, n - 1):
            for j in range(max_ring_index[i], max_ring_index[i+1] - 1):
                wall = [cell_list[j].borders[-1], cell_list[j].borders[-2]]
                edge = Edge(EdgeCircle(cell_list[j], cell_list[j + 1], wall))
                edge_list.append(edge)

            wall = [cell_list[j+1].borders[-1], cell_list[j+1].borders[-2]]
            edge = Edge(EdgeCircle(cell_list[j + 1], cell_list[max_ring_index[i]], wall))
            edge_list.append(edge)

        frame_list = []
        for j in range(max_ring_index[n - 2], max_ring_index[n-1]):
            wall = [cell_list[j].borders[1], cell_list[j].borders[2]]
            frame_list.append(wall)

        return edge_list, frame_list





'''