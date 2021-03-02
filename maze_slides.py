#maze visualize
import pygame, openpyxl, math, time
import maze_functions
import maze_generating
import maze_solving

from Settings import maze as maze_settings
from Settings import screen as screen_settings
from Settings import colors

#size,location
n = maze_settings.n
scr = screen_settings.screen_size
labelsize = screen_settings.labelsize
marginsize = screen_settings.marginsize
a = maze_settings.a
loc = maze_settings.location
line_thickness = screen_settings.line_thickness
gameDisplay = pygame.display.set_mode(scr)

Grid=maze_functions.gridGen(n)
delay = screen_settings.delay
statBool = screen_settings.statBool


def SlideCover(n):
    starttime = time.time()
    gameDisplay.fill(colors.white)
    mazecol = (maze_settings.bgrcol, colors.dgrey, colors.llgreen, colors.lsalmon)
    n = 2 * n
    x = (scr[0] - n * a) / 2
    y = (scr[1] - n * a) / 2
    Grid, Maze = maze_generating.mazePrim(gameDisplay, x, y, n, a, mazecol, -1,False)

    fontsize = 100
    maze_functions.drawGrid2(gameDisplay, x, y, n, a, Grid, mazecol)
    x1= scr[0] / 2
    y1= scr[1] / 2 - math.floor(fontsize * 3 / 4)
    y2= scr[1] / 2 + math.floor(fontsize * 3 / 4)

    maze_functions.textDisplay(gameDisplay, x1,y1,'Maze',  math.floor(fontsize*3/2), colors.navy)
    maze_functions.textDisplay(gameDisplay, x1, y2,'Creation & solving algorithms',  fontsize, colors.navy)
    pygame.display.update()

    x3= scr[0] - 150
    y3= scr[1] - 50
    maze_functions.textDisplay(gameDisplay, x3, y3, 'develeped by Krisztian Dsupin', fontsize//4, colors.navy)
    maze_functions.textDisplay(gameDisplay, x3, y3+fontsize//4, 'krisztian.dsupin@gmail.com', fontsize // 4, colors.navy)
    pygame.display.update()
    pygame.time.delay(2000)

    gameDisplay.fill(colors.white)
    pygame.display.update()
    maze_functions.drawGrid2(gameDisplay,x,y,n,a,Grid,mazecol)
    maze_functions.textDisplay(gameDisplay, x1, y1+math.floor(fontsize*3/4), 'Maze creation algorithms', fontsize, colors.navy)
    maze_functions.textDisplay(gameDisplay, x3, y3, 'develeped by Krisztian Dsupin', fontsize // 4, colors.navy)
    maze_functions.textDisplay(gameDisplay, x3, y3 + fontsize // 4, 'krisztian.dsupin@gmail.com', fontsize // 4,
                         colors.navy)
    pygame.display.update()
    pygame.time.delay(2000)
    endtime=time.time()
    runtime=endtime-starttime
    print('Cover runtime: {0:.2f}s'.format(runtime))
    maze_functions.systemExit()

def SlideParallelgen(n):
    starttime = time.time()
    logBool=True
    fontsize=50
    Edges, Maze, Grid = maze_functions.mazeCreate(n)
    gameDisplay.fill(colors.white)
    mazecol=(maze_functions.bgrcol,maze_functions.lncol,colors.lgreen,colors.salmon)
    pygame.draw.line(gameDisplay, colors.navy, (scr[0] / 2, 0), (scr[0] / 2, scr[1]), 2)
    pygame.draw.line(gameDisplay, colors.navy, (0, scr[1] / 2), (scr[0], scr[1] / 2), 2)

    maze_functions.drawGrid(gameDisplay, loc[0], loc[1], n, a, Grid, (colors.dgrey,colors.black,colors.dgrey,colors.dgrey))
    maze_functions.textDisplay(gameDisplay, scr[0] / 4, labelsize / 2, 'Kruskal\'s algorithm', fontsize, colors.navy)

    maze_functions.drawGrid(gameDisplay, loc[0] + scr[0] / 2, loc[1], n, a, Grid, (colors.dgrey,colors.black,colors.dgrey,colors.dgrey))
    maze_functions.textDisplay(gameDisplay, scr[0] * 3 / 4, labelsize / 2, 'Sidewinder algorithm', fontsize, colors.navy)

    maze_functions.drawGrid(gameDisplay, loc[0], loc[1] + scr[1] / 2, n, a, Grid, (colors.dgrey,colors.black,colors.dgrey,colors.dgrey))
    maze_functions.textDisplay(gameDisplay, scr[0] / 4, scr[1] / 2 + labelsize / 2, 'Recursive backtracker algorithm',
                         fontsize, colors.navy)

    maze_functions.drawGrid(gameDisplay, loc[0] + scr[0] / 2, loc[1] + scr[1] / 2, n, a, Grid, (colors.dgrey,colors.black,colors.dgrey,colors.dgrey))
    maze_functions.textDisplay(gameDisplay, scr[0] * 3 / 4, scr[1] / 2 + labelsize / 2, 'Prim\'s algorithm', fontsize,
                         colors.navy)

    pygame.display.update()
    pygame.time.delay(500)

    # maze log
    delay = 10
    #Kruskal
    EdgesKruskal, MazeKruskal, GridKruskal = maze_functions.mazeCreate(n); RegionsKruskal=maze_functions.regionGen(n)
    VisitedKruskal=[False for i in range(0,n**2)]
    boolKruskal=False
    #Sidewinder
    EdgesSidewr, MazeSidewr, GridSidewr = maze_functions.mazeCreate(n);
    VisitedSidewr=[False for i in range(0,n**2)]; tempList=[]; rowList=[]
    boolSidewr=False
    #Recursive backtracker
    EdgesRecbtr, MazeRecbtr, GridRecbtr= maze_functions.mazeCreate(n); CheckedRecbtr=[0]; newVertex=0
    VisitedRecbtr = [False for i in range(0, n ** 2)]
    boolRecbtr=False
    #Prim
    EdgesPrim, MazePrim, GridPrim = maze_functions.mazeCreate(n);
    VisitedPrim = [False for i in range(0, n ** 2)]; CheckedPrim=[0]; NeighborsPrim=maze_functions.regionNeighbor(n,CheckedPrim[-1])
    boolPrim = False

    k=0
    x1=loc[0]; y1=loc[1]
    x2=loc[0]+scr[0]/2; y2=loc[1]
    x3=loc[0]; y3= loc[1] + scr[1] / 2
    x4=loc[0]+scr[0]/2; y4=loc[1]+scr[1] / 2
    while boolKruskal==False or boolRecbtr==False or boolSidewr==False or boolPrim==False:
        if k%4==0 and boolKruskal==False:
            EdgesKruskal, MazeKruskal, GridKruskal, VisitedKruskal,RegionsKruskal,k, boolKruskal = maze_generating.mazeKruskalparallel(gameDisplay,x1,y1,n,a,mazecol,delay,
                                                                         EdgesKruskal,MazeKruskal,GridKruskal,VisitedKruskal,RegionsKruskal, k,boolKruskal)
            #print('Kruskal', k)
        k += 1

        if k%4==1 and boolSidewr==False:
            EdgesSidewr, MazeSidewr, GridSidewr,rowList,tempList,VisitedSidewr,k, boolSidewr = maze_generating.mazeSidewrparallel(
                gameDisplay, x2, y2, n, a, mazecol, delay,
                EdgesSidewr, MazeSidewr, GridSidewr,tempList,rowList, VisitedSidewr, k, boolSidewr)
            #print('Sidewr', k)
        k += 1

        if k%4==2 and boolRecbtr==False:
            EdgesRecbtr, MazeRecbtr, GridRecbtr,VisitedRecbtr,CheckedRecbtr,newVertex,k,boolRecbtr = maze_generating.mazeRecbtrparallel(gameDisplay, x3, y3, n, a,
                                                                                mazecol, delay,EdgesRecbtr, MazeRecbtr,GridRecbtr,VisitedRecbtr,CheckedRecbtr,
                                                                                newVertex, k, boolRecbtr)
            #print('Recbtr', k)
        k += 1

        if k%4==3 and boolPrim==False:
            EdgesPrim, MazePrim, GridPrim, VisitedPrim, CheckedPrim, NeighborsPrim, k, boolPrim = maze_generating.mazePrimparallel(
                gameDisplay, x4, y4, n, a,
                mazecol, delay, EdgesPrim, MazePrim, GridPrim, VisitedPrim, CheckedPrim,NeighborsPrim, k, boolPrim)
        k+=1
        startime = time.time()
        maze_functions.systemExit()

    pygame.time.delay(1000)
    endtime = time.time()
    runtime = endtime-starttime
    print('Parallel mazegen runtime: {0:.2f}s'.format(runtime))
    maze_functions.systemExit()

def SlideKruskal(n):
    starttime = time.time()
    a = maze_functions.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(colors.white)
    Grid = maze_functions.gridGen(n)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize/2)
    maze_functions.textDisplay(gameDisplay, x1, y1, 'Kruskal\'s algorithm', titleFontsize, colors.navy)

    x2= (scr[0] / 2 - n * a) / 2
    y2=titleFontsize+math.ceil((scr[1] - titleFontsize - n * a) / 2)
    maze_functions.drawGrid(gameDisplay,x2,y2,n,a,Grid,(colors.dgrey,maze_functions.lncol,colors.dgrey,colors.dgrey))
    maze_functions.drawGrid(gameDisplay,x2,y2,n,a,Grid,(colors.dgrey,maze_functions.lncol,colors.dgrey,colors.dgrey))
    pygame.display.update()

    textFontsize=35
    x3= scr[0] / 2 + 50
    y3=y2+(n*a-(titleFontsize*5/2+textFontsize))//2
    maze_functions.textDisplayleft(gameDisplay,x3,y3,"0. Start with a full of grid",textFontsize,colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3+titleFontsize/2, "1. Select a random wall", textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3+titleFontsize, "2. If the wall is between two distinct sets:", textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3+titleFontsize/2, y3+ titleFontsize * 3 / 2, "Remove the current wall", textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3+titleFontsize/2, y3+ titleFontsize * 2, "Merge the sets of the formerly divided cells", textFontsize,
                             colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3 , y3+titleFontsize*5/2, "3. Repeat until only one set remains", textFontsize,
                             colors.navy)
    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize = 20
    pygame.draw.line(gameDisplay, colors.navy, (x1, titleFontsize), (x1, y0 - tocFontsize), 5)
    maze_functions.mazeToc(gameDisplay, x0, y0, 0, tocFontsize, colors.lnavy, colors.navy)
    pygame.display.update()

    mazecol = (colors.dgrey, maze_functions.lncol, colors.lgreen, colors.salmon)
    maze_generating.mazeKruskal(gameDisplay,x2,y2,n,a,mazecol,delay,True)
    pygame.time.delay(2000)
    endtime = time.time()
    runtime = endtime-starttime
    print('Kruskal runtime: {0:.2f}s'.format(runtime))
    maze_functions.systemExit()

def SlideSidewinder(n):
    starttime = time.time()
    a = maze_functions.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(colors.white)
    Grid = maze_functions.gridGen(n)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize/2)
    maze_functions.textDisplay(gameDisplay, x1, y1, 'Sidewinder algorithm', titleFontsize, colors.navy)
    x2= (scr[0] / 2 - n * a) / 2
    y2=titleFontsize+math.ceil((scr[1] - titleFontsize - n * a) / 2)
    maze_functions.drawGrid(gameDisplay,x2,y2,n,a,Grid,(colors.dgrey,maze_functions.lncol,colors.dgrey,colors.dgrey))
    pygame.display.update()

    textFontsize = 30
    x3 = scr[0] / 2 + 50
    y3 = y2+(n*a-(titleFontsize*5/2+textFontsize))//2
    maze_functions.textDisplayleft(gameDisplay, x3, y3, "0. Start with a full of grid", textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize / 2, "1. Work through the grid row-wise", textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize, "2. Randomly decide to remove a wall on the right or not", textFontsize,
                             colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3 + titleFontsize / 2, y3 + titleFontsize * 3 / 2, "If not, merge the previously modified sets",
                             textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3 + titleFontsize / 2, y3 + titleFontsize * 2,
                             "Remove any of the walls above the merged cells", textFontsize,
                             colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize * 5/2, "3. Repeat until all rows have been processed",
                             textFontsize,
                             colors.navy)

    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize = 20
    pygame.draw.line(gameDisplay, colors.navy, (x1, titleFontsize), (x1, y0 - tocFontsize), 5)
    maze_functions.mazeToc(gameDisplay, x0, y0, 1, tocFontsize, colors.lnavy, colors.navy)
    pygame.display.update()
    pygame.time.delay(4000)

    mazecol = (colors.dgrey, maze_functions.lncol, colors.lgreen, colors.salmon)
    maze_generating.mazeSidewinder(gameDisplay, x2, y2, n, a, mazecol, delay, True)
    pygame.time.delay(2000)
    endtime = time.time()
    runtime = endtime-starttime
    print('Sidewinder runtime: {0:.2f}s'.format(runtime))
    maze_functions.systemExit()

def SlideRecbtr(n):
    starttime = time.time()
    a = maze_functions.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(colors.white)
    Grid = maze_functions.gridGen(n)
    mazecol = (colors.dgrey, maze_functions.lncol, colors.lgreen, colors.salmon)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize/2)
    maze_functions.textDisplay(gameDisplay, x1, y1, 'Recursive backtracker algorithm', titleFontsize, colors.navy)
    x2= (scr[0] / 2 - n * a) / 2
    y2=titleFontsize+math.ceil((scr[1] - titleFontsize - n * a) / 2)
    maze_functions.drawGrid(gameDisplay,x2,y2,n,a,Grid,(colors.dgrey,maze_functions.lncol,colors.dgrey,colors.dgrey))
    pygame.display.update()

    textFontsize = 35
    x3 = scr[0] / 2 + 50
    y3 = y2+(n*a-(titleFontsize*3+textFontsize))//2
    maze_functions.textDisplayleft(gameDisplay, x3, y3, "0. Start with a full of grid", textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize / 2, "1. Work through the grid row-wise:", textFontsize,
                             colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize, "2. Randomly select an unvisited cell from",
                             textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3 + titleFontsize // 4, y3 + titleFontsize * 5 / 4, "the adjacent cells of the last visited",textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3 + titleFontsize / 2, y3 + titleFontsize * 7 / 4, "Remove the wall between them",
                             textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3 + titleFontsize / 2, y3 + titleFontsize * 9/4,
                             "If there are no more adjacent cells,", textFontsize,
                             colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3 + titleFontsize / 2, y3 + titleFontsize * 5 / 2, "check the list backwards for adjacent cells ",
                             textFontsize,
                             colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize * 3, "3. Repeat until all rows have been processed",
                             textFontsize,
                             colors.navy)
    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize = 20
    pygame.draw.line(gameDisplay, colors.navy, (x1, titleFontsize), (x1, y0 - tocFontsize), 5)
    maze_functions.mazeToc(gameDisplay, x0, y0, 2, tocFontsize, colors.lnavy, colors.navy)

    pygame.display.update()
    pygame.time.delay(4000)

    maze_generating.mazeRecbtr(gameDisplay, x2, y2, n, a, mazecol, delay, True)
    pygame.time.delay(2000)
    endtime = time.time()
    runtime = endtime-starttime
    print('Recursive btr runtime: {0:.2f}s'.format(runtime))
    maze_functions.systemExit()

