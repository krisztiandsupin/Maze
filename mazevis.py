#maze visualize
import pygame, openpyxl, math, time
import mazefunc, mazealg, solvealg

#size,location
scr=(1280, 924)
n=20
#scr=(1540,778)
labelsize=75
marginsize=15
a=mazefunc.rectSize(scr, n, marginsize, labelsize)                #size of edge of rectengular
loc=((scr[0] / 2 - n * a) / 2, labelsize)
line_thickness=1   #line
gameDisplay = pygame.display.set_mode(scr)
Grid=mazefunc.gridGen(n)
delay=250
statBool=True

def SlideCover(n):
    starttime = time.time()
    gameDisplay.fill(mazefunc.white)
    mazecol=(mazefunc.bgrcol,mazefunc.dgrey,mazefunc.llgreen,mazefunc.lsalmon)
    n = 2 * n
    x = (scr[0] - n * a) / 2
    y = (scr[1] - n * a) / 2
    Grid, Maze = mazealg.mazePrim(gameDisplay, x, y, n, a, mazecol, -1,False)

    fontsize = 100
    mazefunc.drawGrid2(gameDisplay, x, y, n, a, Grid, mazecol)
    x1= scr[0] / 2
    y1= scr[1] / 2 - math.floor(fontsize * 3 / 4)
    y2= scr[1] / 2 + math.floor(fontsize * 3 / 4)

    mazefunc.textDisplay(gameDisplay, x1,y1,'Maze',  math.floor(fontsize*3/2), mazefunc.navy)
    mazefunc.textDisplay(gameDisplay, x1, y2,'Creation & solving algorithms',  fontsize, mazefunc.navy)
    pygame.display.update()

    x3= scr[0] - 150
    y3= scr[1] - 50
    mazefunc.textDisplay(gameDisplay, x3, y3, 'develeped by Krisztian Dsupin', fontsize//4, mazefunc.navy)
    mazefunc.textDisplay(gameDisplay, x3, y3+fontsize//4, 'krisztian.dsupin@gmail.com', fontsize // 4, mazefunc.navy)
    pygame.display.update()
    pygame.time.delay(2000)

    gameDisplay.fill(mazefunc.white)
    pygame.display.update()
    mazefunc.drawGrid2(gameDisplay,x,y,n,a,Grid,mazecol)
    mazefunc.textDisplay(gameDisplay, x1, y1+math.floor(fontsize*3/4), 'Maze creation algorithms', fontsize, mazefunc.navy)
    mazefunc.textDisplay(gameDisplay, x3, y3, 'develeped by Krisztian Dsupin', fontsize // 4, mazefunc.navy)
    mazefunc.textDisplay(gameDisplay, x3, y3 + fontsize // 4, 'krisztian.dsupin@gmail.com', fontsize // 4,
                         mazefunc.navy)
    pygame.display.update()
    pygame.time.delay(2000)
    endtime=time.time()
    runtime=endtime-starttime
    print('Cover runtime: {0:.2f}s'.format(runtime))
    mazefunc.systemExit()

def SlideParallelgen(n):
    starttime = time.time()
    #logBool=False
    fontsize=50
    Edges, Maze, Grid = mazefunc.mazeCreate(n)
    gameDisplay.fill(mazefunc.white)
    mazecol=(mazefunc.bgrcol,mazefunc.lncol,mazefunc.lgreen,mazefunc.salmon)
    pygame.draw.line(gameDisplay, mazefunc.navy, (scr[0] / 2, 0), (scr[0] / 2, scr[1]), 2)
    pygame.draw.line(gameDisplay, mazefunc.navy, (0, scr[1] / 2), (scr[0], scr[1] / 2), 2)

    mazefunc.drawGrid(gameDisplay, loc[0], loc[1], n, a, Grid, (mazefunc.dgrey,mazefunc.black,mazefunc.dgrey,mazefunc.dgrey))
    mazefunc.textDisplay(gameDisplay, scr[0] / 4, labelsize / 2, 'Kruskal\'s algorithm', fontsize, mazefunc.navy)

    mazefunc.drawGrid(gameDisplay, loc[0] + scr[0] / 2, loc[1], n, a, Grid, (mazefunc.dgrey,mazefunc.black,mazefunc.dgrey,mazefunc.dgrey))
    mazefunc.textDisplay(gameDisplay, scr[0] * 3 / 4, labelsize / 2, 'Sidewinder algorithm', fontsize, mazefunc.navy)

    mazefunc.drawGrid(gameDisplay, loc[0], loc[1] + scr[1] / 2, n, a, Grid, (mazefunc.dgrey,mazefunc.black,mazefunc.dgrey,mazefunc.dgrey))
    mazefunc.textDisplay(gameDisplay, scr[0] / 4, scr[1] / 2 + labelsize / 2, 'Recursive backtracker algorithm',
                         fontsize, mazefunc.navy)

    mazefunc.drawGrid(gameDisplay, loc[0] + scr[0] / 2, loc[1] + scr[1] / 2, n, a, Grid, (mazefunc.dgrey,mazefunc.black,mazefunc.dgrey,mazefunc.dgrey))
    mazefunc.textDisplay(gameDisplay, scr[0] * 3 / 4, scr[1] / 2 + labelsize / 2, 'Prim\'s algorithm', fontsize,
                         mazefunc.navy)

    pygame.display.update()
    pygame.time.delay(500)

    # maze log
    delay = 10
    #Kruskal
    EdgesKruskal, MazeKruskal, GridKruskal = mazefunc.mazeCreate(n); RegionsKruskal=mazefunc.regionGen(n)
    VisitedKruskal=[False for i in range(0,n**2)]
    boolKruskal=False
    #Sidewinder
    EdgesSidewr, MazeSidewr, GridSidewr = mazefunc.mazeCreate(n);
    VisitedSidewr=[False for i in range(0,n**2)]; tempList=[]; rowList=[]
    boolSidewr=False
    #Recursive backtracker
    EdgesRecbtr, MazeRecbtr, GridRecbtr= mazefunc.mazeCreate(n); CheckedRecbtr=[0]; newVertex=0
    VisitedRecbtr = [False for i in range(0, n ** 2)]
    boolRecbtr=False
    #Prim
    EdgesPrim, MazePrim, GridPrim = mazefunc.mazeCreate(n);
    VisitedPrim = [False for i in range(0, n ** 2)]; CheckedPrim=[0]; NeighborsPrim=mazefunc.regionNeighbor(n,CheckedPrim[-1])
    boolPrim = False

    k=0
    x1=loc[0]; y1=loc[1]
    x2=loc[0]+scr[0]/2; y2=loc[1]
    x3=loc[0]; y3= loc[1] + scr[1] / 2
    x4=loc[0]+scr[0]/2; y4=loc[1]+scr[1] / 2
    while boolKruskal==False or boolRecbtr==False or boolSidewr==False or boolPrim==False:
        if k%4==0 and boolKruskal==False:
            EdgesKruskal, MazeKruskal, GridKruskal, VisitedKruskal,RegionsKruskal,k, boolKruskal = mazealg.mazeKruskalparallel(gameDisplay,x1,y1,n,a,mazecol,delay,
                                                                         EdgesKruskal,MazeKruskal,GridKruskal,VisitedKruskal,RegionsKruskal, k,boolKruskal)
            #print('Kruskal', k)
        k += 1

        if k%4==1 and boolSidewr==False:
            EdgesSidewr, MazeSidewr, GridSidewr,rowList,tempList,VisitedSidewr,k, boolSidewr = mazealg.mazeSidewrparallel(
                gameDisplay, x2, y2, n, a, mazecol, delay,
                EdgesSidewr, MazeSidewr, GridSidewr,tempList,rowList, VisitedSidewr, k, boolSidewr)
            #print('Sidewr', k)
        k += 1

        if k%4==2 and boolRecbtr==False:
            EdgesRecbtr, MazeRecbtr, GridRecbtr,VisitedRecbtr,CheckedRecbtr,newVertex,k,boolRecbtr = mazealg.mazeRecbtrparallel(gameDisplay, x3, y3, n, a,
                                                                                mazecol, delay,EdgesRecbtr, MazeRecbtr,GridRecbtr,VisitedRecbtr,CheckedRecbtr,
                                                                                newVertex, k, boolRecbtr)
            #print('Recbtr', k)
        k += 1

        if k%4==3 and boolPrim==False:
            EdgesPrim, MazePrim, GridPrim, VisitedPrim, CheckedPrim, NeighborsPrim, k, boolPrim = mazealg.mazePrimparallel(
                gameDisplay, x4, y4, n, a,
                mazecol, delay, EdgesPrim, MazePrim, GridPrim, VisitedPrim, CheckedPrim,NeighborsPrim, k, boolPrim)
        k+=1
        startime = time.time()
        mazefunc.systemExit()

    '''grid1, maze1 = mazealg.mazeKruskal(gameDisplay, loc[0], loc[1], n, a, mazecol, delay,False)
    grid2, maze2 = mazealg.mazeSidewinder(gameDisplay, loc[0] + screen[0] / 2, loc[1], n, a, mazecol, delay,False)
    grid3, maze3 = mazealg.mazeRecbtr(gameDisplay, loc[0], loc[1] + screen[1] / 2, n, a, mazecol, delay,False)
    grid4, maze4 = mazealg.mazePrim(gameDisplay, loc[0] + screen[0] / 2, loc[1] + screen[1] / 2, n, a, mazecol, delay,False)'''

    '''if logBool==True:
        if n >= 10 and n <= 50 and n % 5 == 0:
            book = openpyxl.load_workbook('mazes\size{0}\size{1}log.xlsx'.format(n, n))
            sheet = book.active
            id = int(sheet.cell(2, 2).value)
            mazefunc.mazeLog(n, id, "Kruskal")
            mazefunc.mazePic(n, grid1,mazecol, "maze{0}_{1}".format(n, id))
            id += 1
            mazefunc.mazeLog(n, id, "Sidewinder")
            mazefunc.mazePic(n, grid2,mazecol, "maze{0}_{1}".format(n, id))
            id += 1
            mazefunc.mazeLog(n, id, "Recursive backtracker")
            mazefunc.mazePic(n, grid3,mazecol, "maze{0}_{1}".format(n, id))
            id += 1
            mazefunc.mazeLog(n, id, "Prim")
            mazefunc.mazePic(n, grid4,mazecol, "maze{0}_{1}".format(n, id))'''
    pygame.time.delay(1000)
    endtime = time.time()
    runtime = endtime-starttime
    print('Parallel mazegen runtime: {0:.2f}s'.format(runtime))
    mazefunc.systemExit()

def SlideKruskal(n):
    starttime = time.time()
    a = mazefunc.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(mazefunc.white)
    Grid = mazefunc.gridGen(n)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize/2)
    mazefunc.textDisplay(gameDisplay, x1, y1, 'Kruskal\'s algorithm', titleFontsize, mazefunc.navy)

    x2= (scr[0] / 2 - n * a) / 2
    y2=titleFontsize+math.ceil((scr[1] - titleFontsize - n * a) / 2)
    mazefunc.drawGrid(gameDisplay,x2,y2,n,a,Grid,(mazefunc.dgrey,mazefunc.lncol,mazefunc.dgrey,mazefunc.dgrey))
    pygame.display.update()

    textFontsize=35
    x3= scr[0] / 2 + 50
    y3=y2+(n*a-(titleFontsize*5/2+textFontsize))//2
    mazefunc.textDisplayleft(gameDisplay,x3,y3,"0. Start with a full of grid",textFontsize,mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3+titleFontsize/2, "1. Select a random wall", textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3+titleFontsize, "2. If the wall is between two distinct sets:", textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3+titleFontsize/2, y3+ titleFontsize * 3 / 2, "Remove the current wall", textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3+titleFontsize/2, y3+ titleFontsize * 2, "Merge the sets of the formerly divided cells", textFontsize,
                             mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3 , y3+titleFontsize*5/2, "3. Repeat until only one set remains", textFontsize,
                             mazefunc.navy)
    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize = 20
    pygame.draw.line(gameDisplay, mazefunc.navy, (x1, titleFontsize), (x1, y0 - tocFontsize), 5)
    mazefunc.mazeToc(gameDisplay, x0, y0, 0, tocFontsize, mazefunc.lnavy, mazefunc.navy)
    pygame.display.update()

    mazecol = (mazefunc.dgrey, mazefunc.lncol, mazefunc.lgreen, mazefunc.salmon)
    mazealg.mazeKruskal(gameDisplay,x2,y2,n,a,mazecol,delay,True)
    pygame.time.delay(2000)
    endtime = time.time()
    runtime = endtime-starttime
    print('Kruskal runtime: {0:.2f}s'.format(runtime))
    mazefunc.systemExit()

def SlideSidewinder(n):
    starttime = time.time()
    a = mazefunc.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(mazefunc.white)
    Grid = mazefunc.gridGen(n)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize/2)
    mazefunc.textDisplay(gameDisplay, x1, y1, 'Sidewinder algorithm', titleFontsize, mazefunc.navy)
    x2= (scr[0] / 2 - n * a) / 2
    y2=titleFontsize+math.ceil((scr[1] - titleFontsize - n * a) / 2)
    mazefunc.drawGrid(gameDisplay,x2,y2,n,a,Grid,(mazefunc.dgrey,mazefunc.lncol,mazefunc.dgrey,mazefunc.dgrey))
    pygame.display.update()

    textFontsize = 30
    x3 = scr[0] / 2 + 50
    y3 = y2+(n*a-(titleFontsize*5/2+textFontsize))//2
    mazefunc.textDisplayleft(gameDisplay, x3, y3, "0. Start with a full of grid", textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize / 2, "1. Work through the grid row-wise", textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize, "2. Randomly decide to remove a wall on the right or not", textFontsize,
                             mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3 + titleFontsize / 2, y3 + titleFontsize * 3 / 2, "If not, merge the previously modified sets",
                             textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3 + titleFontsize / 2, y3 + titleFontsize * 2,
                             "Remove any of the walls above the merged cells", textFontsize,
                             mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize * 5/2, "3. Repeat until all rows have been processed",
                             textFontsize,
                             mazefunc.navy)

    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize = 20
    pygame.draw.line(gameDisplay, mazefunc.navy, (x1, titleFontsize), (x1, y0 - tocFontsize), 5)
    mazefunc.mazeToc(gameDisplay, x0, y0, 1, tocFontsize, mazefunc.lnavy, mazefunc.navy)
    pygame.display.update()
    pygame.time.delay(4000)

    mazecol = (mazefunc.dgrey, mazefunc.lncol, mazefunc.lgreen, mazefunc.salmon)
    mazealg.mazeSidewinder(gameDisplay, x2, y2, n, a, mazecol, delay, True)
    pygame.time.delay(2000)
    endtime = time.time()
    runtime = endtime-starttime
    print('Sidewinder runtime: {0:.2f}s'.format(runtime))
    mazefunc.systemExit()

def SlideRecbtr(n):
    starttime = time.time()
    a = mazefunc.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(mazefunc.white)
    Grid = mazefunc.gridGen(n)
    mazecol = (mazefunc.dgrey, mazefunc.lncol, mazefunc.lgreen, mazefunc.salmon)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize/2)
    mazefunc.textDisplay(gameDisplay, x1, y1, 'Recursive backtracker algorithm', titleFontsize, mazefunc.navy)
    x2= (scr[0] / 2 - n * a) / 2
    y2=titleFontsize+math.ceil((scr[1] - titleFontsize - n * a) / 2)
    mazefunc.drawGrid(gameDisplay,x2,y2,n,a,Grid,(mazefunc.dgrey,mazefunc.lncol,mazefunc.dgrey,mazefunc.dgrey))
    pygame.display.update()

    textFontsize = 35
    x3 = scr[0] / 2 + 50
    y3 = y2+(n*a-(titleFontsize*3+textFontsize))//2
    mazefunc.textDisplayleft(gameDisplay, x3, y3, "0. Start with a full of grid", textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize / 2, "1. Work through the grid row-wise:", textFontsize,
                             mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize, "2. Randomly select an unvisited cell from",
                             textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3 + titleFontsize // 4, y3 + titleFontsize * 5 / 4, "the adjacent cells of the last visited",textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3 + titleFontsize / 2, y3 + titleFontsize * 7 / 4, "Remove the wall between them",
                             textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3 + titleFontsize / 2, y3 + titleFontsize * 9/4,
                             "If there are no more adjacent cells,", textFontsize,
                             mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3 + titleFontsize / 2, y3 + titleFontsize * 5 / 2, "check the list backwards for adjacent cells ",
                             textFontsize,
                             mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize * 3, "3. Repeat until all rows have been processed",
                             textFontsize,
                             mazefunc.navy)
    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize = 20
    pygame.draw.line(gameDisplay, mazefunc.navy, (x1, titleFontsize), (x1, y0 - tocFontsize), 5)
    mazefunc.mazeToc(gameDisplay, x0, y0, 2, tocFontsize, mazefunc.lnavy, mazefunc.navy)

    pygame.display.update()
    pygame.time.delay(4000)

    mazealg.mazeRecbtr(gameDisplay, x2, y2, n, a, mazecol, delay, True)
    pygame.time.delay(2000)
    endtime = time.time()
    runtime = endtime-starttime
    print('Recursive btr runtime: {0:.2f}s'.format(runtime))
    mazefunc.systemExit()

