import pygame, openpyxl, math, os, time

import maze_functions
import maze_slides

from Settings import maze as maze_settings
from Settings import screen as screen_settings
from Settings import colors

n = maze_settings.n
position=(0,30)
os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])
#os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

#size,location
scr = screen_settings.screen_size
labelsize = screen_settings.labelsize
marginsize = screen_settings.marginsize
a = maze_settings.a
loc = maze_settings.location
line_thickness = screen_settings.line_thickness

#Screen size
gameDisplay = pygame.display.set_mode(scr)
#gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Maze')

#maze visualization
startime = time.time()
Grid = maze_functions.gridGen(n)
gameDisplay.fill(colors.white)
pygame.display.update()

#id = 0

while True:
    #startime = time.time()
    #maze_slides.SlideCover(n)
    #maze_slides.SlideParallelgen(n)
    #maze_slides.SlideKruskal(n//2)
    #maze_slides.SlideSidewinder(n//2)
    #maze_slides.SlideRecbtr(n//2)
    #maze_slides.SlidePrim(n//2)

    #maze_slides.SlideCover2(n)

    #Grid,Maze=maze_slides.SlideMazegen(n)
    #maze_slides.SlideParallelsol(n,Grid,Maze)
    #maze_slides.SlideWallfw(n,Grid,Maze)
    #maze_slides.SlideAstar(n,Grid,Maze)
    #maze_slides.SlideTremaux(n,Grid,Maze)
    #maze_slides.SlideDeadend(n,Grid,Maze)
    #maze_slides.SlideKruskal_rectengular(n, 5*n, id)
    #id += 1
    #time.sleep(5)
    maze_slides.SlideHexagonal(n)

    #gameDisplay.fill(colors.white)
    #pygame.draw.arc(gameDisplay, colors.black, [100,100, 1000, 1000], 0, 1)

    #endtime=time.time()
    #runtime=math.floor(endtime-startime)
    #print('-----')
    #minute = runtime//60
    #second = runtime-minute*60
    #if second>=10:
    #    print('Total runtime: {0}:{1} ({2}s)'.format(minute,second,runtime))
    #else:
    #    print('Total runtime: {0}:0{1} ({2}s)'.format(minute, second, runtime))

'''while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # most reliable exit on x click
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            # optional exit with escape key
            if event.key == pygame.K_ESCAPE:
                pygame.quit()'''

'''import pygame
import os
import time
import maze_functions as mf
import settings as st

from settings import map
from settings import maze_colors

class screen:
    length = 1024
    width = 768
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    infoObject = pygame.display.Info()
    pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
    game_display = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)

class maze:
    n = map.size
    start = map.start
    end = map.end

    vertices = list(range(0, n**2))
    edges = [[]*(n**2)]
    edge_list, edge_list_ordered, wall, wall_cover = mf.kruskal(n)



class slides:
    screen_height = 1024
    screen_width = 768

    game_display = pygame.display.set_mode((screen_height, screen_width), pygame.HWSURFACE)
    #game_display = pygame.display.set_mode((screen_height, screen_width), pygame.FULLSCREEN)

    #text positioning
    title = 'title'
    text_size = 50

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None

    def on_init(self):
        pygame.init()
        pygame.display.set_caption('Maze')
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def game_render(self):
        self.game_display.fill(st.colors.white)
        mf.text_display(self.game_display, self.screen_height // 2, 50, "Maze", 100, st.colors.navy, st.colors.white, True)
        mf.draw_grid(self.game_display, map.horizontal_position, map.vertical_position, map.size,
                                  map.square_size)

        start_horizontal_position = map.horizontal_position + (maze.start % map.size)*map.square_size
        start_vertical_position = map.vertical_position + (maze.start // map.size)*map.square_size

        mf.draw_rect(self.game_display, start_horizontal_position, start_vertical_position, map.square_size, maze_colors.start,
                     maze_colors.grid_line)

        end_horizontal_position = map.horizontal_position + (maze.end % map.size)*map.square_size
        end_vertical_position = map.vertical_position + (maze.end // map.size)*map.square_size
        mf.draw_rect(self.game_display, end_horizontal_position, end_vertical_position, map.square_size, maze_colors.end,
                     maze_colors.grid_line)

        pygame.display.flip()

        time.sleep(0.5)

        #self.game_display.fill(st.colors.white)
        #mf.text_display(self.game_display, self.screen_height // 2, 50, "Maze", 100, st.colors.navy, st.colors.white, True)

        #mf.draw_maze(self.game_display, map.horizontal_position, map.vertical_position, map.size, map.square_size, maze.wall)
        pygame.display.flip()


    def on_execute(self):
        self.game_render()

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()



            if (keys[pygame.K_ESCAPE]):
                self._running = False

        pygame.quit()

if __name__ == "__main__":
    maze_slide = slides()
    maze_slide.on_execute()'''