def SlidePrim(n):
    starttime = time.time()
    a = maze_functions.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(colors.white)
    Grid = maze_functions.gridGen(n)
    titleFontsize = 100
    mazecol = (colors.dgrey, maze_functions.lncol, colors.lgreen, colors.salmon)
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize/2)
    maze_functions.textDisplay(gameDisplay, x1, y1, 'Prim\'s algorithm', titleFontsize, colors.navy)
    x2= (scr[0] / 2 - n * a) / 2
    y2=titleFontsize+math.ceil((scr[1] - titleFontsize - n * a) / 2)
    maze_functions.drawGrid(gameDisplay, x2, y2, n, a, Grid, (colors.dgrey,maze_functions.lncol,colors.dgrey,colors.dgrey))
    pygame.display.update()

    textFontsize = 35
    x3 = scr[0] / 2 + 50
    y3 = y2 + (n * a - (titleFontsize * 11/4 + textFontsize)) // 2
    maze_functions.textDisplayleft(gameDisplay, x3, y3, "0. Start with a full of grid", textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize / 2, "1. Create a list of adjacent cells", textFontsize,
                             colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize, "2. Randomly select cell from the list", textFontsize,
                             colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3 + titleFontsize // 2, y3 + titleFontsize * 3 / 2, "Remove the wall between the selected",
                             textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3 + titleFontsize // 2, y3 + titleFontsize * 7 / 4, "and it’s adjacent cell",
                             textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3 + titleFontsize // 2, y3 + titleFontsize * 9/4,
                             "Add adjacent cells to the list",
                             textFontsize, colors.navy)

    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize * 11 / 4, "4. Repeat until all cells have been processed",
                             textFontsize,
                             colors.navy)
    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize = 20
    pygame.draw.line(gameDisplay, colors.navy, (x1, titleFontsize), (x1, y0 - tocFontsize), 5)
    maze_functions.mazeToc(gameDisplay, x0, y0, 3, tocFontsize, colors.lnavy, colors.navy)

    pygame.display.update()
    pygame.time.delay(4000)

    maze_generating.mazePrim(gameDisplay, x2, y2, n, a, mazecol, delay, True)
    pygame.time.delay(2000)
    endtime = time.time()
    runtime = endtime-starttime
    print('Prim runtime: %ds' %runtime)
    maze_functions.systemExit()

def SlideCover2(n):
    starttime = time.time()
    mazecol = (maze_functions.bgrcol, colors.dgrey, colors.llgreen, colors.lsalmon)
    fontsize = 100
    n = 2 * n
    x = (scr[0] - n * a) / 2
    y = (scr[1] - n * a) / 2
    x1 = scr[0] / 2
    y1 = scr[1] / 2 - math.floor(fontsize * 3 / 4)

    Grid, Maze = maze_generating.mazePrim(gameDisplay, x, y, n, a, mazecol, -1, False)
    gameDisplay.fill(colors.white)
    pygame.display.update()
    maze_functions.drawGrid2(gameDisplay, x, y, n, a, Grid, mazecol)
    maze_functions.textDisplay(gameDisplay, x1, y1 + math.floor(fontsize * 3 / 4), 'Maze solving algorithms', fontsize,
                         colors.navy)
    x3 = scr[0] - 150
    y3 = scr[1] - 50
    maze_functions.textDisplay(gameDisplay, x3, y3, 'develeped by Krisztian Dsupin', fontsize // 4, colors.navy)
    maze_functions.textDisplay(gameDisplay, x3, y3 + fontsize // 4, 'krisztian.dsupin@gmail.com', fontsize // 4,
                         colors.navy)

    #maze_functions.textDisplay(gameDisplay, x3, y3 + fontsize // 4, 'develeped by Krisztian Dsupin', fontsize // 4,
    #                     colors.navy)

    pygame.display.update()
    pygame.time.delay(2000)
    endtime = time.time()
    runtime = endtime - starttime
    print('Cover2 runtime: {0:.2f}s'.format(runtime))
    maze_functions.systemExit()

def SlideMazegen(n):
    starttime = time.time()
    a = maze_functions.rectSize(scr, n, marginsize, labelsize) * 1.6
    gameDisplay.fill(colors.white)
    titleFontsize = 100
    mazecol = (colors.dgrey, maze_functions.lncol, colors.lgreen, colors.salmon)

    x1 = scr[0] / 2
    y1 = labelsize/2
    maze_functions.textDisplay(gameDisplay, x1, y1 + math.floor(titleFontsize * 3 / 4), 'Maze solving algorithms', titleFontsize,
                         colors.navy)

    x2 = scr[0] / 2
    y2 = scr[1]-labelsize
    maze_functions.textDisplay(gameDisplay, x2, y2, 'Problem: find a path from S to F',
                         titleFontsize//2,
                         colors.navy)

    pygame.display.update()

    x3 = (scr[0] - n * a) / 2
    y3 = y1+titleFontsize+(scr[1]-(y1+titleFontsize+n*a+(scr[1]-y2)))//2
    Grid, Maze = maze_generating.mazeKruskal(gameDisplay, x3, y3, n, a, mazecol, 1, False)
    maze_functions.textDisplay2(gameDisplay,x3+a/2,y3+a/2,'S',25,colors.black,mazecol[2])
    maze_functions.textDisplay2(gameDisplay,x3+(n-1)*a+a/2,y3+(n-1)*a+a/2,'F',25,colors.black,mazecol[3])
    maze_solving.solveAstar(gameDisplay, x3, y3, Maze, Grid, n, a, -1, False)
    pygame.display.update()

    pygame.time.delay(1000)
    endtime = time.time()
    runtime = endtime - starttime
    print('Mazegen runtime: {0:.2f}s'.format(runtime))
    maze_functions.systemExit()
    return Grid,Maze

def SlideParallelsol(n,Grid,Maze):
    starttime = time.time()
    # logBool=False
    fontsize = 50
    gameDisplay.fill(colors.white)
    mazecol = (maze_functions.bgrcol, maze_functions.lncol, colors.lgreen, colors.salmon)
    pygame.draw.line(gameDisplay, colors.navy, (scr[0] / 2, 0), (scr[0] / 2, scr[1]), 2)
    pygame.draw.line(gameDisplay, colors.navy, (0, scr[1] / 2), (scr[0], scr[1] / 2), 2)

    maze_functions.drawGrid(gameDisplay, loc[0], loc[1], n, a, Grid,
                      (colors.white, colors.black, colors.lgreen, colors.salmon))
    maze_functions.textDisplay(gameDisplay, scr[0] / 4, labelsize / 2, 'Wallfollower algorithm', fontsize, colors.navy)

    maze_functions.drawGrid(gameDisplay, loc[0] + scr[0] / 2, loc[1], n, a, Grid,
                      (colors.white, colors.black, colors.lgreen, colors.salmon))
    maze_functions.textDisplay(gameDisplay, scr[0] * 3 / 4, labelsize / 2, 'A* algorithm', fontsize, colors.navy)

    maze_functions.drawGrid(gameDisplay, loc[0], loc[1] + scr[1] / 2, n, a, Grid,
                      (colors.white, colors.black, colors.lgreen, colors.salmon))
    maze_functions.textDisplay(gameDisplay, scr[0] / 4, scr[1] / 2 + labelsize / 2, 'Tremaux algorithm',
                         fontsize, colors.navy)

    maze_functions.drawGrid(gameDisplay, loc[0] + scr[0] / 2, loc[1] + scr[1] / 2, n, a, Grid,
                      (colors.white, colors.black, colors.lgreen, colors.salmon))
    maze_functions.textDisplay(gameDisplay, scr[0] * 3 / 4, scr[1] / 2 + labelsize / 2, 'Dead end filling algorithm', fontsize,
                         colors.navy)

    pygame.display.update()
    pygame.time.delay(500)

    delay = 10
    # Wall follower
    FinishedWallflw = [(0, -1)]; FinishedElementsWallflw = [0]; ShortestWallflw=[]
    boolWallfllw = False

    # A*
    CheckedAstar=[]; FinishedAstar = [(0, maze_functions.distance(0,n), -1)]; ShortestAstar=[]
    boolAstar = False

    #Tremaux
    FinishedTremaux = [];ShortestTremaux=[] ;DeadendTremaux = []; tempCheckedTremaux = [0]; currentTremaux=0
    boolTremaux=False

    #Dead End Filling
    DeadendDef, Branch = maze_functions.mazeDeadend(n, Maze)
    VisitedDef = []; endFillDef=[]; ShortestDef=[]
    boolDef=False

    k = 0
    x1 = loc[0]; y1 = loc[1]
    x2 = loc[0] + scr[0] / 2; y2 = loc[1]
    x3 = loc[0]; y3 = loc[1] + scr[1] / 2
    x4 = loc[0] + scr[0] / 2; y4 = loc[1] + scr[1] / 2
    while boolAstar == False or boolWallfllw==False or boolTremaux==False or boolDef==False:
        maze_functions.systemExit()
        if k % 4 == 0 and boolWallfllw == False:
            FinishedWallflw,FinishedelementsWallflw,ShortestWallflw,boolWallfllw=maze_solving.solveWallflwparallel(gameDisplay,x1,y1,Maze,Grid,n,a,delay,FinishedWallflw,FinishedElementsWallflw,
                                                                                               ShortestWallflw,boolWallfllw)
            #print('Wall flw', k)
        k += 1

        if k % 4 == 1 and boolAstar == False:
            CheckedAstar,FinishedAstar,ShortestAstar,boolAstar=maze_solving.solveAstarparallel(gameDisplay,x2,y2,Maze,Grid,n,a,delay,CheckedAstar,FinishedAstar,ShortestAstar,boolAstar)
            #print('A*', k)
        k += 1

        if k % 4 == 2 and boolTremaux == False:
            FinishedTremaux, ShortestTremaux, DeadendTremaux, currentTremaux, tempCheckedTremaux,boolTremaux=maze_solving.solveTremauxparrallel(
                gameDisplay,x3,y3,Maze,Grid,n,a,delay,FinishedTremaux,ShortestTremaux,DeadendTremaux,currentTremaux,tempCheckedTremaux,boolTremaux)
            #print('Tremaux', k)
        k += 1

        if k % 4 == 3 and boolDef == False:
            VisitedDef,ShortestDef ,DeadendDef, endFillDef, boolDef=maze_solving.solveDeadendparallel(gameDisplay,x4,y4,Maze,Grid,n,a,delay,VisitedDef,ShortestDef,DeadendDef,endFillDef,boolDef)
            #print('Def',k)
        k += 1
        maze_functions.systemExit()
        #print('---')

    pygame.time.delay(1000)
    endtime = time.time()
    runtime = endtime - starttime
    print('Parallel mazesol runtime: {0:.2f}s'.format(runtime))

def SlideWallfw(n,Grid,Maze):
    starttime = time.time()
    a = maze_functions.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(colors.white)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize / 2)
    maze_functions.textDisplay(gameDisplay, x1, y1, 'Wall follower algorithm', titleFontsize, colors.navy)
    x2 = (scr[0] / 2 - n * a) / 2
    y2 = titleFontsize + math.ceil((scr[1] - titleFontsize - n * a) / 2)
    maze_functions.drawGrid(gameDisplay, x2, y2, n, a, Grid, (colors.white, maze_functions.lncol, colors.lgreen, colors.salmon))
    pygame.display.update()

    textFontsize = 35
    x3 = scr[0] / 2 + 50
    y3 = y2 + (n * a - (titleFontsize *2 + textFontsize*7/4)) // 2
    maze_functions.textDisplayleft(gameDisplay, x3, y3, "# Also known as: left/right-hand rule", textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize / 2, "0. Select left or right as a direction",
                             textFontsize,
                             colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize, "1. Select the left/right cell of", textFontsize,
                             colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3+textFontsize*3/4, y3 + titleFontsize*5/4,
                             "previous one’s adjacent cells", textFontsize,
                             colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize * 7/4, "2. Repeat until target cell is processed", textFontsize,
                             colors.navy)
    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize=20
    pygame.draw.line(gameDisplay, colors.navy, (x1, titleFontsize), (x1, y0-tocFontsize), 5)
    maze_functions.mazeToc(gameDisplay, x0, y0, 4, tocFontsize, colors.lnavy, colors.navy)

    pygame.display.update()
    pygame.time.delay(4000)

    Shortest,Finished=maze_solving.solveWallflw(gameDisplay,x2,y2,Maze,Grid,n,a,delay//3,True)
    if statBool==True:
        x3=scr[0]//4
        y3=3*((scr[1]-n*a-titleFontsize)//4)+n*a+titleFontsize-tocFontsize
        percentage=math.floor(100*((len(Shortest)+len(Finished))/(n**2-2)))
        maze_functions.textDisplay(gameDisplay,x3,y3,'Percentage of visited cells: {0}%'.format(percentage),titleFontsize//2,colors.navy)
        pygame.display.update()
    pygame.time.delay(3000)
    endtime = time.time()
    runtime = endtime - starttime
    print('Wallfollower runtime: {0:.2f}s'.format(runtime))
    maze_functions.systemExit()

def SlideAstar(n,Grid,Maze):
    starttime = time.time()
    a = maze_functions.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(colors.white)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize / 2)
    maze_functions.textDisplay(gameDisplay, x1, y1, 'A* algorithm', titleFontsize, colors.navy)
    x2 = (scr[0] / 2 - n * a) / 2
    y2 = titleFontsize + math.ceil((scr[1] - titleFontsize - n * a) / 2)
    maze_functions.drawGrid(gameDisplay, x2, y2, n, a, Grid, (colors.white, maze_functions.lncol, colors.lgreen, colors.salmon))
    pygame.display.update()

    textFontsize = 35
    x3 = scr[0] / 2 + 50
    y3 = y2 + (n * a - (titleFontsize * 2 + textFontsize*2)) // 2
    maze_functions.textDisplayleft(gameDisplay, x3, y3, "0. Create a list of adjacent cells",
                             textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3+textFontsize*3/4, y3+ titleFontsize* 1/ 4,
                             "with it’s distance to the target cell",
                             textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize*3 / 4, "1. Select cell with the smallest distance",
                             textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize*5/4, "2. Add adjacent cells of previously selected",
                             textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3+textFontsize*3/4, y3 + titleFontsize*6/4,
                             "to the list",
                             textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize*2,
                             "3. Repeat until target cell is processed",
                             textFontsize, colors.navy)
    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize=20
    pygame.draw.line(gameDisplay, colors.navy, (x1, titleFontsize), (x1, y0-tocFontsize), 5)
    maze_functions.mazeToc(gameDisplay, x0, y0, 5, tocFontsize, colors.lnavy, colors.navy)

    pygame.display.update()
    pygame.time.delay(4000)

    Shortest, Finished = maze_solving.solveAstar(gameDisplay, x2, y2, Maze, Grid, n, a, delay//3, True)
    if statBool==True:
        x3=scr[0]//4
        y3=3*((scr[1]-n*a-titleFontsize)//4)+n*a+titleFontsize-tocFontsize
        percentage=math.floor(100*((len(Shortest)+len(Finished))/(n**2-2)))
        maze_functions.textDisplay(gameDisplay,x3,y3,'Percentage of visited cells: {0}%'.format(percentage),titleFontsize//2,colors.navy)
        pygame.display.update()

    pygame.time.delay(3000)
    endtime = time.time()
    runtime = endtime - starttime
    print('A* runtime: {0:.2f}s'.format(runtime))
    maze_functions.systemExit()

def SlideTremaux(n, Grid, Maze):
    starttime = time.time()
    a = maze_functions.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(colors.white)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize / 2)
    maze_functions.textDisplay(gameDisplay, x1, y1, 'Tremaux algorithm', titleFontsize, colors.navy)
    x2 = (scr[0] / 2 - n * a) / 2
    y2 = titleFontsize + math.ceil((scr[1] - titleFontsize - n * a) / 2)
    maze_functions.drawGrid(gameDisplay, x2, y2, n, a, Grid,
                      (colors.white, maze_functions.lncol, colors.lgreen, colors.salmon))
    pygame.display.update()

    textFontsize = 35
    x3 = scr[0] / 2 + 50
    y3 = y2 + (n * a - (titleFontsize * 2 + textFontsize*9/4)) // 2
    maze_functions.textDisplayleft(gameDisplay, x3, y3, "0. Mark each path once, when you follow it.", textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize / 2, "1. Never enter a path which has two marks on it.",
                             textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize, "2. Choose randomly an unmarked path",
                             textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3 + textFontsize, y3 + titleFontsize*3/2,
                             "If the path has a mark, turn around",
                             textFontsize, colors.navy)

    maze_functions.textDisplayleft(gameDisplay, x3 + textFontsize, y3 + titleFontsize * 7 / 4,
                             "and return along that path",
                             textFontsize, colors.navy)

    maze_functions.textDisplayleft(gameDisplay, x3+ textFontsize, y3 + titleFontsize*9/4,
                             "If not, choose randomly",
                             textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3 + textFontsize, y3 + titleFontsize * 10 / 4,
                             "one of the remaining paths.",
                             textFontsize, colors.navy)


    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize*3,
                             "3. Repeat until target cell is processed.",
                             textFontsize, colors.navy)
    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize = 20
    pygame.draw.line(gameDisplay, colors.navy, (x1, titleFontsize), (x1, y0 - tocFontsize), 5)
    maze_functions.mazeToc(gameDisplay, x0, y0, 6, tocFontsize, colors.lnavy, colors.navy)

    maze_functions.updelay(4000)
    Shortest, Finished = maze_solving.solveTremaux(gameDisplay, x2, y2, Maze, Grid, n, a, delay//3, True)
    if statBool == True:
        x3 = scr[0] // 4
        y3 = 3 * ((scr[1] - n * a - titleFontsize) // 4) + n * a + titleFontsize-tocFontsize
        percentage = math.floor(100 * ((len(Finished)) / (n ** 2 - 2)))
        maze_functions.textDisplay(gameDisplay, x3, y3, 'Percentage of visited cells: {0}%'.format(percentage),
                             titleFontsize // 2, colors.navy)
        pygame.display.update()
    pygame.time.delay(3000)
    endtime = time.time()
    runtime = endtime - starttime
    print('Tremaux runtime: {0:.2f}s'.format(runtime))
    maze_functions.systemExit()

def SlideDeadend(n, Grid, Maze):
    starttime = time.time()
    a = maze_functions.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(colors.white)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize / 2)
    maze_functions.textDisplay(gameDisplay, x1, y1, 'Dead end filling algorithm', titleFontsize, colors.navy)
    x2 = (scr[0] / 2 - n * a) / 2
    y2 = titleFontsize + math.ceil((scr[1] - titleFontsize - n * a) / 2)
    maze_functions.drawGrid(gameDisplay, x2, y2, n, a, Grid,
                      (colors.white, maze_functions.lncol, colors.lgreen, colors.salmon))
    pygame.display.update()

    textFontsize = 35
    x3 = scr[0] / 2 + 50
    y3 = y2 + (n * a - (titleFontsize * 2 + textFontsize*6/4)) // 2
    maze_functions.textDisplayleft(gameDisplay, x3, y3, "0. Find all dead-ends in the maze", textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize / 2, "1. Fill the path from each",
                             textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3+textFontsize*3/4, y3 + titleFontsize* 3/ 4, "dead-end until a junction",
                             textFontsize, colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3, y3 + titleFontsize*5/4, "2. Unvisited cells are the path", textFontsize,
                             colors.navy)
    maze_functions.textDisplayleft(gameDisplay, x3+textFontsize*3/4, y3 + titleFontsize * 6 / 4,
                             "to the target", textFontsize,
                             colors.navy)

    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize = 20
    pygame.draw.line(gameDisplay, colors.navy, (x1, titleFontsize), (x1, y0 - tocFontsize), 5)
    maze_functions.mazeToc(gameDisplay, x0, y0, 7, tocFontsize, colors.lnavy, colors.navy)
    pygame.display.update()
    pygame.time.delay(4000)

    Shortest, Finished = maze_solving.solveDeadend(gameDisplay, x2, y2, Maze, Grid, n, a, delay//3, True)
    if statBool == True:
        x3 = scr[0] // 4
        y3 = 3 * ((scr[1] - n * a - titleFontsize) // 4) + n * a + titleFontsize-tocFontsize
        percentage = math.floor(100 * ((len(Shortest) + len(Finished)) / (n ** 2 - 2)))
        maze_functions.textDisplay(gameDisplay, x3, y3, 'Percentage of visited cells: {0}%'.format(percentage),
                             titleFontsize // 2, colors.navy)
        pygame.display.update()

    pygame.time.delay(3000)
    endtime = time.time()
    runtime = endtime - starttime
    print('Deadend runtime: {0:.2f}s'.format(runtime))
    maze_functions.systemExit()

def SlideHexagonal(n):
    starttime = time.time()
    a = maze_functions.hexSize(scr, n, marginsize, labelsize) * 1.8
    gameDisplay.fill(colors.white)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize / 2)
    maze_functions.textDisplay(gameDisplay, x1, y1, 'Hexagonal mazes', titleFontsize, colors.navy)
    x2 = scr[0] / 2
    y2 = titleFontsize + 75
    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize = 20
    maze_functions.mazeToc(gameDisplay, x0, y0, 8, tocFontsize, colors.lnavy, colors.navy)

    Grid,Maze,Hexagonal=maze_generating.mazeKruskalhex(gameDisplay,x2,y2,n,a,
            (colors.dgrey,colors.black,colors.lgreen, colors.salmon),delay//10, False)
    pygame.time.delay(1000)
    maze_solving.solveAstarhex(gameDisplay,x2,y2,Maze,Grid,Hexagonal,n,a,delay//5,False)
    endtime = time.time()
    runtime = endtime - starttime
    print('Hexagonal runtime: {0:.2f}s'.format(runtime))
    maze_functions.systemExit()

def SlideKruskal_rectengular(n, m, id):
    starttime = time.time()
    a = maze_settings.a // 2
    gameDisplay.fill(colors.white)
    Grid = maze_functions.gridGen_rectengular(n, m)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize/2)
    maze_functions.textDisplay(gameDisplay, x1, y1, 'Kruskal\'s algorithm', titleFontsize, colors.navy)

    x2= (scr[0] / 2 - n * a) / 2
    y2=titleFontsize+math.ceil((scr[1] - titleFontsize - n * a) / 2)
    maze_functions.drawGrid_rectengular(gameDisplay,x2,y2,n,m,a,Grid,(colors.dgrey,maze_functions.lncol,colors.dgrey,colors.dgrey))
    pygame.display.update()


    mazecol = (colors.dgrey, maze_functions.lncol, colors.lgreen, colors.salmon)
    maze_generating.mazeKruskal_rectengular(gameDisplay,x2,y2,n,m,a,mazecol,delay,False, id)
    pygame.time.delay(1000)
    endtime = time.time()
    runtime = endtime-starttime
    print('Kruskal runtime: {0:.2f}s'.format(runtime))
    maze_functions.systemExit()