import pygame, openpyxl, math, os, time
import mazefunc, mazealg, mazevis, solvealg

position=(0,30)
os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])
#os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

#size,location
n=20
#scr=(1530,790)
scr=(1280, 923)
labelsize=75
marginsize=15
a=mazefunc.rectSize(scr, n, marginsize, labelsize)                #size of edge of rectengular
loc=((scr[0] / 2 - n * a) / 2, labelsize)
line_thickness=1   #line thichness


#Screen size
gameDisplay = pygame.display.set_mode(scr)
#gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Maze')

#maze visualization
startime=time.time()
Grid=mazefunc.gridGen(n)
gameDisplay.fill(mazefunc.white)
pygame.display.update()

while True:
    startime = time.time()
    mazevis.SlideCover(n)
    mazevis.SlideParallelgen(n)
    mazevis.SlideKruskal(n//2)
    mazevis.SlideSidewinder(n//2)
    mazevis.SlideRecbtr(n//2)
    mazevis.SlidePrim(n//2)
    mazevis.SlideCover2(n)
    Grid,Maze=mazevis.SlideMazegen(n)
    mazevis.SlideParallelsol(n,Grid,Maze)
    mazevis.SlideWallfw(n,Grid,Maze)
    mazevis.SlideAstar(n,Grid,Maze)
    mazevis.SlideTremaux(n,Grid,Maze)
    mazevis.SlideDeadend(n,Grid,Maze)
    mazevis.SlideHexagonal(n)
    endtime=time.time()
    runtime=math.floor(endtime-startime)
    print('-----')
    minute=runtime//60
    second=runtime-minute*60

if second>=10:
    print('Total runtime: {0}:{1} ({2}s)'.format(minute,second,runtime))
else:
    print('Total runtime: {0}:0{1} ({2}s)'.format(minute, second, runtime))

'''while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # most reliable exit on x click
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            # optional exit with escape key
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit'''



