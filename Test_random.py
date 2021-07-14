import time
import pygame
import AlgorithmSettings
import Functions
import GameSettings
import MazeFunctions
import Settings
from Color import Color
from Maze import Maze
from Settings import screen as screen_settings
from Text import Text
import math
import pyautogui

screen_size = screen_settings.screen_size

# Screen size
gameDisplay = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Maze')
pygame.init()

gameDisplay.fill(Color.white)
pygame.display.update()

text_color = Color.navy
text_color_light = Color.navy_light
text_size = 50
PI = math.pi

a = 30
r = a / (2 * math.sin(PI / 8))
m = a / (2 * math.tan(PI / 8))
n = 5

def polygon_points(n, center, r, rotation = 0):
    point_list = [(round(center[0] + r * math.cos(2 * i * PI / n + rotation)), round(center[1] + r * math.sin(2 * i * PI / n + rotation))) for
                  i in range(n)]
    return point_list

center = (screen_size[0] // 2, screen_size[1] //2)

b = m + a / 2

upper_left = (center[0] - (n - 1)*b, center[1] - (n - 1)*b)

grid_polygons = []

for column in range(2*n - 1):
    for row in range(2*n - 1):
        polygon_center = (upper_left[0] + row*b, upper_left[1] + column*b)
        if (row + column) % 2 == 0: # octagon
            octagon_radius = r
            polygon_point_list = polygon_points(8, polygon_center, octagon_radius, PI / 8)
        else:
            square_radius = a/math.sqrt(2)  # for square center
            polygon_point_list = polygon_points(4, polygon_center, square_radius, PI / 4)

        grid_polygons.append(polygon_point_list)
        pygame.draw.polygon(gameDisplay, Color.black, polygon_point_list, 1)


###############



gameDisplay.fill(Color.white)
pygame.display.update()

maze_hexagon1 = Maze(10, "hexagon", "kruskal")
maze_hexagon2 = Maze(10, "hexagon", "kruskal")
maze_hexagon1.create((int(screen_size[0] * 0.25), screen_size[1] // 2), 1, graph_bool=False)
maze_hexagon2.create((int(screen_size[0] * 0.75), screen_size[1] // 2), 1, graph_bool=False)

maze_octagon1 = Maze(10, "octagon", "kruskal")
maze_octagon2 = Maze(10, "octagon", "kruskal")
maze_octagon1.create((int(screen_size[0] * 0.25), screen_size[1] // 2), 1, graph_bool=False)
maze_octagon2.create((int(screen_size[0] * 0.75), screen_size[1] // 2), 1, graph_bool=False)

maze_circle1 = Maze(10, "circle", "kruskal")
maze_circle2 = Maze(10, "circle", "kruskal")
maze_circle1.create((int(screen_size[0] * 0.25), screen_size[1] // 2), 1, graph_bool=False)
maze_circle2.create((int(screen_size[0] * 0.75), screen_size[1] // 2), 1, graph_bool=False)

maze_triangle1 = Maze(20, "triangle", "kruskal")
maze_triangle2 = Maze(20, "triangle", "kruskal")
maze_triangle1.create((int(screen_size[0] * 0.25), screen_size[1] // 2), 1, graph_bool=False)
maze_triangle2.create((int(screen_size[0] * 0.75), screen_size[1] // 2), 1, graph_bool=False)


maze_hexagon1.draw(gameDisplay, graph_bool=False, visibility_bool=False)
maze_octagon2.draw(gameDisplay, graph_bool=False, visibility_bool=False)
pygame.image.save(gameDisplay, "maze1.png")

MazeFunctions.updete_delay(2000)
gameDisplay.fill(Color.white)

maze_circle1.draw(gameDisplay, graph_bool=False, visibility_bool=False)
maze_triangle2.draw(gameDisplay, graph_bool=False, visibility_bool=False)
pygame.image.save(gameDisplay, "maze2.png")

MazeFunctions.updete_delay(2000)
gameDisplay.fill(Color.white)

maze_octagon1.draw(gameDisplay, graph_bool=False, visibility_bool=False)
maze_triangle2.draw(gameDisplay, graph_bool=False, visibility_bool=False)
pygame.image.save(gameDisplay, "maze3.png")

MazeFunctions.updete_delay(2000)
gameDisplay.fill(Color.white)

maze_circle1.draw(gameDisplay, graph_bool=False, visibility_bool=False)
maze_hexagon2.draw(gameDisplay, graph_bool=False, visibility_bool=False)
pygame.image.save(gameDisplay, "maze4.png")

MazeFunctions.updete_delay(2000)
gameDisplay.fill(Color.white)

maze_triangle1.draw(gameDisplay, graph_bool=False, visibility_bool=False)
maze_hexagon2.draw(gameDisplay, graph_bool=False, visibility_bool=False)
pygame.image.save(gameDisplay, "maze5.png")

MazeFunctions.updete_delay(2000)
gameDisplay.fill(Color.white)

maze_circle1.draw(gameDisplay, graph_bool=False, visibility_bool=False)
maze_octagon2.draw(gameDisplay, graph_bool=False, visibility_bool=False)
pygame.image.save(gameDisplay, "maze6.png")

while True:
    Functions.buttonpress_detect()

    if Settings.keyboard_space_press:
        pygame.quit()
        raise SystemExit



    Functions.mouse_reset()
    MazeFunctions.updete_delay(10)


