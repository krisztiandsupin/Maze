'''import mazefunc
import pygame, random,math

scr = (1024, 768)
margin=15
titleLabel=75
line_thickness = 1

hlcol1=mazefunc.lred #highlight color
hlcol2=mazefunc.mred #highlisht color 2
mbgrcol=mazefunc.white

#delay=-1: draw nothing
#delay=0: draw without steps
def mazeKruskal(screen,x,y,n,a,mazecol,delay,stepBool):
    textsize=math.ceil(a * 0.75)
    bgrcol = mazecol[0]
    lncol = mazecol[1]
    m = (2 * n * (n - 1)) - 1  # length Edges

    if stepBool==True and (delay==-1 or delay==0):
        delay=1000

    Edges, Maze, Grid = mazefunc.mazeCreate(n)
    Regions = mazefunc.regionGen(n)
    RegionStep = [i for i in range(0, n ** 2)]

    if delay!=-1:
        mazefunc.drawGrid(screen,x,y,n, a, Grid,(bgrcol,lncol,bgrcol,bgrcol))
    if stepBool==True:
        for i in range(0, n):
            for j in range(0, n):
                mazefunc.textDisplay2(screen, x + j * a + a / 2, y + i * a + a / 2, "{0}".format(i * n + j),
                                     textsize, mazefunc.black,bgrcol)
        mazefunc.updelay(4000)
        step = 1
        speed = 0

    while len(Regions) != 1:
        randEdge = random.choice(Edges)
        edge0 = randEdge[0]
        edge1 = randEdge[1]
        i = 0
        while i <= m:
            if edge0 in Regions[i]:
                break
            else:
                i += 1
        j = 0
        while j <= m:
            if edge1 in Regions[j]:
                break
            else:
                j += 1

        if stepBool:
            mazefunc.colorRegion(screen,x,y,n,a,Grid,edge0,hlcol1)
            mazefunc.textDisplay2(screen, x + (edge0 % n) * a + a / 2, y + (edge0 // n) * a + a / 2,
                                  "{0}".format(RegionStep[edge0]), textsize, mazefunc.black, hlcol1)
            mazefunc.colorRegion(screen,x,y,n,a,Grid,edge1,hlcol1)
            mazefunc.textDisplay2(screen, x + (edge1 % n) * a + a / 2, y + (edge1 // n) * a + a / 2,
                                  "{0}".format(RegionStep[edge1]), textsize, mazefunc.black, hlcol1)
            mazefunc.updelay(delay//2)

        if i != j:
            for k in range(0, len(Regions[j])):
                Regions[i].append(Regions[j][k])
                Neighbors=mazefunc.regionNeighbor(n,Regions[j][k])  #check neighbors of vertex k
                for l in Neighbors:
                    edge=(min(Regions[j][k],l),max(Regions[j][k],l))
                    if l in Regions[i] and edge in Edges and edge!=randEdge:
                        Edges.remove(edge)

            regionvalue = min(Regions[i])
            for l in Regions[i]:
                if stepBool == True:
                    mazefunc.colorRegion(screen,x,y,n,a,Grid,l,mazefunc.bgrcol)
                    mazefunc.textDisplay(screen, x + (l % n) * a + a / 2, y + (l // n) * a + a / 2,
                                         "{0}".format(regionvalue), textsize, mazefunc.black)
                RegionStep[l] = regionvalue

            Regions.remove(Regions[j])
            Edges, Maze, Grid = mazefunc.mazeUpdate(n, Edges, Maze, Grid, edge0, edge1)
            if delay!=0 and delay!=1:
                begincoord, endcoord = mazefunc.edgeErase(x, y, n, a, line_thickness, edge0, edge1)
                pygame.draw.line(screen, bgrcol, begincoord, endcoord, line_thickness)
                mazefunc.updelay(delay)

            if stepBool == True:
                mazefunc.colorRegion(screen,x,y,n,a,Grid,edge0,mazefunc.bgrcol)
                mazefunc.textDisplay(screen, x + (edge0 % n) * a + a / 2, y + (edge0 // n) * a + a / 2,
                                     "{0}".format(RegionStep[edge0]), textsize, mazefunc.black)
                mazefunc.colorRegion(screen, x, y, n, a, Grid, edge1, mazefunc.bgrcol)
                mazefunc.textDisplay(screen, x + (edge1 % n) * a + a / 2, y + (edge1 // n) * a + a / 2,
                                     "{0}".format(RegionStep[edge1]), textsize, mazefunc.black)
                pygame.display.update()
            m -= 1
            mazefunc.systemExit()

        if stepBool == True:
            mazefunc.colorRegion(screen, x, y, n, a, Grid, edge0, mazefunc.bgrcol)
            mazefunc.textDisplay(screen, x + (edge0 % n) * a + a / 2, y + (edge0 // n) * a + a / 2,
                                 "{0}".format(RegionStep[edge0]), textsize, mazefunc.black)
            mazefunc.colorRegion(screen, x, y, n, a, Grid, edge1, mazefunc.bgrcol)
            mazefunc.textDisplay(screen, x + (edge1 % n) * a + a / 2, y + (edge1 // n) * a + a / 2,
                                 "{0}".format(RegionStep[edge1]), textsize, mazefunc.black)
            pygame.time.delay(delay // 2)

            step += 1
            speed,delay=mazefunc.mazeSpeed(n, delay, speed, step, ((0.1, 2), (0.25, 2),(0.6,2)))

    if stepBool==True:
        mazecol = (mazefunc.white, lncol, mazefunc.lgreen, mazefunc.salmon)
        mazefunc.drawGrid(screen, x, y, n, a, Grid, mazecol)
        for i in range(0, n):
            for j in range(0, n):
                mazefunc.textDisplay2(screen, x + j * a + a / 2, y + i * a + a / 2, "{0}".format(regionvalue),
                                     textsize, mazefunc.black,mazefunc.white)
        mazefunc.textDisplay2(screen, x + a / 2, y + a / 2, "{0}".format(regionvalue),
                              textsize, mazefunc.black, mazefunc.lgreen)
        mazefunc.textDisplay2(screen, x + (n - 1) * a + a / 2, y + (n - 1) * a + a / 2, "{0}".format(regionvalue),
                              textsize, mazefunc.black, mazefunc.salmon)
        mazefunc.updelay(delay*(2**(speed)))

    if delay != -1:
        mazefunc.drawGrid(screen, x, y, n, a, Grid, (mazefunc.white,mazefunc.black,mazefunc.lgreen,mazefunc.salmon))
        pygame.display.update()

    return Grid, Maze

def mazeRecbtr(screen,x,y,n,a,mazecol,delay,stepBool):
    Edges, Maze, Grid = mazefunc.mazeCreate(n)
    bgrcol=mazecol[0]
    lncol=mazecol[1]

    if stepBool==True and (delay==-1 or delay==0):
        delay=1000

    if delay!=-1:
        mazefunc.drawGrid(screen,x,y,n, a, Grid,(bgrcol,lncol,bgrcol,bgrcol))
        pygame.display.update()

    Checked=[0]
    if stepBool==True:
        mazefunc.colorRegion(screen,x,y,n,a,Grid,Checked[0],hlcol2)
        pygame.display.update()
    newVertex=0

    if stepBool == True:
        step = 1
        speed = 0
    while len(Checked)!=n**2:
        Neighbors = mazefunc.regionNeighbor(n, newVertex)
        NbrTemp = Neighbors.copy()
        for j in NbrTemp:
            if j in Checked:
                Neighbors.remove(j)
        lenNbr=len(Neighbors)
        tempChecked = [newVertex]

        while lenNbr!=0:
            if stepBool==True:
                for j in Neighbors:
                    mazefunc.colorRegion(screen,x,y,n,a,Grid,j,hlcol1)
                mazefunc.updelay(delay//2)

            randVertex = random.choice(Neighbors)
            temp=tempChecked[-1]
            Checked.append(randVertex)
            tempChecked.append(randVertex)
            Neighbors.remove(randVertex)

            edge0=min(temp,randVertex)
            edge1=max(temp, randVertex)
            Edges, Maze, Grid = mazefunc.mazeUpdate(n, Edges, Maze, Grid, edge0, edge1)

            if stepBool==True:
                mazefunc.colorRegion(screen,x,y,n,a,Grid,randVertex,hlcol2)
                pygame.display.update()

                for i in Neighbors:
                    mazefunc.colorRegion(screen,x,y,n,a,Grid,i,bgrcol)
                begincoord, endcoord = mazefunc.edgeErase(x, y, n, a, line_thickness, edge0, edge1)
                pygame.draw.line(screen, hlcol2, begincoord, endcoord, line_thickness)
                mazefunc.updelay(delay*2)
            if stepBool==False and (delay!=-1 ):
                begincoord, endcoord = mazefunc.edgeErase(x, y, n, a, line_thickness, edge0, edge1)
                pygame.draw.line(screen, bgrcol, begincoord, endcoord, line_thickness)
                mazefunc.updelay(delay * 2)


            Neighbors = mazefunc.regionNeighbor(n, randVertex)
            NbrTemp = Neighbors.copy()
            for j in NbrTemp:
                if j in Checked:
                    Neighbors.remove(j)
            lenNbr = len(Neighbors)
            if stepBool==True:
                step += 1
                speed, delay = mazefunc.mazeSpeed(n, delay, speed, step, ((0.1, 2), (0.25, 2), (0.6, 2)))
            mazefunc.systemExit()

        for j in tempChecked:
            mazefunc.colorRegion(screen,x,y,n,a,Grid,j,mazefunc.white)

        if len(Checked)!=n**2:
            i=1
            while lenNbr==0:
                newVertex=Checked[-1-i]
                newNeighbors=mazefunc.regionNeighbor(n,newVertex)
                newNbrtemp = newNeighbors.copy()
                for j in newNbrtemp:
                    if j in Checked:
                        newNeighbors.remove(j)

                lenNbr=len(newNeighbors)
                i+=1


    if delay!=-1:
        mazecol = (mazefunc.white, lncol, mazefunc.lgreen, mazefunc.salmon)
        mazefunc.drawGrid(screen,x,y,n,a,Grid,mazecol)
        pygame.display.update()
    return Grid, Maze

def mazeSidewinder(screen,x,y,n,a,mazecol,delay,stepBool):
    if stepBool==True and (delay==-1 or delay==0):
        delay=1000

    bgrcol=mazecol[0]
    lncol=mazecol[1]
    Edges, Maze, Grid = mazefunc.mazeCreate(n)
    #a = mazefunc.rectSize(scr, n, margin, titleLabel)
    if delay!=-1:
        mazefunc.drawGrid(screen, x, y, n, a, Grid, (bgrcol,lncol,bgrcol,bgrcol))
        pygame.display.update()

    #1th row
    if stepBool == True:
        for j in range(0,n):
            pygame.draw.rect(screen, hlcol1, [x + j * a, y, a + 1, a + 1], 0)
            mazefunc.drawRect(screen, x + j * a, y, a, Grid[j], hlcol1,
                              mazefunc.black)

        mazefunc.updelay(delay)
        for j in range(0, n):
            mazefunc.colorRegion(screen,x,y,n,a,Grid,j,mazefunc.white)

    for j in range(0,n-1):
        edge0 = j
        edge1 = j+1
        Edges, Maze, Grid = mazefunc.mazeUpdate(n, Edges, Maze, Grid, edge0, edge1)

        if delay!=-1 and delay!=0:
            begincoord,endcoord=mazefunc.edgeErase(x,y,n,a,line_thickness,j,j+1)
            pygame.draw.line(screen, mazefunc.white,begincoord,endcoord,line_thickness)
        mazefunc.systemExit()

    mazefunc.updelay(delay*3//2)
    #kth row, k!=1
    for j in range(1,n): #run through rows
        if j==math.floor(0.3*n):
            delay=delay//2
        if j==math.floor(0.6*n):
            delay=delay//2
        rowList=[]
        tempList=[]
        for k in range(0,n):
            randBool=bool(random.getrandbits(1))
            tempList.append(j * n + k)
            mazefunc.systemExit()
            if randBool==True:
                rowList.append(tempList)
                tempList=[]
        if tempList: #if it isn't empty
            rowList.append(tempList)

        for L in rowList:
            if stepBool == True:
                for k in L:
                    mazefunc.colorRegion(screen,x,y,n,a,Grid,k,hlcol1)
                mazefunc.updelay(delay//2)
            for m in range(0,len(L)-1):
                edge0=L[m]
                edge1=L[m]+1
                begincoord, endcoord = mazefunc.edgeErase(x, y, n, a, line_thickness, edge0, edge1)
                pygame.draw.line(screen, hlcol1, begincoord, endcoord, line_thickness)
                Edges, Maze, Grid = mazefunc.mazeUpdate(n, Edges, Maze, Grid, edge0, edge1)
                mazefunc.systemExit()
            mazefunc.updelay(delay//2)

            rand=random.randint(L[0],L[-1])
            edge2=rand-n
            edge3=rand
            if stepBool==True:
                mazefunc.colorRegion(screen, x, y, n, a, Grid, edge2, hlcol2)
                mazefunc.colorRegion(screen, x, y, n, a, Grid, edge3, hlcol2)
                mazefunc.updelay(delay//2)
                begincoord, endcoord = mazefunc.edgeErase(x, y, n, a, line_thickness, edge2, edge3)
                pygame.draw.line(screen, hlcol2, begincoord, endcoord, line_thickness)
                mazefunc.updelay(delay//2)

            Edges, Maze, Grid = mazefunc.mazeUpdate(n, Edges, Maze, Grid, edge2, edge3)

            if stepBool == True:
                for k in L:
                    mazefunc.colorRegion(screen, x, y, n, a, Grid, k, mazefunc.white)
                mazefunc.colorRegion(screen, x, y, n, a, Grid, edge2, mazefunc.white)

            if delay != -1 and delay != 0:
                for m in range(0, len(L) - 1):
                    edge0 = L[m]
                    edge1 = L[m] + 1
                    begincoord, endcoord = mazefunc.edgeErase(x, y, n, a, line_thickness, edge0, edge1)
                    pygame.draw.line(screen, mazefunc.white, begincoord, endcoord, line_thickness)

            if delay!=-1 and delay!=0:
                begincoord, endcoord = mazefunc.edgeErase(x, y, n, a, line_thickness, edge2, edge3)
                pygame.draw.line(screen, mazefunc.white, begincoord, endcoord, line_thickness)
                mazefunc.updelay(delay)


    if stepBool==True:
        mazecol=(mazefunc.white,lncol,mazefunc.lgreen,mazefunc.salmon)
    if delay!=-1:
        mazefunc.drawGrid(screen, x, y, n, a, Grid, mazecol)
        pygame.display.update()
    return Grid,Maze

def mazePrim(screen, x, y, n,a, mazecol,delay,stepBool):
    if stepBool==True and (delay==-1 or delay==0):
        delay=1000
    bgrcol=mazecol[0]
    lncol=mazecol[1]
    Edges, Maze, Grid = mazefunc.mazeCreate(n)

    if delay!=-1:
        mazefunc.drawGrid(screen, x, y, n, a, Grid,(bgrcol,lncol,bgrcol,bgrcol))
        pygame.display.update()

    start=0
    Checked = [start]
    Neighbors=mazefunc.regionNeighbor(n,Checked[0])

    if stepBool==True:
        mazefunc.colorRegion(screen,x,y,n,a,Grid,start,mbgrcol)
        for j in Neighbors:
            mazefunc.colorRegion(screen, x, y, n, a, Grid, j, hlcol1)
        mazefunc.updelay(delay)
    step=0
    speed=0
    while len(Neighbors) !=0 :
        randVertex=random.choice(Neighbors)
        NeighborsTemp = mazefunc.regionNeighbor(n, randVertex)
        flag=False
        while len(NeighborsTemp)!=0:
            j=random.choice(NeighborsTemp)
            if j in Checked and flag==False:
                edge0 = min(j,randVertex)
                edge1 = max(j, randVertex)
                flag=True
            if j not in Checked and j not in Neighbors:
                Neighbors.append(j)
            NeighborsTemp.remove(j)
        Checked.append(randVertex)
        Neighbors.remove(randVertex)
        if stepBool==True:
            mazefunc.colorRegion(screen, x, y, n, a, Grid, edge0, hlcol2)
            mazefunc.colorRegion(screen, x, y, n, a, Grid, edge1, hlcol2)
            mazefunc.updelay(delay)

        Edges, Maze, Grid = mazefunc.mazeUpdate(n, Edges, Maze, Grid, edge0, edge1)
        if stepBool == True:
            mazefunc.colorRegion(screen, x, y, n, a, Grid, edge0, mbgrcol)
            mazefunc.colorRegion(screen, x, y, n, a, Grid, edge1, mbgrcol)
            bgrcol = mbgrcol
        if delay!=-1 and delay!=0:
            begincoord, endcoord = mazefunc.edgeErase(x, y, n, a, line_thickness, edge0, edge1)
            pygame.draw.line(screen, bgrcol, begincoord, endcoord, line_thickness)
            if stepBool==True:
                bgrcol=mazecol[0]
            mazefunc.updelay(delay)
        if stepBool==True:
            for j in Neighbors:
                mazefunc.colorRegion(screen, x, y, n, a, Grid, j, hlcol1)
            mazefunc.updelay(delay)
            step += 1
            speed, delay = mazefunc.mazeSpeed(n, delay, speed, step, ((0.1, 2), (0.25, 2), (0.6, 2)))
        mazefunc.systemExit()

    if stepBool==True:
        mazecol=(mbgrcol,lncol,mazefunc.lgreen,mazefunc.salmon)
    if delay!=-1:
        mazefunc.drawGrid(screen, x, y, n, a, Grid, mazecol)
        pygame.display.update()
    return Grid, Maze

def mazeKruskalparallel(screen,x,y,n,a,mazecol,delay,Edges, Maze, Grid,VRegions,Regions,k, parBool):
    m = (2 * n * (n - 1)) - 1  # length Edges

    while len(Regions) != 1:
        randEdge = random.choice(Edges)
        edge0 = randEdge[0]
        edge1 = randEdge[1]
        i = 0
        while i <= m:
            if edge0 in Regions[i]:
                break
            else:
                i += 1
        j = 0
        while j <= m:
            if edge1 in Regions[j]:
                break
            else:
                j += 1

        if i != j:
            for l in Regions[j]:
                Regions[i].append(l)

        #remove needless edges from Edges
            #remove edges with edge0
            neighborTemp=mazefunc.regionNeighbor(n,edge0)
            neighborTemp.remove(edge1)
            for l in neighborTemp:
                if l in Regions[i] and (min(l,edge0),max(l,edge0)) in Edges:
                    Edges.remove((min(l,edge0),max(l,edge0)))
            # remove edges with edge0
            neighborTemp = mazefunc.regionNeighbor(n, edge1)
            neighborTemp.remove(edge0)
            for l in neighborTemp:
                if l in Regions[i] and (min(l, edge1), max(l, edge1)) in Edges:
                    Edges.remove((min(l, edge1), max(l, edge1)))

            Regions.remove(Regions[j])
            Edges, Maze, Grid = mazefunc.mazeUpdate(n, Edges, Maze, Grid, edge0, edge1)
            VRegions[edge0] = True
            VRegions[edge1] = True

            begincoord, endcoord = mazefunc.edgeErase(x, y, n, a, line_thickness, edge0, edge1)
            pygame.draw.line(screen, mazefunc.white, begincoord, endcoord, line_thickness)
            m -= 1
        break

    if len(Regions)==1:
        parBool=True
    for i in range(0,n**2):
        if VRegions[i] == True:
            mazefunc.colorRegion(screen,x,y,n,a,Grid,i,mazefunc.white)
    if parBool == True:
        mazefunc.drawGrid(screen, x, y, n, a, Grid, mazecol)
    mazefunc.updelay(delay)

    return Edges, Maze, Grid,VRegions,Regions,k, parBool

def mazeSidewrparallel(screen,x,y,n,a,mazecol,delay,Edges, Maze, Grid,tempList,rowList,VRegions,k, parBool):
    l=(k-1)//4
    mazefunc.colorRegion(screen,x,y,n,a,Grid,0,mazefunc.white)
    VRegions[0]=True
    #1th row
    if l<n**2:
        if l <n-1:
            edge0 = l
            edge1 = l+1
            Edges, Maze, Grid = mazefunc.mazeUpdate(n, Edges, Maze, Grid, edge0, edge1)
            VRegions[edge1]
            mazefunc.colorRegion(screen, x, y, n, a, Grid, edge1, mazefunc.white)
            begincoord,endcoord=mazefunc.edgeErase(x,y,n,a,line_thickness,l,l+1)
            pygame.draw.line(screen, mazefunc.white,begincoord,endcoord,line_thickness)
        #kth row, k!=1
        else:
            row=l//n
            if l%n !=n-1:
                while row<n:
                    column=l%n
                    mazefunc.colorRegion(screen,x,y,n,a,Grid,row*n,mazefunc.white)
                    while column <n-1:
                        if column == 0:
                            rowList = []
                            tempList = []
                            VRegions[row * n] = True
                        edge0=row*n+column
                        edge1=edge0+1
                        randBool=bool(random.getrandbits(1))
                        tempList.append(row * n + column)
                        mazefunc.colorRegion(screen, x, y, n, a, Grid, edge1, mazefunc.white)
                        VRegions[edge1] = True
                        if edge1%n==n-1:
                            tempList.append(row * n + column+1)
                            Edges, Maze, Grid = mazefunc.mazeUpdate(n, Edges, Maze, Grid, edge0, edge1)
                            begincoord, endcoord = mazefunc.edgeErase(x, y, n, a, line_thickness, edge0, edge1)
                            pygame.draw.line(screen, mazefunc.white, begincoord, endcoord, line_thickness)
                            randBool=True
                        if randBool==True:
                            rowList.append(tempList)
                            rand = random.choice(tempList)
                            edge2 = rand - n
                            edge3 = rand
                            Edges, Maze, Grid = mazefunc.mazeUpdate(n, Edges, Maze, Grid, edge2, edge3)
                            begincoord, endcoord = mazefunc.edgeErase(x, y, n, a, line_thickness, edge2, edge3)
                            pygame.draw.line(screen, mazefunc.white, begincoord, endcoord, line_thickness)
                            tempList=[]
                        else:
                            Edges, Maze, Grid = mazefunc.mazeUpdate(n, Edges, Maze, Grid, edge0, edge1)
                            begincoord, endcoord = mazefunc.edgeErase(x, y, n, a, line_thickness, edge0, edge1)
                            pygame.draw.line(screen, mazefunc.white, begincoord, endcoord, line_thickness)
                        break
                    break

    else:
        parBool=True
        mazefunc.drawGrid(screen, x, y, n, a, Grid, mazecol)
        mazefunc.updelay(delay)

    return Edges, Maze, Grid,rowList,tempList,VRegions,k, parBool

def mazeRecbtrparallel(screen,x,y,n,a,mazecol,delay,Edges, Maze, Grid,VRegions,Checked,newVertex,k,parBool):
    VRegions[0]=True
    while len(Checked)!=n**2:
        Neighbors = mazefunc.regionNeighbor(n, newVertex)
        NbrTemp = Neighbors.copy()
        for j in NbrTemp:
            if j in Checked:
                Neighbors.remove(j)
        lenNbr=len(Neighbors)
        tempChecked = [newVertex]

        while lenNbr!=0:
            randVertex = random.choice(Neighbors)
            temp=tempChecked[-1] #last visited
            Checked.append(randVertex)
            tempChecked.append(randVertex)
            Neighbors.remove(randVertex)
            edge0=min(temp,randVertex)
            edge1=max(temp, randVertex)
            Edges, Maze, Grid = mazefunc.mazeUpdate(n, Edges, Maze, Grid, edge0, edge1)
            VRegions[randVertex]=True
            Neighbors = mazefunc.regionNeighbor(n, randVertex)
            NbrTemp = Neighbors.copy()
            for j in NbrTemp:
                if j in Checked:
                    Neighbors.remove(j)
            lenNbr = len(Neighbors)
            newVertex=randVertex
            break

        if len(Checked)!=n**2:
            i=1
            while lenNbr==0:
                newVertex=Checked[-1-i]
                newNeighbors=mazefunc.regionNeighbor(n,newVertex)
                newNbrtemp = newNeighbors.copy()
                for j in newNbrtemp:
                    if j in Checked:
                        newNeighbors.remove(j)

                lenNbr=len(newNeighbors)
                i+=1
        break

    if len(Checked)==n**2:
        parBool=True
    for i in range(0,n**2):
        if VRegions[i] == True:
            mazefunc.colorRegion(screen,x,y,n,a,Grid,i,mazefunc.white)
    if parBool == True:
        mazefunc.drawGrid(screen, x, y, n, a, Grid, mazecol)
    mazefunc.updelay(delay)

    return Edges, Maze, Grid,VRegions,Checked,newVertex,k, parBool

def mazePrimparallel(screen, x, y, n,a, mazecol,delay,Edges, Maze, Grid, VRegions, Checked,Neighbors ,k, parBool):
    VRegions[0]=True
    while len(Neighbors) !=0 :
        randVertex=random.choice(Neighbors)
        NeighborsTemp = mazefunc.regionNeighbor(n, randVertex)
        flag=False
        while len(NeighborsTemp)!=0:
            j=random.choice(NeighborsTemp)
            if j in Checked and flag==False:
                edge0 = min(j,randVertex)
                edge1 = max(j, randVertex)
                flag=True
            if j not in Checked and j not in Neighbors:
                Neighbors.append(j)
            NeighborsTemp.remove(j)
        Checked.append(randVertex)
        Neighbors.remove(randVertex)
        VRegions[randVertex]=True
        mazefunc.regionNeighbor(n,randVertex)
        Edges, Maze, Grid = mazefunc.mazeUpdate(n, Edges, Maze, Grid, edge0, edge1)
        begincoord, endcoord = mazefunc.edgeErase(x, y, n, a, line_thickness, edge0, edge1)
        pygame.draw.line(screen, mazefunc.white, begincoord, endcoord, line_thickness)
        break

    if len(Neighbors)==0:
        parBool=True
    for i in range(0,n**2):
        if VRegions[i] == True:
            mazefunc.colorRegion(screen,x,y,n,a,Grid,i,mazefunc.white)
    if parBool == True:
        mazefunc.drawGrid(screen, x, y, n, a, Grid, mazecol)
    mazefunc.updelay(delay)

    return Edges, Maze, Grid,VRegions,Checked,Neighbors,k, parBool

def mazeKruskalhex(screen,x,y,n,a,mazecol,delay,stepBool):
    textsize=math.floor(a*1.2)
    #x,y=mazefunc.mazeHexposition(x,y,n,a)
    boolNumbers=False
    if stepBool==True and (delay==-1 or delay==0):
        delay=1000

    Hexagonal = mazefunc.regionHexgen(n)
    Edges, Maze, Grid = mazefunc.mazeHexcreate(n,Hexagonal)
    Regions = [[i] for i in range(0, 6 * (n * (n - 1) // 2) - 1)]

    if delay!=-1:
        mazefunc.drawHexgrid(screen,x,y,n, a, Grid,mazefunc.dgrey,mazefunc.black)
        mazefunc.updelay(delay)
    if stepBool==True and boolNumbers==True:
        m = n
        p = 1
        q = 0
        for i in range(0, 2 * n - 1):
            for j in range(0, m):
                mazefunc.textDisplay2(screen, x - m * (a * math.cos(math.pi / 6)) + j * (2 * a * math.cos(math.pi / 6)) + (
                            a * math.cos(math.pi / 6)), y + i * (a + a * math.sin(math.pi / 6)) + a // 2,
                             '{0}'.format(q), 20, mazefunc.black, mazefunc.dgrey)
                q += 1
            if m == 2 * n - 1:
                p = -p
            m += p
        mazefunc.updelay(delay)

    step = 1
    speed = 0
    while len(Regions) != 1:
        randEdge = random.choice(Edges)
        edge0 = randEdge[0]
        edge1 = randEdge[1]
        i=0
        for t in Regions:
            if edge0 in t:
                i=Regions.index(t)
                break

        j=0
        for t in Regions:
            if edge1 in t:
                j=Regions.index(t)
                break

        if stepBool:
            mazefunc.colorHexregion(screen,x,y,n,a,Grid,Hexagonal,edge0,hlcol1)
            row,column,m=mazefunc.hexRegposition(n,Hexagonal,edge0)
            if boolNumbers==True:
                mazefunc.textDisplay2(screen, x - m * (a * math.cos(math.pi / 6)) + column * (2 * a * math.cos(math.pi / 6)) + (
                            a * math.cos(math.pi / 6)), y + row * (a + a * math.sin(math.pi / 6)) + a // 2, '{0}'.format(edge0),
                             textsize, mazefunc.black, mazefunc.lred)

            mazefunc.colorHexregion(screen,x,y,n,a,Grid,Hexagonal,edge1,hlcol1)
            row, column, m = mazefunc.hexRegposition(n, Hexagonal, edge1)
            if boolNumbers==True:
                mazefunc.textDisplay2(screen,
                                      x - m * (a * math.cos(math.pi / 6)) + column * (2 * a * math.cos(math.pi / 6)) + (
                                              a * math.cos(math.pi / 6)),
                                      y + row * (a + a * math.sin(math.pi / 6)) + a // 2, '{0}'.format(edge1),
                                      textsize, mazefunc.black, mazefunc.lred)

            mazefunc.updelay(delay)

        if i != j:
            for k in range(0, len(Regions[j])):
                Regions[i].append(Regions[j][k])
                Neighbors = mazefunc.regionNeighborHex(n,Hexagonal ,Regions[j][k])  # check neighbors of vertex k
                for l in Neighbors:
                    edge = (min(Regions[j][k], l), max(Regions[j][k], l))
                    if l in Regions[i] and edge in Edges and edge != randEdge:
                        Edges.remove(edge)

            regionvalue = min(Regions[i])
            if stepBool == True:
                for l in Regions[i]:
                    mazefunc.colorHexregion(screen, x, y, n, a, Grid, Hexagonal, l, mazefunc.white)
                    if boolNumbers==True:
                        row, column, m = mazefunc.hexRegposition(n, Hexagonal, l)
                        mazefunc.textDisplay(screen,
                                              x - m * (a * math.cos(math.pi / 6)) + column * (
                                                          2 * a * math.cos(math.pi / 6)) + (
                                                      a * math.cos(math.pi / 6)),
                                              y + row * (a + a * math.sin(math.pi / 6)) + a // 2, '{0}'.format(regionvalue),
                                              textsize, mazefunc.black)


            Regions.remove(Regions[j])
            Edges, Maze, Grid = mazefunc.mazeHexupdate(n, Edges, Maze, Grid,Hexagonal, edge0, edge1)

            row0,column0,m0=mazefunc.hexRegposition(n,Hexagonal,edge0)
            row1, column1, m1 = mazefunc.hexRegposition(n, Hexagonal, edge1)

            x0 = x - m0 * (a * math.cos(math.pi / 6)) + column0 * (2 * a * math.cos(math.pi / 6))
            y0 = y + row0 * (a + a * math.sin(math.pi / 6))
            x1 = x - m1 * (a * math.cos(math.pi / 6)) + column1 * (2 * a * math.cos(math.pi / 6))
            y1 = y + row1 * (a + a * math.sin(math.pi / 6))

            mazefunc.drawHex(screen,x0,y0,a,Grid[edge0],mazefunc.white,mazefunc.black)
            mazefunc.drawHex(screen, x1, y1,a,Grid[edge1], mazefunc.white, mazefunc.black)
            if boolNumbers==True:
                mazefunc.textDisplay(screen,
                                     x - m0 * (a * math.cos(math.pi / 6)) + column0 * (
                                             2 * a * math.cos(math.pi / 6)) + (
                                             a * math.cos(math.pi / 6)),
                                     y + row0 * (a + a * math.sin(math.pi / 6)) + a // 2, '{0}'.format(regionvalue),
                                     textsize, mazefunc.black)
                mazefunc.textDisplay(screen,
                                     x - m1 * (a * math.cos(math.pi / 6)) + column1 * (
                                             2 * a * math.cos(math.pi / 6)) + (
                                             a * math.cos(math.pi / 6)),
                                     y + row1 * (a + a * math.sin(math.pi / 6)) + a // 2, '{0}'.format(regionvalue),
                                     textsize, mazefunc.black)
            #mazefunc.updelay(delay)
            pygame.display.update()
        else:
            regionvalue = min(Regions[i])
            mazefunc.colorHexregion(screen, x, y, n, a, Grid, Hexagonal, edge0, mazefunc.white)
            if boolNumbers==True:
                row, column, m = mazefunc.hexRegposition(n, Hexagonal, edge0)
                mazefunc.textDisplay2(screen,
                                      x - m * (a * math.cos(math.pi / 6)) + column * (2 * a * math.cos(math.pi / 6)) + (
                                              a * math.cos(math.pi / 6)),
                                      y + row * (a + a * math.sin(math.pi / 6)) + a // 2, '{0}'.format(regionvalue),
                                      textsize, mazefunc.black, mazefunc.white)

            mazefunc.colorHexregion(screen, x, y, n, a, Grid, Hexagonal, edge1, mazefunc.white)
            if boolNumbers==True:
                row, column, m = mazefunc.hexRegposition(n, Hexagonal, edge1)
                mazefunc.textDisplay2(screen,
                                      x - m * (a * math.cos(math.pi / 6)) + column * (2 * a * math.cos(math.pi / 6)) + (
                                              a * math.cos(math.pi / 6)),
                                      y + row * (a + a * math.sin(math.pi / 6)) + a // 2, '{0}'.format(regionvalue),
                                      textsize, mazefunc.black, mazefunc.white)
            #mazefunc.updelay(delay)

        step += 1
        speed,delay=mazefunc.mazeSpeed(n, delay, speed, step, ((0.1, 2), (0.25, 2),(0.6,2)))
        mazefunc.systemExit()

    start=(n+2*(n-1))*(n-1)//2
    finish=((n+2*n-1)*n)//2-1
    mazefunc.drawHexgrid(screen,x,y,n,a,Grid,mazefunc.white,mazefunc.black)
    mazefunc.colorHexregion(screen,x,y,n,a,Grid,Hexagonal,start,mazefunc.lgreen)
    mazefunc.colorHexregion(screen, x, y, n, a, Grid, Hexagonal, finish, mazefunc.salmon)
    pygame.display.update()

    return Grid, Maze,Hexagonal
'''