import math,pygame, random
import maze_functions

from Settings import maze as maze_settings
from Settings import screen as screen_settings
from Settings import colors

n = maze_settings.n
screen = screen_settings.screen_size
labelsize = screen_settings.labelsize
marginsize = screen_settings.marginsize

a = maze_settings.a            #size of edge of rectengular
loc = ((screen[0]/2-n*a)/2,labelsize)
line_thickness = screen_settings.line_thickness   #line thichness
x=100
y=50

#Screen size
#gameDisplay = pygame.display.set_mode(screen)
#pygame.display.set_caption('Maze Generator')
#gameDisplay.fill(colors.white)

#Grid,Maze=mazealg.mazeRecbtr(gameDisplay,x,y,n,a,colors.white,colors.black,0)
#pygame.time.delay(1500)


# A* algorithm
# element (current, maze_functions.distance, origin)
def solveAstar(screen,x,y,Maze,Grid,n,a,delay,stepBool):
    s = 0  # start
    e = n**2-1  # end
    Finished = [(s, maze_functions.distance(s,n), -1)]  # finished
    Checked = []  # check

    speed=0; step=0
    while Finished[-1][0] != e:
        for m in Maze:
            if m[0] == Finished[-1][0] and m[1] != Finished[-1][2]:
                Checked.append((m[1], maze_functions.distance(m[1],n) + 1, m[0]))
            elif m[1] == Finished[-1][0] and m[0] != Finished[-1][2]:
                Checked.append((m[0], maze_functions.distance(m[0],n) + 1, m[1]))

        Checked.sort(key=lambda tup: tup[1])

        if stepBool==True:
            for i in Checked:
                maze_functions.colorRegion(screen,x,y,n,a,Grid,i[0],colors.lred)
                maze_functions.textDisplay2(screen,x+(i[0]%n)*a+a/2,y+(i[0]//n)*a+a/2,'{0}'.format(i[1]),20,colors.black,colors.lred)
            maze_functions.updelay(delay)

            maze_functions.colorRegion(screen, x, y, n, a, Grid, Checked[0][0], colors.mred)
            maze_functions.colorRegion(screen, x, y, n, a, Grid, Checked[0][2], colors.mred)
            maze_functions.updelay(delay)


        if delay!=-1:
            maze_functions.colorRegion(screen, x, y, n, a, Grid, Checked[0][0], colors.lyellow)
            if Checked[0][2] != 0:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, Checked[0][2], colors.lyellow)
            else:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, Checked[0][2], colors.lgreen)
            if Checked[0][0] == n**2-1:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, Checked[0][0], colors.salmon)
            maze_functions.updelay(delay)

        for f in Finished:
            if f[0] == Checked[0][0] and f[1] > Checked[0][1]:
                Finished.remove(f)

        if Checked[0][0]!=n**2-1 and delay!=-1:
            maze_functions.colorRegion(screen, x, y, n, a, Grid, Checked[0][0], colors.lyellow)
            pygame.display.update()
        pygame.time.delay(delay)
        Finished.append(Checked[0])
        Checked.remove(Checked[0])
        step+=1
        speed, delay = maze_functions.mazeSpeed(n, delay, speed, step, ((0.1, 2), (0.25, 2), (0.6, 2)))
        maze_functions.systemExit()

    Shortest = [Finished[-1][0]]  # Solution
    while Shortest[-1] != s:
        i = -1
        while Finished[i][0] != Shortest[-1]:
            i -= 1
        Shortest.append(Finished[i][2])
        Finished.remove(Finished[i])

    for i in range(len(Shortest)-2,0,-1):
        maze_functions.colorRegion(screen,x,y,n,a,Grid,Shortest[i],colors.lblue)
        if delay!=-1:
            maze_functions.updelay(delay//2)
        else:
            maze_functions.updelay(75)

    pygame.display.update()
    return Shortest, Finished

def solveWallflw(screen,x,y,Maze,Grid,n,a,delay,stepBool):
    s = 0  # start
    e = n ** 2 - 1  # end
    Finished = [(s,-1)]  # finished
    FinishedElements=[s]
    step=0
    speed=0
    while Finished[-1][0]!=e:
        i=0
        flag=False
        while flag!=True:
            vertex=Finished[-1-i]
            Neighbors=maze_functions.regionNeighbor(n,vertex[0])
            Neighbors.append(-1)
            j=0
            while Neighbors[j]!=-1:
                edge=(min(vertex[0],Neighbors[j]),max(vertex[0],Neighbors[j]))
                if Neighbors[j] in FinishedElements or edge not in Maze:
                    Neighbors.remove(Neighbors[j])
                else:
                    j+=1
            Neighbors.remove(-1)

            if len(Neighbors)!=0:
                flag=True
                i=0
            else:
                if i == 0:
                    pygame.time.delay(delay*2)
                i += 1

        if stepBool == True:
            for j in Neighbors:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, j, colors.lred)
            maze_functions.updelay(delay)

        nextVertex=maze_functions.leftMove(n,vertex,Neighbors)
        if stepBool==True:
            maze_functions.colorRegion(screen, x, y, n, a, Grid, vertex[0], colors.mred)
            maze_functions.colorRegion(screen,x,y,n,a,Grid,nextVertex,colors.mred)
            maze_functions.updelay(delay)
            if vertex[0]!=0:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, vertex[0], colors.lyellow)
            else:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, vertex[0], colors.lgreen)
            if nextVertex!=e:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, nextVertex, colors.lyellow)
            else:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, nextVertex, colors.salmon)
            Neighbors.remove(nextVertex)
            for j in Neighbors:
                if j!=n**2-1:
                    maze_functions.colorRegion(screen,x,y,n,a,Grid,j,colors.white)
                else:
                    maze_functions.colorRegion(screen, x, y, n, a, Grid, j, colors.salmon)
        Finished.append((nextVertex,vertex[0]))
        FinishedElements.append(nextVertex)
        step += 1
        speed, delay = maze_functions.mazeSpeed(n, delay, speed, step, ((0.1, 2), (0.25, 2), (0.6, 2)))
        maze_functions.systemExit()

    Shortest = [Finished[-1][0]]  # Solution
    while Shortest[-1] != s:
        i = -1
        while Finished[i][0] != Shortest[-1]:
            i -= 1
        Shortest.append(Finished[i][1])
        Finished.remove(Finished[i])

    for i in range(len(Shortest) - 2, 0, -1):
        maze_functions.colorRegion(screen,x,y,n,a,Grid,Shortest[i],colors.lblue)
        pygame.display.update()
        pygame.time.delay(delay)
    return Shortest, Finished

def solveTremaux(screen,x,y,Maze,Grid,n,a,delay,stepBool):
    start = 0
    finish = n ** 2 - 1
    current = start
    Finished = []
    Deadend=[]
    tempChecked = [start]
    step=0
    speed=0
    while current != finish:
        temp = current
        Neighbors = maze_functions.regionNeighbor(n, temp)
        Neighbors.append(-1)
        j=0
        while Neighbors[j]!=-1:
            vertex=Neighbors[j]
            edge = (min(temp, vertex), max(temp, vertex))
            if vertex in tempChecked or vertex in Finished or edge not in Maze:
                Neighbors.remove(vertex)
            else:
                j+=1
        Neighbors.remove(Neighbors[-1])
        if bool(Neighbors) == False:
            for j in range(1, len(tempChecked)):
                Finished.append(tempChecked[j])
            pygame.display.update()
            tempChecked=[]
            while bool(Neighbors) == False:  # is empty
                temp = Finished[-1]
                Neighbors = maze_functions.regionNeighbor(n, temp)
                Neighbors.append(-1)
                j = 0
                while Neighbors[j]!= -1:
                    vertex = Neighbors[j]
                    edge = (min(temp, vertex), max(temp, vertex))
                    if vertex in tempChecked or vertex in Finished or vertex in Deadend or edge not in Maze:
                        Neighbors.remove(vertex)
                    else:
                        j += 1
                Neighbors.remove(Neighbors[-1])
                if bool(Neighbors)==False:
                    Deadend.append(temp)
                    Finished.remove(temp)
                    maze_functions.colorRegion(screen, x, y, n, a, Grid, temp, colors.dgrey)
            maze_functions.updelay(delay)

        if stepBool==True:
            for j in Neighbors:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, j,colors.lred)
            maze_functions.updelay(delay//2)
        nextVertex = random.choice(Neighbors)
        Neighbors.remove(nextVertex)
        if stepBool==True:
            maze_functions.colorRegion(screen, x, y, n, a, Grid, nextVertex, colors.mred)
            maze_functions.colorRegion(screen, x, y, n, a, Grid, temp, colors.mred)
            maze_functions.updelay(delay//2)
            if bool(Neighbors)==True:
                for j in Neighbors:
                    maze_functions.colorRegion(screen, x, y, n, a, Grid, j, colors.white)

            edge=(min(temp,nextVertex),max(temp,nextVertex))
            if 0 in edge:
                if edge[0]==0:
                    maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[0], colors.lgreen)
                    if edge[1] in Finished or edge[1] in Deadend:
                        maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[1], colors.dgrey)
                    else:
                        maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[1], colors.lyellow)
                else:
                    maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[1], colors.lgreen)
                    if edge[0] in Finished or edge[0] in Deadend:
                        maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[1], colors.dgrey)
                    else:
                        maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[1], colors.lyellow)

            else:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, temp, colors.lyellow)
            if n**2-1 in edge:
                if edge[0]==n**2-1:
                    maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[0], colors.salmon)
                    maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[1], colors.lyellow)
                else:
                    maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[1], colors.salmon)
                    maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[0], colors.lyellow)
            maze_functions.colorRegion(screen,x,y,n,a,Grid,0,colors.lgreen)
            maze_functions.updelay(delay//2)

        if temp!=current:
            tempChecked.append(temp)
        tempChecked.append(nextVertex)
        current = nextVertex

        step += 1
        speed, delay = maze_functions.mazeSpeed(n, delay, speed, step, ((0.1, 2), (0.35, 2), (0.7, 2)))
        maze_functions.systemExit()

    for j in range(1, len(tempChecked)):
        Finished.append(tempChecked[j])

    Finished.remove(n ** 2 - 1)
    for i in Finished:
        maze_functions.colorRegion(screen, x, y, n, a, Grid, i, colors.lblue)
        maze_functions.updelay(delay)

    Shortest=Finished
    Finished=Finished+Deadend
    return Shortest, Finished

def solveDeadend(screen,x,y,Maze,Grid,n,a,delay,stepBool):
    Deadend,Branch=maze_functions.mazeDeadend(n,Maze)
    Visited=[]
    if stepBool==True:
        for j in Deadend:
            maze_functions.colorRegion(screen,x,y,n,a,Grid,j,colors.lred)
            maze_functions.updelay(delay//4)
        maze_functions.updelay(4*delay)
    step=0
    speed=0
    for j in Deadend:
        if stepBool==True:
            maze_functions.colorRegion(screen, x, y, n, a, Grid, j, colors.mred)
            maze_functions.updelay(2*delay)
            maze_functions.colorRegion(screen, x, y, n, a, Grid, j, colors.dgrey)
            maze_functions.updelay(delay)
        endFill = maze_functions.mazeEndfiller(n, Maze, Visited, j)
        for k in endFill:
            Visited.append(k)
            if stepBool==True:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, k, colors.dgrey)
                maze_functions.updelay(delay)
            step += 1
            speed, delay = maze_functions.mazeSpeed(n, delay, speed, step, ((0.1, 2), (0.25, 2), (0.6, 2)))
            maze_functions.systemExit()

    notVisited=[]
    for i in range(1,n**2):
        if i not in Visited:
            notVisited.append(i)

    s=0
    Neigbors=maze_functions.regionNeighbor(n,s)
    for j in Neigbors:
        if j in notVisited:
            nextVertex=j
            maze_functions.colorRegion(screen,x,y,n,a,Grid,nextVertex,colors.lblue)
            maze_functions.updelay(100)
            maze_functions.systemExit()
            break


    edge=(0,nextVertex)

    Finished = maze_functions.uniq(Visited)
    Shortest = [0]

    while edge[1]!=n**2-1:
        Neigbors = maze_functions.regionNeighbor(n, nextVertex)
        for j in Neigbors:
            tempEdge=(min(j,nextVertex),max(j,nextVertex))
            if j in notVisited and tempEdge in Maze and tempEdge!=edge:
                edge=(min(j,nextVertex),max(j,nextVertex))
                nextVertex = j
                if nextVertex!=n**2-1:
                    Shortest.append(nextVertex)
                    maze_functions.colorRegion(screen, x, y, n, a, Grid, nextVertex, colors.lblue)
                    maze_functions.updelay(delay)
                break

    return Shortest,Finished

def solveAstarparallel(screen,x,y,Maze,Grid,n,a,delay,Checked,Finished,Shortest,parBool):
    s = 0  # start
    e = n**2-1  # end
    while Finished[-1][0] != e:
        for m in Maze:
            if m[0] == Finished[-1][0] and m[1] != Finished[-1][2]:
                Checked.append((m[1], maze_functions.distance(m[1],n) + 1, m[0]))
            elif m[1] == Finished[-1][0] and m[0] != Finished[-1][2]:
                Checked.append((m[0], maze_functions.distance(m[0],n) + 1, m[1]))

        Checked.sort(key=lambda tup: tup[1])

        maze_functions.colorRegion(screen, x, y, n, a, Grid, Checked[0][0], colors.lyellow)
        maze_functions.colorRegion(screen, x, y, n, a, Grid, Checked[0][2], colors.lyellow)
        if s in Checked[0] or e in Checked[0]:
            maze_functions.colorRegion(screen, x, y, n, a, Grid, s, colors.lgreen)
            maze_functions.colorRegion(screen, x, y, n, a, Grid, e, colors.salmon)
        maze_functions.updelay(delay)

        for f in Finished:
            if f[0] == Checked[0][0] and f[1] > Checked[0][1]:
                Finished.remove(f)

        if Checked[0][0]!=n**2-1 and delay!=-1:
            maze_functions.colorRegion(screen, x, y, n, a, Grid, Checked[0][0], colors.lyellow)
            pygame.display.update()
        pygame.time.delay(delay)
        Finished.append(Checked[0])
        Checked.remove(Checked[0])
        break

    if Finished[-1][0] == e:
        FinishedTemp=Finished.copy()
        if bool(Shortest)==False:
            Shortest = [Finished[-1][0]]
            while Shortest[-1] != s:
                i = -1
                while Finished[i][0] != Shortest[-1]:
                    i -= 1
                Shortest.append(Finished[i][2])
                Finished.remove(Finished[i])
            Shortest.reverse()
            Shortest.remove(Shortest[0])
            Shortest.remove(Shortest[-1])
            Finished=FinishedTemp
        while bool(Shortest)==True:
            maze_functions.colorRegion(screen, x, y, n, a, Grid, Shortest[0], colors.lblue)
            Shortest.remove(Shortest[0])
            maze_functions.updelay(delay)
            break
        if bool(Shortest)==False:
            parBool=True

    return Checked, Finished,Shortest ,parBool

def solveWallflwparallel(screen,x,y,Maze,Grid,n,a,delay,Finished,FinishedElements,Shortest,parBool):
    s = 0  # start
    e = n ** 2 - 1  # end
    while Finished[-1][0]!=e:
        i=0
        flag=False
        while flag!=True:
            vertex=Finished[-1-i]
            Neighbors=maze_functions.regionNeighbor(n,vertex[0])
            Neighbors.append(-1)
            j=0
            while Neighbors[j]!=-1:
                edge=(min(vertex[0],Neighbors[j]),max(vertex[0],Neighbors[j]))
                if Neighbors[j] in FinishedElements or edge not in Maze:
                    Neighbors.remove(Neighbors[j])
                else:
                    j+=1
            Neighbors.remove(-1)

            if len(Neighbors)!=0:
                flag=True
                i=0
            else:
                if i == 0:
                    pygame.time.delay(delay*2)
                i += 1

        nextVertex=maze_functions.leftMove(n,vertex,Neighbors)

        if vertex[0]!=0:
            maze_functions.colorRegion(screen, x, y, n, a, Grid, vertex[0], colors.lyellow)
        else:
            maze_functions.colorRegion(screen, x, y, n, a, Grid, vertex[0], colors.lgreen)
        if nextVertex!=e:
            maze_functions.colorRegion(screen, x, y, n, a, Grid, nextVertex, colors.lyellow)
        else:
            maze_functions.colorRegion(screen, x, y, n, a, Grid, nextVertex, colors.salmon)
        Finished.append((nextVertex,vertex[0]))
        FinishedElements.append(nextVertex)
        maze_functions.updelay(delay)
        break

    if Finished[-1][0] == e:
        FinishedTemp=Finished.copy()
        if bool(Shortest)==False:
            Shortest = [Finished[-1][0]]
            while Shortest[-1] != s:
                i = -1
                while Finished[i][0] != Shortest[-1]:
                    i -= 1
                Shortest.append(Finished[i][1])
                Finished.remove(Finished[i])
            Shortest.reverse()
            Shortest.remove(Shortest[0])
            Shortest.remove(Shortest[-1])
            Finished=FinishedTemp
        while bool(Shortest)==True:
            maze_functions.colorRegion(screen, x, y, n, a, Grid, Shortest[0], colors.lblue)
            Shortest.remove(Shortest[0])
            maze_functions.updelay(delay)
            break
        if bool(Shortest)==False:
            parBool=True

    return Finished,FinishedElements,Shortest,parBool

def solveTremauxparrallel(screen,x,y,Maze,Grid,n,a,delay,Finished,Shortest,Deadend,current,tempChecked,parBool):
    start = 0
    finish = n ** 2 - 1

    while current != finish:
        temp = current
        Neighbors = maze_functions.regionNeighbor(n, temp)
        Neighbors.append(-1)
        j=0
        while Neighbors[j]!=-1:
            vertex=Neighbors[j]
            edge = (min(temp, vertex), max(temp, vertex))
            if vertex in tempChecked or vertex in Finished or edge not in Maze:
                Neighbors.remove(vertex)
            else:
                j+=1
        Neighbors.remove(Neighbors[-1])
        if bool(Neighbors) == False:
            for j in range(1, len(tempChecked)):
                Finished.append(tempChecked[j])
            pygame.display.update()
            tempChecked=[]
            while bool(Neighbors) == False:  # is empty
                temp = Finished[-1]
                Neighbors = maze_functions.regionNeighbor(n, temp)
                Neighbors.append(-1)
                j = 0
                while Neighbors[j]!= -1:
                    vertex = Neighbors[j]
                    edge = (min(temp, vertex), max(temp, vertex))
                    if vertex in tempChecked or vertex in Finished or vertex in Deadend or edge not in Maze:
                        Neighbors.remove(vertex)
                    else:
                        j += 1
                Neighbors.remove(Neighbors[-1])
                if bool(Neighbors)==False:
                    Deadend.append(temp)
                    Finished.remove(temp)
                    maze_functions.colorRegion(screen, x, y, n, a, Grid, temp, colors.dgrey)
            maze_functions.updelay(delay)

        nextVertex = random.choice(Neighbors)
        Neighbors.remove(nextVertex)

        edge=(min(temp,nextVertex),max(temp,nextVertex))
        if 0 in edge:
            if edge[0]==0:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[0], colors.lgreen)
                if edge[1] in Finished or edge[1] in Deadend:
                    maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[1], colors.dgrey)
                else:
                    maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[1], colors.lyellow)
            else:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[1], colors.lgreen)
                if edge[0] in Finished or edge[0] in Deadend:
                    maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[1], colors.dgrey)
                else:
                    maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[1], colors.lyellow)

        else:
            maze_functions.colorRegion(screen, x, y, n, a, Grid, temp, colors.lyellow)
        if n**2-1 in edge:
            if edge[0]==n**2-1:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[0], colors.salmon)
                maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[1], colors.lyellow)
            else:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[1], colors.salmon)
                maze_functions.colorRegion(screen, x, y, n, a, Grid, edge[0], colors.lyellow)
        maze_functions.colorRegion(screen,x,y,n,a,Grid,0,colors.lgreen)
        maze_functions.updelay(delay)

        if temp!=current:
            tempChecked.append(temp)
        tempChecked.append(nextVertex)
        current = nextVertex
        break

    if current == finish:
        if bool(tempChecked)==True:
            for j in range(1, len(tempChecked)):
                Finished.append(tempChecked[j])
            tempChecked=[]
            Finished.remove(n ** 2 - 1)

        while bool(Finished)==True:
            maze_functions.colorRegion(screen, x, y, n, a, Grid, Finished[0], colors.lblue)
            maze_functions.updelay(delay)
            Finished.remove(Finished[0])

            if bool(Finished)==False:
                parBool=True
            break

        Shortest=Finished
        #Finished=Finished+Deadend
    return Finished,Shortest,Deadend,current,tempChecked,parBool

