import pygame, math, openpyxl, datetime

line_thickness=1
#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255,0,0)
navy = 	(0,0,128)
lnavy = (127,127,255)
salmon=(250,128,114)
lsalmon=(250,200,200)
lgreen=(145,243,96)
llgreen=(200,255,200)
silver=(192,192,192)
lyellow= (240,230,140)
lblue=(135,206,235)
lgrey=(211,211,211)
dgrey=(169,169,169)
ddgrey=(79,79,79)
dred=(180,40,10)
mred=(250,65,80)
lred=(250,160,150)
gold=(219, 186, 0)
lgold=(255,215,0)
dgreen=(0,128,64)
green=(0,170,85)
dblue=(0,74,111)
blue=(0,110,162)

bgrcol=(255,255,255)
lncol=(0,0,0)
stcol=(145,243,96)
fncol=(250,128,114)

scr=(1280, 924)



def rectSize(screen,n,marginsize,labelsize):    #calculate the optimal rectangle size
    a = (min(screen[0], screen[1]) / 2 - marginsize-labelsize)/n
    a=math.floor(a)
    return a

def textDisplay(display,x,y,string,size,color): #centered text display
    myfont = pygame.font.SysFont('cabria', size)
    text = myfont.render(string, True, color, (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = x
    textrect.centery = y
    display.blit(text, textrect)

def textDisplay2(display,x,y,string,size,color,bgrcol): #centered text display
    myfont = pygame.font.SysFont('cabria', size)
    text = myfont.render(string, True, color, bgrcol)
    textrect = text.get_rect()
    textrect.centerx = x
    textrect.centery = y
    display.blit(text, textrect)

def textDisplayleft(display,x,y,string,size,color):
    myfont = pygame.font.SysFont('cabria', size)
    text = myfont.render(string, True, color)
    display.blit(text, (x,y))


def drawRect(screen, x, y, a, T, bgrcol, lncol):
    #line_thickness=1
    temp=(x,y)
    plus=((a,0),(0,a),(-a,0),(0,-a))
    pygame.draw.rect(screen, bgrcol, (x, y, a + line_thickness, a + line_thickness), 0)
    for i in range(0,len(T)):
        if T[i]==True:
            pygame.draw.line(screen, lncol, [temp[0], temp[1]], [temp[0] + plus[i][0], temp[1] + plus[i][1]], line_thickness)
        else:
            pygame.draw.line(screen, bgrcol, [temp[0], temp[1]], [temp[0] + plus[i][0], temp[1] + plus[i][1]], line_thickness)
        temp=(temp[0]+plus[i][0],temp[1]+plus[i][1])
    plus=((a,0),(a,a),(0,a),(0,0))
    for i in range(0,4):
        if (T[i] or T[(i+1)%4])==True:
            pygame.draw.line(screen, lncol, (x + plus[i][0], y + plus[i][1]), (x + plus[i][0], y + plus[i][1]),
                             line_thickness)

#mazecol=(background col,line col,start field col, end field col)
def drawGrid(screen,x,y,n,a,Grid,mazecol):
    bgrcol=mazecol[0]
    lncol=mazecol[1]
    for i in range(0,n):
        for j in range(0,n):
            drawRect(screen,x+j*a,y+i*a,a,Grid[i*n+j],bgrcol,lncol)
    if mazecol[2]!=mazecol[0] and mazecol[3]!=mazecol[0]:
        colorRegion(screen,x,y,n,a,Grid,0,mazecol[2])
        colorRegion(screen,x,y,n,a,Grid,n**2-1,mazecol[3])

def drawGrid2(screen,x,y,n,a,Grid,mazecol):
    bgrcol=mazecol[0]
    lncol=mazecol[1]
    for i in range(0,n):
        for j in range(0,n):
            drawRect(screen,x+j*a,y+i*a,a,Grid[i*n+j],bgrcol,lncol)
    if mazecol[2]!=mazecol[0] and mazecol[3]!=mazecol[0]:
        colorRegion2(screen,x,y,n,a,Grid,0,mazecol[2],lncol)
        colorRegion2(screen,x,y,n,a,Grid,n**2-1,mazecol[3],lncol)

def edgeGen(n):
    Edges=[]
    #rows
    for i in range(0,n):
        for j in range(0,n-1):
            Edges.append((i*n+j,i*n+j+1))
    #Colums
    for i in range(0,n-1):
        for j in range(0,n):
            Edges.append((i*n+j,(i+1)*n+j))
    return Edges

def regionGen(n):
    Regions=[[i] for i in range(0,n**2)]
    return Regions

def gridGen(n): # n x n rect list with bools for edges
    Grid=[[True,True,True,True] for i in range(0,n**2)]
    return Grid

def mazePic(n,Grid,mazecol,flname):
    a=rectSize((1024,768),n,50,75)
    win = pygame.Surface((1024, 768))
    win.fill(white)
    x=(1024-n*2*a)//2
    y=(768-n*2*a)//2
    drawGrid(win,x,y,n,2*a,Grid,mazecol)
    filename = "{0}.png".format(flname)
    pygame.image.save(win, 'mazes\size{0}\{1}'.format(n,filename))
    print("file {} has been saved".format(filename))
    # update the display window to show the drawing

def mazeLogfc(a,b):
    for i in range(a, b, 5):
        book = openpyxl.Workbook()
        sheet = book.active
        sheet['A1'] = 'size'
        sheet['B1'] = i
        sheet['A2'] = 'generated mazes'
        sheet['B2'] = 0
        sheet['A3'] = 'name'
        sheet['B3'] = 'algorithm'
        sheet['C3'] = 'date&time'
        book.save('mazes\size{0}\size{1}log.xlsx'.format(i, i))

def mazeLog(n,id,algorithm):
    book = openpyxl.load_workbook('mazes\size{0}\size{1}log.xlsx'.format(n, n))
    sheet = book.active
    time = datetime.datetime.now().strftime('%Y:%m:%d %H:%M:%S')

    sheet.cell(id + 4, 1).value = "maze20_%d" % id
    sheet.cell(id + 4, 2).value =algorithm
    sheet.cell(id + 4, 3).value = time

    id += 1
    sheet.cell(2, 2).value = id
    book.save('mazes\size{0}\size{1}log.xlsx'.format(n, n))

def edgeErase(x,y,n,a,line_thickness,k,l): #n=maze dimension, (x,y)=coordinates of griid upper-left point, k,l=grid k th, l th region (k<l)
    if k < l:
        t = l
        l = k
        k = t
    if abs(k-l)==1:
        begincdList=[x+(k%n)*a,y+(k//n)*a+line_thickness] #begin coordinates
        endcdList=[x+(k%n)*a,y+((k//n)+1)*a-line_thickness] #end coordinates
    else:
        begincdList = [x + (k % n) * a+ line_thickness, y + (k // n) * a]  # begin coordinates
        endcdList = [x + (k % n+1) * a - line_thickness, y + (k // n) * a]  # end coordinates
    return begincdList,endcdList

'need to rewrite'
def regionNeighbor(n,k):
    if k==0:
        return [k+1,k+n]
    elif k==n-1:
        return [n-2,2*n-1]
    elif k==(n-1)*n:
        return [(n-2)*n,(n-1)*n+1]
    elif k==n*n-1:
        return [(n-1)*n-1,n*n-2]
    elif k//n==0 and (k!=0 or k!=n-1):
        return [k-1,k+1,k+n]
    elif k//n==n-1 and (k!=(n-1)*n or n*n-1):
        return [k-1,k+1,k-n]
    elif k%n==0 and (k!=0 or k!=(n-1)*n):
        return [k-n,k+1,k+n]
    elif k%n==n-1 and (k!=(n-1) or n*n-1):
        return [k-n,k-1,k+n]
    else:
        return [k-n,k+1,k+n,k-1]

'need to rewrite'
def gridEdgeremove(Grid,n,edge0,edge1):
    if edge0<edge1:
        if edge1-edge0==1:
            Grid[edge0][1]=False
            Grid[edge1][3]=False
        elif (edge1-edge0)==n:
            Grid[edge0][2] = False
            Grid[edge1][0] = False
        else:
            print("wrong edges")
    else:
        if edge0-edge1==1:
            Grid[edge0][3]=False
            Grid[edge1][1]=False
        elif (edge1-edge0)==n:
            Grid[edge0][0] = False
            Grid[edge1][2] = False
        else:
            print("wrong edges")
    return Grid

def colorRegion(screen, x , y, n, a, Grid, region,col):
    pygame.draw.rect(screen, col, [x+(region%n)*a, y+(region//n)*a, a + 1, a + 1], 0)
    drawRect(screen, x+(region%n)*a, y+(region//n)*a, a, Grid[region], col, lncol)

def colorRegion2(screen, x , y, n, a, Grid, region,col,lncol):
    pygame.draw.rect(screen, col, [x+(region%n)*a, y+(region//n)*a, a + 1, a + 1], 0)
    drawRect(screen, x+(region%n)*a, y+(region//n)*a, a, Grid[region], col, lncol)

#update and delay
def updelay(milisec):
    pygame.display.update()
    pygame.time.delay(milisec)

def mazeSpeed(n,delay,speed,step,limits):
    perc1=limits[0][0]
    speedup1=limits[0][1]
    perc2=limits[1][0]
    speedup2=limits[1][1]
    perc3 = limits[2][0]
    speedup3 = limits[2][1]
    if step >= math.floor(n ** 2 * perc1) and speed == 0:
        speed += 1
        delay = delay // speedup1
    if step >= math.floor(n ** 2 * perc2) and speed == 1:
        speed += 1
        delay = delay // speedup2
    if step >= math.floor(n ** 2 * perc3) and speed == 1:
        speed += 1
        delay = delay // speedup3
    return speed,delay

def mazeUpdate(n,Edges,Maze,Grid,edge0,edge1):
    remEdge = (edge0, edge1)
    Edges.remove(remEdge)
    Maze.append(remEdge)
    Grid = gridEdgeremove(Grid, n, edge0, edge1)
    return Edges,Maze,Grid

def mazeCreate(n):
    Edges = edgeGen(n)
    Grid = gridGen(n)
    Maze = []
    return Edges,Maze,Grid

def distance(vertex,n):  #vertex mazefunc.distance from endpoint with (n-1,n-1) coord
    return n-(vertex//n+1)+n-(vertex%n+1)-1

def mazeDeadend(n,Maze):
    Celltype=[[i,0] for i in range(0,n**2)]
    for i in Maze:
        Celltype[i[0]][1] += 1
        Celltype[i[1]][1] += 1

    Deadend=[]
    Branch=[]
    for j in Celltype:
        if j[1]==1:
            Deadend.append(j[0])
        elif j[1]>=3:
            Branch.append(j[0])
    if 0 in Deadend:
        Deadend.remove(0)
    if n**2-1 in Deadend:
        Deadend.remove(n**2-1)
    return Deadend,Branch

def mazeEndfiller(n,Maze,Visited,vertex):
    endFill=[vertex]
    Neighbors=regionNeighbor(n,vertex)
    i=0
    Neighbors.append(-1)
    while Neighbors[i]!=-1:
        tempVertex=Neighbors[i]
        edge=(min(vertex,tempVertex),max(vertex,tempVertex))
        if edge not in Maze or tempVertex in Visited:
            Neighbors.remove(tempVertex)
        else:
            i+=1
    Neighbors.remove(-1)
    Visited.append(vertex)

    while len(Neighbors)==1:
        nextVertex=Neighbors[0]
        endFill.append(nextVertex)
        Neighbors=regionNeighbor(n,nextVertex)
        i = 0
        Neighbors.append(-1)
        while Neighbors[i] != -1:
            tempVertex = Neighbors[i]
            edge = (min(nextVertex, tempVertex), max(nextVertex, tempVertex))
            if (edge not in Maze or tempVertex in Visited) and (nextVertex!=0 and nextVertex!=n**2-1):
                Neighbors.remove(tempVertex)
            else:
                i += 1
        Neighbors.remove(-1)
        if len(Neighbors)==1:
            Visited.append(nextVertex)

    endFill.remove(endFill[-1])
    return endFill

def uniq(List):
    sortList=[(List[i],i) for i in range(0,len(List))]
    sortList.sort(key=lambda tup: tup[0])
    for i in range(0,len(sortList)-1):
        if sortList[i][0]==sortList[i+1][0]:
            List.remove(sortList[i][0])
    return List

def leftMove(n,vertex,Neighbors):
    if len(Neighbors)==1:
        return Neighbors[0]
    else:
        #rightward
        if vertex[0]-vertex[1]==1:
            return min(Neighbors)
        #leftward
        elif vertex[0]-vertex[1]==-1:
            return max(Neighbors)
        #upward
        elif vertex[0]-vertex[1]==-n:
            temp=0
            modtemp=n-1
            for i in Neighbors:
                if (i%n)<=modtemp:
                    modtemp=i%n
                    temp=i
            return temp
        #downward
        elif vertex[0]-vertex[1]==n:
            temp = 0
            modtemp = 0
            for i in Neighbors:
                if (i % n) >= modtemp:
                    modtemp = i % n
                    temp = i
            return temp

def drawHex(screen, x, y, a, T, bgrcol, lncol):
    pygame.draw.polygon(screen, bgrcol,
                        [(x, y), (x + a * math.cos(math.pi / 6), y - a * math.sin(math.pi / 6)),
                         (x + 2 * a * math.cos(math.pi / 6), y),
                         (x + 2 * a * math.cos(math.pi / 6), y + a),
                         (x + a * math.cos(math.pi / 6), y + a + a * math.sin(math.pi / 6)), (x, y + a)],0)
    if T[0]==True:
        pygame.draw.line(screen,lncol,(x, y), (x + a * math.cos(math.pi / 6), y - a * math.sin(math.pi / 6)),1)
    else:
        pygame.draw.line(screen, bgrcol, (x, y), (x + a * math.cos(math.pi / 6), y - a * math.sin(math.pi / 6)), 1)
    if T[1]==True:
        pygame.draw.line(screen, lncol, (x + a * math.cos(math.pi / 6), y - a * math.sin(math.pi / 6)),
                         (x + 2 * a * math.cos(math.pi / 6), y), 1)
    else:
        pygame.draw.line(screen, bgrcol, (x + a * math.cos(math.pi / 6), y - a * math.sin(math.pi / 6)),
                     (x + 2 * a * math.cos(math.pi / 6), y), 1)
    if T[2]==True:
        pygame.draw.line(screen, lncol, (x + 2 * a * math.cos(math.pi / 6), y),
                         (x + 2 * a * math.cos(math.pi / 6), y + a), 1)
    else:
        pygame.draw.line(screen, bgrcol, (x + 2 * a * math.cos(math.pi / 6), y),
                         (x + 2 * a * math.cos(math.pi / 6), y + a), 1)
    if T[3]==True:
        pygame.draw.line(screen, lncol, (x + 2 * a * math.cos(math.pi / 6), y + a),
                         (x + a * math.cos(math.pi / 6), y + a + a * math.sin(math.pi / 6)), 1)
    else:
        pygame.draw.line(screen, bgrcol, (x + 2 * a * math.cos(math.pi / 6), y + a),
                         (x + a * math.cos(math.pi / 6), y + a + a * math.sin(math.pi / 6)), 1)
    if T[4]==True:
        pygame.draw.line(screen, lncol, (x + a * math.cos(math.pi / 6), y + a + a * math.sin(math.pi / 6)), (x, y + a), 1)
    else:
        pygame.draw.line(screen, bgrcol, (x + a * math.cos(math.pi / 6), y + a + a * math.sin(math.pi / 6)), (x, y + a), 1)
    if T[5]==True:
        pygame.draw.line(screen, lncol, (x, y + a),(x, y), 1)
    else:
        pygame.draw.line(screen, bgrcol, (x, y + a), (x, y), 1)

def drawHexgrid(screen,x,y,n,a,Grid,bgrcol,lncol):
    m=n
    p=1
    q=0
    for i in range(0,2*n-1):
        for j in range(0,m):
            drawHex(screen,x-m*(a*math.cos(math.pi/6))+j*(2*a*math.cos(math.pi/6)),y+i*(a+a*math.sin(math.pi/6)),a,Grid[q],bgrcol,lncol)
            q+=1
        if m==2*n-1:
            p=-p
        m += p

def drawHex(screen, x, y, a, T, bgrcol, lncol):
    pygame.draw.polygon(screen, bgrcol,
                        [(x, y), (x + a * math.cos(math.pi / 6), y - a * math.sin(math.pi / 6)),
                         (x + 2 * a * math.cos(math.pi / 6), y),
                         (x + 2 * a * math.cos(math.pi / 6), y + a),
                         (x + a * math.cos(math.pi / 6), y + a + a * math.sin(math.pi / 6)), (x, y + a)],0)
    if T[0]==True:
        pygame.draw.line(screen,lncol,(x, y), (x + a * math.cos(math.pi / 6), y - a * math.sin(math.pi / 6)),1)
    else:
        pygame.draw.line(screen, bgrcol, (x, y), (x + a * math.cos(math.pi / 6), y - a * math.sin(math.pi / 6)), 1)
    if T[1]==True:
        pygame.draw.line(screen, lncol, (x + a * math.cos(math.pi / 6), y - a * math.sin(math.pi / 6)),
                         (x + 2 * a * math.cos(math.pi / 6), y), 1)
    else:
        pygame.draw.line(screen, bgrcol, (x + a * math.cos(math.pi / 6), y - a * math.sin(math.pi / 6)),
                     (x + 2 * a * math.cos(math.pi / 6), y), 1)
    if T[2]==True:
        pygame.draw.line(screen, lncol, (x + 2 * a * math.cos(math.pi / 6), y),
                         (x + 2 * a * math.cos(math.pi / 6), y + a), 1)
    else:
        pygame.draw.line(screen, bgrcol, (x + 2 * a * math.cos(math.pi / 6), y),
                         (x + 2 * a * math.cos(math.pi / 6), y + a), 1)
    if T[3]==True:
        pygame.draw.line(screen, lncol, (x + 2 * a * math.cos(math.pi / 6), y + a),
                         (x + a * math.cos(math.pi / 6), y + a + a * math.sin(math.pi / 6)), 1)
    else:
        pygame.draw.line(screen, bgrcol, (x + 2 * a * math.cos(math.pi / 6), y + a),
                         (x + a * math.cos(math.pi / 6), y + a + a * math.sin(math.pi / 6)), 1)
    if T[4]==True:
        pygame.draw.line(screen, lncol, (x + a * math.cos(math.pi / 6), y + a + a * math.sin(math.pi / 6)), (x, y + a), 1)
    else:
        pygame.draw.line(screen, bgrcol, (x + a * math.cos(math.pi / 6), y + a + a * math.sin(math.pi / 6)), (x, y + a), 1)
    if T[5]==True:
        pygame.draw.line(screen, lncol, (x, y + a),(x, y), 1)
    else:
        pygame.draw.line(screen, bgrcol, (x, y + a), (x, y), 1)

def drawHexgrid(screen,x,y,n,a,Grid,bgrcol,lncol):
    m=n
    p=1
    q=0
    for i in range(0,2*n-1):
        for j in range(0,m):
            drawHex(screen,x-m*(a*math.cos(math.pi/6))+j*(2*a*math.cos(math.pi/6)),y+i*(a+a*math.sin(math.pi/6)),a,Grid[q],bgrcol,lncol)
            #textDisplay2(screen,x-m*(a*math.cos(math.pi/6))+j*(2*a*math.cos(math.pi/6))+(a*math.cos(math.pi/6)),y+i*(a+a*math.sin(math.pi/6))+a//2,'{0}'.format(q),20,black,bgrcol)
            q+=1
        if m==2*n-1:
            p=-p
        m += p

def regionHexgen(n):
    Regions=[]
    m = n
    p = 1
    q = 0
    for i in range(0, 2 * n - 1):
        Row=[]
        for j in range(0, m):
            Row.append(q)
            q += 1
        Regions.append(Row)
        if m == 2 * n - 1:
            p = -p
        m += p
    return Regions

def edgeHexgen(n,Regions):
    Edges=[]
    #rows
    for i in Regions:
        for j in range(0,len(i)-1):
            Edges.append((i[j],i[j+1]))
    #left diagonal upper par
    for i in range(0,n-1):
        for j in range(0,len(Regions[i])):
            Edges.append((Regions[i][j],Regions[i+1][j]))
    #left diagonal lower part
    for i in range(n-1,2*n-2):
        for j in range(1,len(Regions[i])):
            Edges.append((Regions[i][j],Regions[i+1][j-1]))
    #right diagonal upper part
    for i in range(0,n-1):
        for j in range(0,len(Regions[i])):
            Edges.append((Regions[i][j],Regions[i+1][j+1]))
    #right diagonal lower part
    for i in range(n-1,2*n-2):
        for j in range(0,len(Regions[i])-1):
            Edges.append((Regions[i][j],Regions[i+1][j]))
    return Edges

def gridHexgen(n):
    Grid = [[True for i in range(0, 6)] for j in range(0, 6 * (n * (n + 1) // 2) + 1)]
    return Grid

def mazeHexcreate(n,Regions):
    Edges = edgeHexgen(n,Regions)
    Grid = gridHexgen(n)
    Maze = []
    return Edges,Maze,Grid

def colorHexregion(screen, x, y, n, a, Grid, Hexagonal, region, col):
    row,column,m=hexRegposition(n,Hexagonal,region)
    drawHex(screen,x-m*(a*math.cos(math.pi/6))+column*(2*a*math.cos(math.pi/6)),y+row*(a+a*math.sin(math.pi/6)),a,Grid[region],col,black)

def hexRegposition(n,Hexagonal,region):
    row = 0;
    column = 0;
    for i in Hexagonal:
        if region in i:
            for j in i:
                if region == j:
                    row = Hexagonal.index(i)
                    column = i.index(j)
                    break
            if row != 0 or column != 0:
                break
    if row < n:
        m = row + n
    else:
        m = 2 * n - 1 - (row - (n - 1))
    return row,column,m

def edgeHexerase(screen,x, y, n, a,Hexagonal ,line_thickness, edge0, edge1): #n=maze dimension, (x,y)=coordinates of griid upper-left point, k,l=grid k th, l th region (k<l)
    row0, column0, m0 = hexRegposition(n, Hexagonal, edge0)
    row1, column1, m1 = hexRegposition(n, Hexagonal, edge1)
    xcord0=x - m0 * (a * math.cos(math.pi / 6)) + column0 * (2 * a * math.cos(math.pi / 6)) + (a * math.cos(math.pi / 6))
    ycord0=y + row0 * (a + a * math.sin(math.pi / 6)) + a // 2

    if row0==row1: #in the same row
        pygame.draw.line(screen, white, (xcord0 + 2 * a * math.cos(math.pi / 6), ycord0),
                         (xcord0 + 2 * a * math.cos(math.pi / 6), ycord0 + a), 1)
    elif row1<=n-1 and column0==column1: #same upper right diagonal
        pygame.draw.line(screen, white, (xcord0 + a * math.cos(math.pi / 6), ycord0 + a + a * math.sin(math.pi / 6)), (xcord0, ycord0 + a),
                         1)
    elif row1>=n and column0==column1+1: #same lower right diagonal
        pygame.draw.line(screen, white, (xcord0 + a * math.cos(math.pi / 6), ycord0 + a + a * math.sin(math.pi / 6)), (xcord0, ycord0 + a),
                         1)
    elif row1<=n-1 and column0==column1+1: #same upper left diagonal
        pygame.draw.line(screen, white, (x + 2 * a * math.cos(math.pi / 6), y + a),
                         (x + a * math.cos(math.pi / 6), y + a + a * math.sin(math.pi / 6)), 1)
    elif row1>=n and column0==column1:
        pygame.draw.line(screen, white, (x + 2 * a * math.cos(math.pi / 6), y + a),
                         (x + a * math.cos(math.pi / 6), y + a + a * math.sin(math.pi / 6)), 1)

def gridHexedgeremove(Grid,Hexagonal,n,edge0,edge1):
    row0, column0, m0 = hexRegposition(n, Hexagonal, edge0)
    row1, column1, m1 = hexRegposition(n, Hexagonal, edge1)

    if row0 == row1:  # in the same row
        Grid[edge0][2]=False
        Grid[edge1][5]=False
    elif row1 <= n - 1 and column0 == column1:  # same upper left diagonal
        Grid[edge0][4] = False
        Grid[edge1][1] = False
    elif row1 >= n and column0 == column1 + 1:  # same lower left diagonal
        Grid[edge0][4] = False
        Grid[edge1][1] = False
    elif row1 <= n - 1 and column0+1 == column1:  # same upper right diagonal
        Grid[edge0][3] = False
        Grid[edge1][0] = False
    elif row1 >= n and column0 == column1: #same lower right diagonal
        Grid[edge0][3] = False
        Grid[edge1][0] = False
    return Grid


def mazeHexupdate(n,Edges,Maze,Grid,Hexagonal,edge0,edge1):
    remEdge = (edge0, edge1)
    Edges.remove(remEdge)
    Maze.append(remEdge)
    Grid = gridHexedgeremove(Grid,Hexagonal ,n, edge0, edge1)
    return Edges,Maze,Grid

def mazeHexposition(x,y,n,a):
    x=x+(2*n-1)*a*math.cos(math.pi/6)
    y=y+a*math.sin(math.pi/6)
    return x,y

def hexSize(scr,n,marginsize,labelsize):    #calculate the optimal rectangle size
    a = ((min(scr[0], scr[1]) - marginsize-labelsize)/2 )/ (2*n)
    a=a/(1+math.sin(math.pi/6))
    a = math.floor(a)
    return a

def hexDistance(n,Hexagonal,vertex):  #vertex mazefunc.distance from endpoint with (n-1,n-1) coord
    row0,column0,m0=hexRegposition(n,Hexagonal,vertex)
    row1,column1,m1=(n-1),2*(n-1),2*n-1 #basic endpoint
    return abs(row1-row0)+abs(column1-column0)-(m1-m0)

def regionNeighborHex(n,Hexagonal,k):
    row, column, m = hexRegposition(n, Hexagonal,k)
    #first row
    if row==0:
        if column==0:
            return [k+1,k+n,k+n+1]
        elif column==n-1:
            return [k-1,k+n,k+n+1]
        else:
            return [k-1,k+1,k+n,k+n+1]
    #middle row
    elif row==n-1:
        if column==0:
            return [k+1,k+(2*n-1),k-2*(n-1)]
        elif column==2*(n-1):
            return [k-1,k-(2*n-1),k+2*(n-1)]
        else:
            return [k-1,k+1,k-2*(n-1),k-2*(n-1)-1,k+2*(n-1),k+2*(n-1)+1]
    #last row
    elif row==2*(n-1):
        if column==0:
            return [k-n-1,k-n,k+1]
        elif column==n-1:
            return [k-1,k-n-1,k-n]
        else:
            return [k-1,k+1,k-n,k-n-1]
    #other upper rows
    elif row>0 and row<(n-1):
        if column==0:
            return [k-m+1,k+1,k+m,k+m+1]
        elif column==m-1:
            return [k-m,k-1,k+m,k+m+1]
        else:
            return [k-1,k+1,k-m,k-m+1,k+m,k+m+1]
    #other lower rows
    else:
        if column==0:
            return [k-m-1,k-m,k+1,k+m]
        elif column==m-1:
            return [k-m-1,k-m,k-1,k+m-1]
        else:
            return [k-1,k+1,k-m,k-m-1,k+m,k+m-1]

#Table of contents
#k: current slide number
def mazeToc(screen,x,y,slidenum,fontsize,col1,col2):
    textList=['Kruskal\'s alg.','Sidewinder alg.','Rec. backtr. alg.','Prim\'s alg.','Wallfollower alg.', 'A* alg.','Tremaux alg.','Dead end f.  alg.','Hexagonal mazes']
    step=(scr[0])//len(textList)
    for i in range(0,len(textList)):
        if i==slidenum:
            textDisplay(screen, x+step//2+i*step, y, textList[i], fontsize, col2)
        else:
            textDisplay(screen, x+step//2+i*step, y, textList[i], fontsize, col1)

def systemExit():
    RUNNING, PAUSE = 0, 1
    state = RUNNING
    while True:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    raise SystemExit
                elif e.key == pygame.K_SPACE:
                    if state == RUNNING:
                        state = PAUSE


        while state == PAUSE:
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        raise SystemExit
                    elif e.key == pygame.K_SPACE:
                        state = RUNNING
        break

def mazeRange(n,Maze,vertex,r):
    rangeList=[]
    row=vertex%n
    column=vertex//n

    #horizontal rightward
    if row+r<=n-1:
        endvertex=vertex+r
    else:
        endvertex=row*(n-1)

    for i in range(vertex,endvertex):
        if (i,i+1) in Maze:
            rangeList.append(i+1)
        else:
            break

    #horizontal leftward
    if row-r>=0:
        startvertex=vertex-r
    else:
        startvertex=row*n

    for i in range(startvertex,vertex):
        if (i,i+1) in Maze:
            rangeList.append(i+1)
        else:
            break

    #verticcal upward
    if column-r>=0:
        startvertex=vertex-(r*n)
    else:
        startvertex=column

    for i in range(startvertex,vertex,n):
        if (i,i+n) in Maze:
            rangeList.append(i+n)
        else:
            break

    #vertical downward
    if column+r<=n-1:
        endvertex=column+r*n
    else:
        endvertex=(n-1)*n+column
    for i in range(vertex,endvertex,n):
        if (i,i+n) in Maze:
            rangeList.append(i+n)
        else:
            break

    return rangeList

def mouseRegionPosition(x,y,n,a,):
    region=-1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                region=(pos[1]-y)//(2*a)*n+(pos[0]-x)//(2*a)
                return region
        if region!=-1:
            break

def drawFigure(screen,x,y,a,col):
    pygame.draw.circle(screen,col,(x+a//2,y+math.floor(7/32*a)),math.floor(3/32*a),0) #head
    pygame.draw.line(screen,col,(x+a//2,y+math.floor(10/32*a)),(x+a//2,y+math.floor(16/32*a)),3) #body
    pygame.draw.line(screen,col,(x+a//2,y+math.floor(13/32*a)),(x+a//2-a//6,y+math.floor(15/32*a)),3) #left arm
    pygame.draw.line(screen,col,(x+a//2,y+math.floor(13/32*a)),(x+a//2+a//6,y+math.floor(15/32*a)),3) #right arm
    pygame.draw.line(screen,col,(x+a//2,y+math.floor(16/32*a)),(x+a//2-a//8,y+math.floor(22/32*a)),3) #left leg
    pygame.draw.line(screen,col,(x+a//2,y+math.floor(16/32*a)),(x+a//2+a//8,y+math.floor(22/32*a)),3) #right leg'''

def dist(n,vertex1,vertex2): #need to sync dist and distance
    return math.abs(vertex1//n-vertex2//n)+math.abs(vertex1%n-vertex2%n)