def SlidePrim(n):
    starttime = time.time()
    a = mazefunc.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(mazefunc.white)
    Grid = mazefunc.gridGen(n)
    titleFontsize = 100
    mazecol = (mazefunc.dgrey, mazefunc.lncol, mazefunc.lgreen, mazefunc.salmon)
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize/2)
    mazefunc.textDisplay(gameDisplay, x1, y1, 'Prim\'s algorithm', titleFontsize, mazefunc.navy)
    x2= (scr[0] / 2 - n * a) / 2
    y2=titleFontsize+math.ceil((scr[1] - titleFontsize - n * a) / 2)
    mazefunc.drawGrid(gameDisplay, x2, y2, n, a, Grid, (mazefunc.dgrey,mazefunc.lncol,mazefunc.dgrey,mazefunc.dgrey))
    pygame.display.update()

    textFontsize = 35
    x3 = scr[0] / 2 + 50
    y3 = y2 + (n * a - (titleFontsize * 11/4 + textFontsize)) // 2
    mazefunc.textDisplayleft(gameDisplay, x3, y3, "0. Start with a full of grid", textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize / 2, "1. Create a list of adjacent cells", textFontsize,
                             mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize, "2. Randomly select cell from the list", textFontsize,
                             mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3 + titleFontsize // 2, y3 + titleFontsize * 3 / 2, "Remove the wall between the selected",
                             textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3 + titleFontsize // 2, y3 + titleFontsize * 7 / 4, "and it’s adjacent cell",
                             textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3 + titleFontsize // 2, y3 + titleFontsize * 9/4,
                             "Add adjacent cells to the list",
                             textFontsize, mazefunc.navy)

    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize * 11 / 4, "4. Repeat until all cells have been processed",
                             textFontsize,
                             mazefunc.navy)
    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize = 20
    pygame.draw.line(gameDisplay, mazefunc.navy, (x1, titleFontsize), (x1, y0 - tocFontsize), 5)
    mazefunc.mazeToc(gameDisplay, x0, y0, 3, tocFontsize, mazefunc.lnavy, mazefunc.navy)

    pygame.display.update()
    pygame.time.delay(4000)

    mazealg.mazePrim(gameDisplay, x2, y2, n, a, mazecol, delay, True)
    pygame.time.delay(2000)
    endtime = time.time()
    runtime = endtime-starttime
    print('Prim runtime: %ds' %runtime)
    mazefunc.systemExit()

