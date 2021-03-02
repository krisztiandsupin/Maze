'''import pygame, openpyxl, math, os, time
import mazefunc, mazealg, mazevis, solvealg

position=(0,30)
os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])
#os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

#size,location
n=30
#scr=(1530,790)
scr=(1280, 923)
labelsize=75
marginsize=15
a=mazefunc.rectSize(scr, n, marginsize, labelsize)                #size of edge of rectengular
loc=((scr[0] / 2 - n * a) / 2, labelsize)
line_thickness=3   #line thichness


#Screen size
gameDisplay = pygame.display.set_mode(scr)
#gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Maze')

#maze visualization
startime=time.time()
Grid=mazefunc.gridGen(n)
gameDisplay.fill(mazefunc.white)
pygame.display.update()

n=31
x0=100
y0=100
lnthickness=2
Grid,Maze=mazealg.mazePrim(gameDisplay,0,0,n,2*a,(mazefunc.white,mazefunc.black,mazefunc.white,mazefunc.white),-1,False)
mazefunc.drawGrid(gameDisplay,x0,y0,n,2*a,Grid,(mazefunc.white,mazefunc.black,mazefunc.white,mazefunc.white))
for i in range(0,n**2):
    mazefunc.colorRegion2(gameDisplay, x0, y0, n, 2 * a, Grid, i, mazefunc.lgrey,mazefunc.dgrey)

startList=[0, n-1, n*(n-1), n**2-1]
colList=[mazefunc.dblue,mazefunc.dred,mazefunc.dgreen,mazefunc.gold]
lcolList=[mazefunc.blue,mazefunc.mred,mazefunc.green,mazefunc.lgold]

for i in range(0,len(startList)):
    mazefunc.colorRegion2(gameDisplay, x0, y0, n, 2 * a, Grid, startList[i], colList[i], mazefunc.black)
mazefunc.colorRegion(gameDisplay, x0, y0, n, 2 * a, Grid, n//2*n+n//2, mazefunc.salmon)

#frame
pygame.draw.rect(gameDisplay,mazefunc.black,[x0,y0,2*n*a+lnthickness-1,2*n*a+lnthickness-1],lnthickness)
pygame.display.update()

#position and size for team names
x1=x0+n*2*a+100
y1=y0+150
textsize=50
#team names
steplist=[i for i in range(0,len(colList))]
for i in range(0,len(colList)):
    if i==0:
        pygame.draw.circle(gameDisplay,colList[i],(x1,y1+i*textsize),textsize//4,0)
        mazefunc.textDisplayleft(gameDisplay,x1+textsize//2,y1+i*textsize-textsize//3,'Team {0}'.format(i+1),textsize,colList[i])
    else:
        pygame.draw.circle(gameDisplay, colList[i], (x1, y1 + i * textsize+textsize), textsize // 4, 0)
        mazefunc.textDisplayleft(gameDisplay, x1 + textsize // 2, y1 + i * textsize+textsize - textsize // 3,
                                 'Team {0}'.format(i + 1), textsize, colList[i])

mazefunc.updelay(1000)

step=0
movesleft=5
target=n//2*n+n//2
mazefunc.textDisplayleft(gameDisplay,x1,y1+textsize//2,'moves left: {0}'.format(movesleft),textsize//10*8,colList[step%4])
pygame.display.update()


Visible=[[] for i in range(0,4)]
for i in range(0,4):
    regionNeighbor = mazefunc.regionNeighbor(n, startList[i])
    for j in regionNeighbor:
        step=j-startList[i]
        for k in range(0,5):
            if (min(startList[i]+k*step,startList[i]+(k+1)*step),max(startList[i]+k*step,startList[i]+(k+1)*step)) in Maze:
                Visible[i].append(startList[i]+(k+1)*step)
            else:
                break

for i in Visible:
    for j in i:
        mazefunc.colorRegion(gameDisplay, x0, y0, n, 2 * a, Grid, j, mazefunc.white)
        mazefunc.updelay(10)
    pygame.time.delay(30)

pygame.display.update()
VisibleAll=Visible[0]+Visible[1]+Visible[2]+Visible[3]
CurrentPosition=startList

for i in range(0,4):
    pygame.draw.circle(gameDisplay,mazefunc.lgreen,(x0+(startList[i]%n)*2*a+a,y0+(startList[i]//n)*2*a+a),math.floor(a*0.8),0)
    #mazefunc.drawFigure(gameDisplay,x0+(startList[i]%n)*2*a,y0+(startList[i]//n)*2*a,2*a,lcolList[i])
mazefunc.updelay(10000)

step=0

while True:
    current=0
    while movesleft!= 0:
        print(current)
        region=-1
        while region !=startList[step%4]:
            region = mazefunc.mouseRegionPosition(x0, y0, n, a)

        lcol = lcolList[startList.index(region)]
        mazefunc.drawRect(gameDisplay, x0 + region % n * 2 * a, y0 + region // n * 2 * a, 2 * a, Grid[region],
                          lcol, mazefunc.black)

        mazefunc.updelay(500)
        col = colList[startList.index(region)]
        mazefunc.drawRect(gameDisplay, x0 + region % n * 2 * a, y0 + region // n * 2 * a, 2 * a, Grid[region],
                          col, mazefunc.black)

        regionNeighbor=mazefunc.regionNeighbor(n,region)

        List=mazefunc.mazeRange(n,Maze,current,movesleft)
        print(List)
        for i in List:
            mazefunc.textDisplay(gameDisplay,x0+(i%n*2*a)+a,y0+(i//n*2*a)+a,'X',2*a,col)
        pygame.display.update()

        while current not in List:
            current = mazefunc.mouseRegionPosition(x0, y0, n, a)

        mazefunc.textDisplay(gameDisplay, x0 + (current % n * 2 * a) + a, y0 + (current // n * 2 * a) + a, 'X', 2 * a, lcol)
        mazefunc.updelay(200)
        mazefunc.textDisplay(gameDisplay, x0 + (current % n * 2 * a) + a, y0 + (current // n * 2 * a) + a, 'X', 2 * a, col)
        mazefunc.updelay(200)

        newVisible=mazefunc.mazeRange(n,Maze,current,5)
        print(newVisible)
        for i in newVisible:
            mazefunc.colorRegion(gameDisplay,x0,y0,n,2*a,Grid,i,mazefunc.white)
            mazefunc.updelay(50)


        for i in List:
            mazefunc.colorRegion(gameDisplay,x0,y0,n,2*a,Grid,i,mazefunc.white)
        pygame.display.update()
        pygame.draw.circle(gameDisplay, mazefunc.lgreen,
                           (x0 + (current % n) * 2 * a + a, y0 + (current // n) * 2 * a + a),
                           math.floor(a * 0.8), 0)




            # get a list of all sprites that are under the mouse cursor
            #clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # most reliable exit on x click
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            # optional exit with escape key
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit '''