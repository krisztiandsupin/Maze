import pygame
from Color import Color
import MazeFunctions

class Edge:
    def __init__(self, start_cell, end_cell, wall):
        self.start_cell = start_cell
        self.end_cell = end_cell
        self.wall = wall

    def color(self, screen, line_color):
        pygame.draw.line(screen, line_color, self.wall[0], self.wall[1])

    def color_graph(self, screen, line_color):
        pygame.draw.line(screen, line_color, MazeFunctions.graph_position(self.start_cell.position), \
                         MazeFunctions.graph_position(self.end_cell.position))

    def draw_corners(self, screen, color = Color.black):
        pygame.draw.line(screen, color, self.wall[0], self.wall[0])
        pygame.draw.line(screen, color, self.wall[1], self.wall[1])