def solveDeadendparallel(screen,x,y,Maze,Grid,n,a,delay,Visited,Shortest,Deadend,endFill,parBool):
    while bool(Deadend)==True:
        if bool(endFill)==False and bool(Deadend)==True:
            endFill = maze_functions.mazeEndfiller(n, Maze, Visited, Deadend[0])

        while bool(endFill) == True:
            Visited.append(endFill[0])
            maze_functions.colorRegion(screen, x, y, n, a, Grid, endFill[0], colors.dgrey)
            maze_functions.updelay(delay)
            endFill.remove(endFill[0])
            break
        if bool(endFill)==False:
            Deadend.remove(Deadend[0])
        break

    if bool(Deadend)==False:
        if bool(Shortest)==False:
            Shortest.append(0)
            Visited.append(0)
        while Shortest[-1]!=n**2-1:
            vertex=Shortest[-1]
            Neighbor=maze_functions.regionNeighbor(n,vertex)
            Neighbor.append(-1)
            j=0
            while Neighbor[j]!=-1:
                edge=(min(vertex,Neighbor[j]),max(vertex,Neighbor[j]))
                if edge not in Maze or Neighbor[j] in Visited:
                    Neighbor.remove(Neighbor[j])
                else:
                    j+=1
            nextVertex=Neighbor[0]
            if nextVertex!=n**2-1:
                maze_functions.colorRegion(screen, x, y, n, a, Grid, nextVertex, colors.lblue)
                maze_functions.updelay(delay)
                Shortest.append(nextVertex)
                Visited.append(nextVertex)
                break
            else:
                parBool=True
                break

    return Visited,Shortest,Deadend,endFill,parBool