def SlideCover2(n):
    starttime = time.time()
    mazecol = (mazefunc.bgrcol, mazefunc.dgrey, mazefunc.llgreen, mazefunc.lsalmon)
    fontsize = 100
    n = 2 * n
    x = (scr[0] - n * a) / 2
    y = (scr[1] - n * a) / 2
    x1 = scr[0] / 2
    y1 = scr[1] / 2 - math.floor(fontsize * 3 / 4)

    Grid, Maze = mazealg.mazePrim(gameDisplay, x, y, n, a, mazecol, -1, False)
    gameDisplay.fill(mazefunc.white)
    pygame.display.update()
    mazefunc.drawGrid2(gameDisplay, x, y, n, a, Grid, mazecol)
    mazefunc.textDisplay(gameDisplay, x1, y1 + math.floor(fontsize * 3 / 4), 'Maze solving algorithms', fontsize,
                         mazefunc.navy)
    x3 = scr[0] - 150
    y3 = scr[1] - 50
    mazefunc.textDisplay(gameDisplay, x3, y3, 'develeped by Krisztian Dsupin', fontsize // 4, mazefunc.navy)
    mazefunc.textDisplay(gameDisplay, x3, y3 + fontsize // 4, 'krisztian.dsupin@gmail.com', fontsize // 4,
                         mazefunc.navy)

    #mazefunc.textDisplay(gameDisplay, x3, y3 + fontsize // 4, 'develeped by Krisztian Dsupin', fontsize // 4,
    #                     mazefunc.navy)

    pygame.display.update()
    pygame.time.delay(2000)
    endtime = time.time()
    runtime = endtime - starttime
    print('Cover2 runtime: {0:.2f}s'.format(runtime))
    mazefunc.systemExit()

def SlideMazegen(n):
    starttime = time.time()
    a = mazefunc.rectSize(scr, n, marginsize, labelsize) * 1.6
    gameDisplay.fill(mazefunc.white)
    titleFontsize = 100
    mazecol = (mazefunc.dgrey, mazefunc.lncol, mazefunc.lgreen, mazefunc.salmon)

    x1 = scr[0] / 2
    y1 = labelsize/2
    mazefunc.textDisplay(gameDisplay, x1, y1 + math.floor(titleFontsize * 3 / 4), 'Maze solving algorithms', titleFontsize,
                         mazefunc.navy)

    x2 = scr[0] / 2
    y2 = scr[1]-labelsize
    mazefunc.textDisplay(gameDisplay, x2, y2, 'Problem: find a path from S to F',
                         titleFontsize//2,
                         mazefunc.navy)

    pygame.display.update()

    x3 = (scr[0] - n * a) / 2
    y3 = y1+titleFontsize+(scr[1]-(y1+titleFontsize+n*a+(scr[1]-y2)))//2
    Grid, Maze = mazealg.mazeKruskal(gameDisplay, x3, y3, n, a, mazecol, 1, False)
    mazefunc.textDisplay2(gameDisplay,x3+a/2,y3+a/2,'S',25,mazefunc.black,mazecol[2])
    mazefunc.textDisplay2(gameDisplay,x3+(n-1)*a+a/2,y3+(n-1)*a+a/2,'F',25,mazefunc.black,mazecol[3])
    solvealg.solveAstar(gameDisplay, x3, y3, Maze, Grid, n, a, -1, False)
    pygame.display.update()

    pygame.time.delay(1000)
    endtime = time.time()
    runtime = endtime - starttime
    print('Mazegen runtime: {0:.2f}s'.format(runtime))
    mazefunc.systemExit()
    return Grid,Maze

def SlideParallelsol(n,Grid,Maze):
    starttime = time.time()
    # logBool=False
    fontsize = 50
    gameDisplay.fill(mazefunc.white)
    mazecol = (mazefunc.bgrcol, mazefunc.lncol, mazefunc.lgreen, mazefunc.salmon)
    pygame.draw.line(gameDisplay, mazefunc.navy, (scr[0] / 2, 0), (scr[0] / 2, scr[1]), 2)
    pygame.draw.line(gameDisplay, mazefunc.navy, (0, scr[1] / 2), (scr[0], scr[1] / 2), 2)

    mazefunc.drawGrid(gameDisplay, loc[0], loc[1], n, a, Grid,
                      (mazefunc.white, mazefunc.black, mazefunc.lgreen, mazefunc.salmon))
    mazefunc.textDisplay(gameDisplay, scr[0] / 4, labelsize / 2, 'Wallfollower algorithm', fontsize, mazefunc.navy)

    mazefunc.drawGrid(gameDisplay, loc[0] + scr[0] / 2, loc[1], n, a, Grid,
                      (mazefunc.white, mazefunc.black, mazefunc.lgreen, mazefunc.salmon))
    mazefunc.textDisplay(gameDisplay, scr[0] * 3 / 4, labelsize / 2, 'A* algorithm', fontsize, mazefunc.navy)

    mazefunc.drawGrid(gameDisplay, loc[0], loc[1] + scr[1] / 2, n, a, Grid,
                      (mazefunc.white, mazefunc.black, mazefunc.lgreen, mazefunc.salmon))
    mazefunc.textDisplay(gameDisplay, scr[0] / 4, scr[1] / 2 + labelsize / 2, 'Tremaux algorithm',
                         fontsize, mazefunc.navy)

    mazefunc.drawGrid(gameDisplay, loc[0] + scr[0] / 2, loc[1] + scr[1] / 2, n, a, Grid,
                      (mazefunc.white, mazefunc.black, mazefunc.lgreen, mazefunc.salmon))
    mazefunc.textDisplay(gameDisplay, scr[0] * 3 / 4, scr[1] / 2 + labelsize / 2, 'Dead end filling algorithm', fontsize,
                         mazefunc.navy)

    pygame.display.update()
    pygame.time.delay(500)

    delay = 10
    # Wall follower
    FinishedWallflw = [(0, -1)]; FinishedElementsWallflw = [0]; ShortestWallflw=[]
    boolWallfllw = False

    # A*
    CheckedAstar=[]; FinishedAstar = [(0, mazefunc.distance(0,n), -1)]; ShortestAstar=[]
    boolAstar = False

    #Tremaux
    FinishedTremaux = [];ShortestTremaux=[] ;DeadendTremaux = []; tempCheckedTremaux = [0]; currentTremaux=0
    boolTremaux=False

    #Dead End Filling
    DeadendDef, Branch = mazefunc.mazeDeadend(n, Maze)
    VisitedDef = []; endFillDef=[]; ShortestDef=[]
    boolDef=False

    k = 0
    x1 = loc[0]; y1 = loc[1]
    x2 = loc[0] + scr[0] / 2; y2 = loc[1]
    x3 = loc[0]; y3 = loc[1] + scr[1] / 2
    x4 = loc[0] + scr[0] / 2; y4 = loc[1] + scr[1] / 2
    while boolAstar == False or boolWallfllw==False or boolTremaux==False or boolDef==False:
        mazefunc.systemExit()
        if k % 4 == 0 and boolWallfllw == False:
            FinishedWallflw,FinishedelementsWallflw,ShortestWallflw,boolWallfllw=solvealg.solveWallflwparallel(gameDisplay,x1,y1,Maze,Grid,n,a,delay,FinishedWallflw,FinishedElementsWallflw,
                                                                                               ShortestWallflw,boolWallfllw)
            #print('Wall flw', k)
        k += 1

        if k % 4 == 1 and boolAstar == False:
            CheckedAstar,FinishedAstar,ShortestAstar,boolAstar=solvealg.solveAstarparallel(gameDisplay,x2,y2,Maze,Grid,n,a,delay,CheckedAstar,FinishedAstar,ShortestAstar,boolAstar)
            #print('A*', k)
        k += 1

        if k % 4 == 2 and boolTremaux == False:
            FinishedTremaux, ShortestTremaux, DeadendTremaux, currentTremaux, tempCheckedTremaux,boolTremaux=solvealg.solveTremauxparrallel(
                gameDisplay,x3,y3,Maze,Grid,n,a,delay,FinishedTremaux,ShortestTremaux,DeadendTremaux,currentTremaux,tempCheckedTremaux,boolTremaux)
            #print('Tremaux', k)
        k += 1

        if k % 4 == 3 and boolDef == False:
            VisitedDef,ShortestDef ,DeadendDef, endFillDef, boolDef=solvealg.solveDeadendparallel(gameDisplay,x4,y4,Maze,Grid,n,a,delay,VisitedDef,ShortestDef,DeadendDef,endFillDef,boolDef)
            #print('Def',k)
        k += 1
        mazefunc.systemExit()
        #print('---')

    pygame.time.delay(1000)
    endtime = time.time()
    runtime = endtime - starttime
    print('Parallel mazesol runtime: {0:.2f}s'.format(runtime))

def SlideWallfw(n,Grid,Maze):
    starttime = time.time()
    a = mazefunc.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(mazefunc.white)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize / 2)
    mazefunc.textDisplay(gameDisplay, x1, y1, 'Wall follower algorithm', titleFontsize, mazefunc.navy)
    x2 = (scr[0] / 2 - n * a) / 2
    y2 = titleFontsize + math.ceil((scr[1] - titleFontsize - n * a) / 2)
    mazefunc.drawGrid(gameDisplay, x2, y2, n, a, Grid, (mazefunc.white, mazefunc.lncol, mazefunc.lgreen, mazefunc.salmon))
    pygame.display.update()

    textFontsize = 35
    x3 = scr[0] / 2 + 50
    y3 = y2 + (n * a - (titleFontsize *2 + textFontsize*7/4)) // 2
    mazefunc.textDisplayleft(gameDisplay, x3, y3, "# Also known as: left/right-hand rule", textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize / 2, "0. Select left or right as a direction",
                             textFontsize,
                             mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize, "1. Select the left/right cell of", textFontsize,
                             mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3+textFontsize*3/4, y3 + titleFontsize*5/4,
                             "previous one’s adjacent cells", textFontsize,
                             mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize * 7/4, "2. Repeat until target cell is processed", textFontsize,
                             mazefunc.navy)
    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize=20
    pygame.draw.line(gameDisplay, mazefunc.navy, (x1, titleFontsize), (x1, y0-tocFontsize), 5)
    mazefunc.mazeToc(gameDisplay, x0, y0, 4, tocFontsize, mazefunc.lnavy, mazefunc.navy)

    pygame.display.update()
    pygame.time.delay(4000)

    Shortest,Finished=solvealg.solveWallflw(gameDisplay,x2,y2,Maze,Grid,n,a,delay//3,True)
    if statBool==True:
        x3=scr[0]//4
        y3=3*((scr[1]-n*a-titleFontsize)//4)+n*a+titleFontsize-tocFontsize
        percentage=math.floor(100*((len(Shortest)+len(Finished))/(n**2-2)))
        mazefunc.textDisplay(gameDisplay,x3,y3,'Percentage of visited cells: {0}%'.format(percentage),titleFontsize//2,mazefunc.navy)
        pygame.display.update()
    pygame.time.delay(3000)
    endtime = time.time()
    runtime = endtime - starttime
    print('Wallfollower runtime: {0:.2f}s'.format(runtime))
    mazefunc.systemExit()

def SlideAstar(n,Grid,Maze):
    starttime = time.time()
    a = mazefunc.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(mazefunc.white)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize / 2)
    mazefunc.textDisplay(gameDisplay, x1, y1, 'A* algorithm', titleFontsize, mazefunc.navy)
    x2 = (scr[0] / 2 - n * a) / 2
    y2 = titleFontsize + math.ceil((scr[1] - titleFontsize - n * a) / 2)
    mazefunc.drawGrid(gameDisplay, x2, y2, n, a, Grid, (mazefunc.white, mazefunc.lncol, mazefunc.lgreen, mazefunc.salmon))
    pygame.display.update()

    textFontsize = 35
    x3 = scr[0] / 2 + 50
    y3 = y2 + (n * a - (titleFontsize * 2 + textFontsize*2)) // 2
    mazefunc.textDisplayleft(gameDisplay, x3, y3, "0. Create a list of adjacent cells",
                             textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3+textFontsize*3/4, y3+ titleFontsize* 1/ 4,
                             "with it’s distance to the target cell",
                             textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize*3 / 4, "1. Select cell with the smallest distance",
                             textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize*5/4, "2. Add adjacent cells of previously selected",
                             textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3+textFontsize*3/4, y3 + titleFontsize*6/4,
                             "to the list",
                             textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize*2,
                             "3. Repeat until target cell is processed",
                             textFontsize, mazefunc.navy)
    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize=20
    pygame.draw.line(gameDisplay, mazefunc.navy, (x1, titleFontsize), (x1, y0-tocFontsize), 5)
    mazefunc.mazeToc(gameDisplay, x0, y0, 5, tocFontsize, mazefunc.lnavy, mazefunc.navy)

    pygame.display.update()
    pygame.time.delay(4000)

    Shortest, Finished = solvealg.solveAstar(gameDisplay, x2, y2, Maze, Grid, n, a, delay//3, True)
    if statBool==True:
        x3=scr[0]//4
        y3=3*((scr[1]-n*a-titleFontsize)//4)+n*a+titleFontsize-tocFontsize
        percentage=math.floor(100*((len(Shortest)+len(Finished))/(n**2-2)))
        mazefunc.textDisplay(gameDisplay,x3,y3,'Percentage of visited cells: {0}%'.format(percentage),titleFontsize//2,mazefunc.navy)
        pygame.display.update()

    pygame.time.delay(3000)
    endtime = time.time()
    runtime = endtime - starttime
    print('A* runtime: {0:.2f}s'.format(runtime))
    mazefunc.systemExit()

def SlideTremaux(n, Grid, Maze):
    starttime = time.time()
    a = mazefunc.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(mazefunc.white)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize / 2)
    mazefunc.textDisplay(gameDisplay, x1, y1, 'Tremaux algorithm', titleFontsize, mazefunc.navy)
    x2 = (scr[0] / 2 - n * a) / 2
    y2 = titleFontsize + math.ceil((scr[1] - titleFontsize - n * a) / 2)
    mazefunc.drawGrid(gameDisplay, x2, y2, n, a, Grid,
                      (mazefunc.white, mazefunc.lncol, mazefunc.lgreen, mazefunc.salmon))
    pygame.display.update()

    textFontsize = 35
    x3 = scr[0] / 2 + 50
    y3 = y2 + (n * a - (titleFontsize * 2 + textFontsize*9/4)) // 2
    mazefunc.textDisplayleft(gameDisplay, x3, y3, "0. Mark each path once, when you follow it.", textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize / 2, "1. Never enter a path which has two marks on it.",
                             textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize, "2. Choose randomly an unmarked path",
                             textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3 + textFontsize, y3 + titleFontsize*3/2,
                             "If the path has a mark, turn around",
                             textFontsize, mazefunc.navy)

    mazefunc.textDisplayleft(gameDisplay, x3 + textFontsize, y3 + titleFontsize * 7 / 4,
                             "and return along that path",
                             textFontsize, mazefunc.navy)

    mazefunc.textDisplayleft(gameDisplay, x3+ textFontsize, y3 + titleFontsize*9/4,
                             "If not, choose randomly",
                             textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3 + textFontsize, y3 + titleFontsize * 10 / 4,
                             "one of the remaining paths.",
                             textFontsize, mazefunc.navy)


    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize*3,
                             "3. Repeat until target cell is processed.",
                             textFontsize, mazefunc.navy)
    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize = 20
    pygame.draw.line(gameDisplay, mazefunc.navy, (x1, titleFontsize), (x1, y0 - tocFontsize), 5)
    mazefunc.mazeToc(gameDisplay, x0, y0, 6, tocFontsize, mazefunc.lnavy, mazefunc.navy)

    mazefunc.updelay(4000)
    Shortest, Finished = solvealg.solveTremaux(gameDisplay, x2, y2, Maze, Grid, n, a, delay//3, True)
    if statBool == True:
        x3 = scr[0] // 4
        y3 = 3 * ((scr[1] - n * a - titleFontsize) // 4) + n * a + titleFontsize-tocFontsize
        percentage = math.floor(100 * ((len(Finished)) / (n ** 2 - 2)))
        mazefunc.textDisplay(gameDisplay, x3, y3, 'Percentage of visited cells: {0}%'.format(percentage),
                             titleFontsize // 2, mazefunc.navy)
        pygame.display.update()
    pygame.time.delay(3000)
    endtime = time.time()
    runtime = endtime - starttime
    print('Tremaux runtime: {0:.2f}s'.format(runtime))
    mazefunc.systemExit()

def SlideDeadend(n, Grid, Maze):
    starttime = time.time()
    a = mazefunc.rectSize(scr, n, marginsize, labelsize) * 1.4
    gameDisplay.fill(mazefunc.white)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize / 2)
    mazefunc.textDisplay(gameDisplay, x1, y1, 'Dead end filling algorithm', titleFontsize, mazefunc.navy)
    x2 = (scr[0] / 2 - n * a) / 2
    y2 = titleFontsize + math.ceil((scr[1] - titleFontsize - n * a) / 2)
    mazefunc.drawGrid(gameDisplay, x2, y2, n, a, Grid,
                      (mazefunc.white, mazefunc.lncol, mazefunc.lgreen, mazefunc.salmon))
    pygame.display.update()

    textFontsize = 35
    x3 = scr[0] / 2 + 50
    y3 = y2 + (n * a - (titleFontsize * 2 + textFontsize*6/4)) // 2
    mazefunc.textDisplayleft(gameDisplay, x3, y3, "0. Find all dead-ends in the maze", textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize / 2, "1. Fill the path from each",
                             textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3+textFontsize*3/4, y3 + titleFontsize* 3/ 4, "dead-end until a junction",
                             textFontsize, mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3, y3 + titleFontsize*5/4, "2. Unvisited cells are the path", textFontsize,
                             mazefunc.navy)
    mazefunc.textDisplayleft(gameDisplay, x3+textFontsize*3/4, y3 + titleFontsize * 6 / 4,
                             "to the target", textFontsize,
                             mazefunc.navy)

    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize = 20
    pygame.draw.line(gameDisplay, mazefunc.navy, (x1, titleFontsize), (x1, y0 - tocFontsize), 5)
    mazefunc.mazeToc(gameDisplay, x0, y0, 7, tocFontsize, mazefunc.lnavy, mazefunc.navy)
    pygame.display.update()
    pygame.time.delay(4000)

    Shortest, Finished = solvealg.solveDeadend(gameDisplay, x2, y2, Maze, Grid, n, a, delay//3, True)
    if statBool == True:
        x3 = scr[0] // 4
        y3 = 3 * ((scr[1] - n * a - titleFontsize) // 4) + n * a + titleFontsize-tocFontsize
        percentage = math.floor(100 * ((len(Shortest) + len(Finished)) / (n ** 2 - 2)))
        mazefunc.textDisplay(gameDisplay, x3, y3, 'Percentage of visited cells: {0}%'.format(percentage),
                             titleFontsize // 2, mazefunc.navy)
        pygame.display.update()

    pygame.time.delay(3000)
    endtime = time.time()
    runtime = endtime - starttime
    print('Deadend runtime: {0:.2f}s'.format(runtime))
    mazefunc.systemExit()

def SlideHexagonal(n):
    starttime = time.time()
    a = mazefunc.hexSize(scr, n, marginsize, labelsize) * 1.8
    gameDisplay.fill(mazefunc.white)
    titleFontsize = 100
    x1 = scr[0] / 2
    y1 = math.ceil(titleFontsize / 2)
    mazefunc.textDisplay(gameDisplay, x1, y1, 'Hexagonal mazes', titleFontsize, mazefunc.navy)
    x2 = scr[0] / 2
    y2 = titleFontsize + 75
    x0 = 0
    y0 = scr[1] // 100 * 98
    tocFontsize = 20
    mazefunc.mazeToc(gameDisplay, x0, y0, 8, tocFontsize, mazefunc.lnavy, mazefunc.navy)
    mazefunc.updelay(1000)

    Grid,Maze,Hexagonal=mazealg.mazeKruskalhex(gameDisplay,x2,y2,n,a,(mazefunc.dgrey,mazefunc.black,mazefunc.lgreen,mazefunc.salmon),delay//10,True)
    pygame.time.delay(2000)
    solvealg.solveAstarhex(gameDisplay,x2,y2,Maze,Grid,Hexagonal,n,a,delay//5,False)
    endtime = time.time()
    runtime = endtime - starttime
    print('Hexagonal runtime: {0:.2f}s'.format(runtime))
    mazefunc.systemExit()