def solveAstarhex(screen,x,y,Maze,Grid,Hexagonal,n,a,delay,stepBool):
    start = (n + 2 * (n - 1)) * (n - 1) // 2
    finish = ((n + 2 * n - 1) * n) // 2 - 1
    Finished = [(start, maze_functions.hexDistance(n,Hexagonal,start), -1)]  # finished
    Checked = []  # check

    speed=0; step=0
    while Finished[-1][0] != finish:
        for m in Maze:
            if m[0] == Finished[-1][0] and m[1] != Finished[-1][2]:
                Checked.append((m[1], maze_functions.hexDistance(n,Hexagonal,m[1]), m[0]))
            elif m[1] == Finished[-1][0] and m[0] != Finished[-1][2]:
                Checked.append((m[0], maze_functions.hexDistance(n,Hexagonal,m[0]), m[1]))

        Checked.sort(key=lambda tup: tup[1])

        if stepBool==True:
            for i in Checked:
                maze_functions.colorHexregion(screen,x,y,n,a,Grid,Hexagonal,i[0],colors.lred)
                row, column, m = maze_functions.hexRegposition(n, Hexagonal, i[0])
                maze_functions.textDisplay2(screen,
                                      x - m * (a * math.cos(math.pi / 6)) + column * (2 * a * math.cos(math.pi / 6)) + (
                                              a * math.cos(math.pi / 6)),
                                      y + row * (a + a * math.sin(math.pi / 6)) + a // 2, '{0}'.format('{0}'.format(i[1])),
                                      math.ceil(a * 0.85), colors.black, colors.lred)
            maze_functions.updelay(delay)
            maze_functions.colorHexregion(screen, x, y, n, a, Grid, Hexagonal, Checked[0][0], colors.mred)
            maze_functions.colorHexregion(screen, x, y, n, a, Grid, Hexagonal, Checked[0][2], colors.mred)
            maze_functions.updelay(delay)


        if delay!=-1:
            maze_functions.colorHexregion(screen, x, y, n, a, Grid, Hexagonal, Checked[0][0], colors.lyellow)
            if Checked[0][2] != start:
                maze_functions.colorHexregion(screen, x, y, n, a, Grid, Hexagonal, Checked[0][2], colors.lyellow)
            else:
                maze_functions.colorHexregion(screen, x, y, n, a, Grid, Hexagonal, Checked[0][2], colors.lgreen)
            if Checked[0][0] == finish:
                maze_functions.colorHexregion(screen, x, y, n, a, Grid, Hexagonal, Checked[0][0], colors.salmon)
            maze_functions.updelay(delay)

        for f in Finished:
            if f[0] == Checked[0][0] and f[1] > Checked[0][1]:
                Finished.remove(f)

        if Checked[0][0]!=finish and delay!=-1:
            maze_functions.colorHexregion(screen, x, y, n, a, Grid, Hexagonal, Checked[0][0], colors.lyellow)
        pygame.time.delay(delay)
        Finished.append(Checked[0])
        Checked.remove(Checked[0])
        step+=1
        speed, delay = maze_functions.mazeSpeed(n, delay, speed, step, ((0.1, 2), (0.25, 2), (0.6, 2)))
        maze_functions.systemExit()

    Shortest = [Finished[-1][0]]  # Solution
    while Shortest[-1] != start:
        i = -1
        while Finished[i][0] != Shortest[-1]:
            i -= 1
        Shortest.append(Finished[i][2])
        Finished.remove(Finished[i])

    for i in range(len(Shortest)-2,0,-1):
        maze_functions.colorHexregion(screen, x, y, n, a, Grid, Hexagonal, Shortest[i], colors.lblue)
        if delay!=-1:
            maze_functions.updelay(delay//2)
        else:
            maze_functions.updelay(75)

    pygame.display.update()
    return Shortest, Finished