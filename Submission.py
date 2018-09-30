#MONISHA NAIR ID:2017H1120241P
import turtle
import timeit


myPen = turtle.Turtle(visible='False')
window = turtle.Screen()
window.setup(width=1000,height=700)
window.bgcolor("black")
window.title("Block Puzzle")
#window.setup(startx=10,starty=100)
myPen.hideturtle()
myPen.speed(0)
#global variables
writePathBlue = turtle.Turtle(visible='False')
writePathBlue.color("blue")
writePathBlue.hideturtle()

writePathGreen = turtle.Turtle(visible='False')
writePathGreen.color("green")
writePathGreen.hideturtle()

heading = turtle.Turtle(visible='False')
heading.color("white")
heading.hideturtle()

heading.penup()
heading.setx(0)
heading.sety(300)
heading.pendown()
heading.write("greedy best first search")
heading.penup()
heading.setx(0)
heading.sety(-30)
heading.pendown()
heading.write("beam hill climbing search")

heading.penup()
heading.color("red")
heading.setx(200)
heading.sety(300)
heading.pendown()
heading.write("blue--> heuristic1 green-->heuristic2",font=("Comic Sans MS", 12, "normal"))

heading.penup()
heading.color("white")
heading.setx(-350)
heading.sety(300)
heading.pendown()
heading.write("Comparative Analysis")

heading.penup()
heading.color("white")
heading.setx(-450)
heading.sety(250)
heading.pendown()
heading.write("Time : ")

heading.penup()
heading.color("white")
heading.setx(-450)
heading.sety(230)
heading.pendown()
heading.write("Cost : ")

heading.penup()
heading.color("white")
heading.setx(-450)
heading.sety(200)
heading.pendown()
heading.write("Memory : ")
slabs = 10

#classes
class State :
    lis=[]
    parent = None
    hVal = -1

    def getHval(self):
        return self.hVal

initmap={}
goalmap={}
def init1():

    initmap[1] = [[19,120,26,16,90],[116,148,132],
                  [104,31,28,37,200,81],[118,106,99,1,40,63,190,205,10],
                  [14,32,20,36,78,22],[11,16,8,12,98],
                  [39,70,86,55,100],[316,178,122],
                  [141,302],[341,112,89,67,54,44]]
    # initmap[2] = [[26, 16, 90], [116, 148, 132], [104, 31, 28, 37, 200, 81,90,72],
    #               [118, 106, 99, 1, 40, 63, 190, 205, 10], [14, 32, 20, 36, 78, 22], [11, 16, 8, 12, 98],
    #               [39, 70], [122], [141, 302], [1, 2, 89, 67, 54, 44]]
    # initmap[3] = [[1, 2, 3], [11, 12, 13,14], [21, 22, 23, 24, 25],
    #               [31,32,33,34,35,36], [41, 42, 43, 44, 45, 46,47], [51,52, 53, 54, 55,56,57,58],
    #               [61,62,63,64,65,66,67,68,69], [71,72,73,74,75,76,77,78,79,80], [81, 82], [91]]




def init2():
    goalmap[1] = [[19, 120, 26, 16],[116, 148, 132,90],
                  [104, 31, 28, 37, 200],[118, 106, 99, 1, 40, 63, 190, 205, 10,81],
                  [14, 32, 20], [11, 16, 8, 12, 98,78,36],
              [39, 70, 86, 55, 100], [316, 178],
                  [141, 302], [341, 112, 89, 67, 54, 44,122,22]]
    # goalmap[2] = [[26], [116, 148, 132], [104, 31, 28, 37, 200, 81, 90, 72],
    #               [118, 106, 99, 1, 40, 63, 190, 205], [14, 32, 20, 36, 78, 22,10], [11, 16, 8, 12],
    #               [39, 70,98], [122], [141, 302], [1, 2, 89, 67, 54, 44,90,16]]
    # goalmap[3] = [[1], [11, 12, 13, 14], [21, 22, 23, 24, 25],
    #               [31, 32, 33, 34, 35, 36], [41, 42, 43, 44, 45, 46], [51, 52, 53, 54, 55, 56, 57, 58,47],
    #               [61, 62, 63, 64, 65, 66, 67, 68, 69,91], [71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [81, 82], [3,2]]


def goalState(i):
    return goalmap[i]

def initalState(i,c):
    state = State()
    state.lis = copy(initmap[i])
    if c==1 :
        state.hVal = calheuristicOneofgoalstate(i)
    else:
        state.hVal = calheuristicTwoofgoalstate(i)

    return state




def calheuristicOneofgoalstate(i):
    b = goalState(i)
    h = 0
    for x in b :
        val= len(x)
        for y in x :
            h = h + val
            val  =  val - 1

    return h

def calheuristicTwoofgoalstate(i):
    b = goalState(i)
    h = 0
    for x in b :
        h = h + len(x)
    return h


def calheuristicOneothers(a,it):
    val = 0
    g = goalState(it)
    for i in range(0,10):
        leni = len(a[i])
        lenic = 1
        if leni > 0 :
            for j in range(0,leni):
                try:
                    if g[i][j] == a[i][j]:
                        val = val + lenic
                    else :
                        val = val + (-1) * lenic
                    lenic = lenic + 1
                except :
                    val = val + (-1)*lenic
                    lenic = lenic + 1

    return val

def calheuristicTwoothers(a,it):
    val = 0
    g = goalState(it)
    for i in range(0,10):
        leni = len(a[i])
        if leni > 0 :
            for j in range(0,leni):
                try:
                    if g[i][j] == a[i][j]:
                        val = val + 1
                    else :
                        val = val + (-1)

                except :
                    val = val + (-1)
                    #lenic = lenic + 1

    return val

def copy(x):
    y=[]
    for i in x :
        sub = []
        for j in i :
            sub.append(j)
        y.append(sub)
    return y


def genNextState(parent,c,it):
    #minHval = calheuristicothers(parent)
    changed = False
    allStates=[]
    ans = []
    for i in range(0, slabs):
        dummy = []
        dummy.clear()
        dummy = copy(parent.lis)
        #print("parents copy : " ,dummy)
        if (len(dummy[i]) > 0):
            x = dummy[i].pop()
            #print("edited parents copy : ",x)
            for j in range(0, slabs):
                if i != j:
                    dumm2 = []
                    dumm2 = copy(dummy)
                    dumm2[j].append(x)
                    if c==1:
                        y = calheuristicOneothers(dumm2,it)
                    else :
                        y = calheuristicTwoothers(dumm2,it)
                    #print("what is going on : ",dumm2)
                    state = State()
                    state.lis = copy(dumm2)
                    #print("i should get : " , state.lis)
                    state.parent = parent
                    state.hVal = y
                    if(state.hVal>parent.hVal):
                        allStates.append(state)
                    else :
                        allStates.append(state)

    return allStates

def hash(a):
    ind = 1
    val = 0
    for i in a :
        ind2 = 1
        for j in i :
           val = val + ind * ind2 * j
           ind2 = ind2 + 1
        ind = ind + 1

    return val


check = set()

def func2(it,c):
    res = []
    if c==1:
        goalVal = calheuristicOneofgoalstate(it)
    else :
        goalVal = calheuristicTwoofgoalstate(it)
    #currVal = calheuristicothers(initState())
    #found
    state = initalState(it,c)
    currStates = []
    currStates.append(state)
    found = False
    while(len(currStates)>=0):
        # print("*********currState********")
        # for y in currStates:
        #     print(y.lis)
        # print("***************************")
        if len(currStates)==0:
            print("no answer ")
            break
        else :
            nextStates =[]
            for x in currStates :
                sublis = genNextState(x,c,it)
                for y in sublis :
                    #print("i got : ", y.lis , ' : ' , y.hVal )
                    if y.hVal==goalVal :
                        res.append(y)
                        #print("ans found" , y.lis)
                        found = True
                        break
                    else :
                        nextStates.append(y)
                if found == True:
                    break
            if found==True:
                break

            currStates.clear()
            nextStates = sorted(nextStates,key=State.getHval,reverse=True)
            index = 0
            while(len(currStates)<1 and index<len(nextStates)):
                xy = hash(nextStates[index].lis)
                if(xy not in check):
                    currStates.append(nextStates[index])
                    check.add(xy)
                index = index + 1

            #print("len of : " , len(currStates))

    return res
            #break

def func3(it,c):
    res = []
    if c==1:
        goalVal = calheuristicOneofgoalstate(it)
    else :
        goalVal = calheuristicTwoofgoalstate(it)
    #currVal = calheuristicothers(initState())
    #found
    state = initalState(it,c)
    currStates = []
    currStates.append(state)
    found = False
    while(len(currStates)>=0):
        # print("*********currState********")
        # for y in currStates:
        #     print(y.lis)
        # print("***************************")
        if len(currStates)==0:
            print("no answer ")
            break
        else :
            nextStates =[]
            for x in currStates :
                sublis = genNextState(x,c,it)
                for y in sublis :
                    #print("i got : ", y.lis , ' : ' , y.hVal )
                    if y.hVal==goalVal :
                        res.append(y)
                        #print("ans found" , y.lis)
                        found = True
                        break
                    else :
                        nextStates.append(y)
                if found == True:
                    break
            if found==True:
                break

            currStates.clear()
            nextStates = sorted(nextStates,key=State.getHval,reverse=True)
            index = 0
            while(len(currStates)<4 and index<len(nextStates)):
                xy = hash(nextStates[index].lis)
                if(xy not in check):
                    currStates.append(nextStates[index])
                    check.add(xy)
                index = index + 1

            #print("len of : " , len(currStates))

    return res
            #break

def func(x,y,z):
    myPen.penup()
    myPen.color("yellow")
    myPen.setx(x)
    myPen.sety(y)
    myPen.pendown()
    # myPen.width(5)
    # myPen.setx("0")
    # myPen.sety("0")
    myPen.forward(25)
    myPen.left(90)
    myPen.forward(25)
    myPen.left(90)
    myPen.forward(25)
    myPen.left(90)
    myPen.forward(25)
    myPen.left(90)
    myPen.penup()
    myPen.setx(x+5)
    myPen.sety(y+5)
    myPen.color("green")
    myPen.pendown()
    myPen.write(z)
   # myPen.pendown()

def erase(x,y,z,curry):
    myPen.penup()
    myPen.setx(x)
    myPen.sety(y)
    if y==curry:
        myPen.color("black")
    else :
        myPen.color("yellow")
    myPen.pendown()
    # myPen.width(5)
    # myPen.setx("0")
    # myPen.sety("0")
    myPen.forward(25)
    myPen.left(90)
    myPen.penup()
    myPen.color("black")
    myPen.pendown()
    myPen.forward(25)
    myPen.left(90)
    myPen.forward(25)
    myPen.left(90)
    myPen.forward(25)
    myPen.left(90)
    myPen.penup()
    myPen.setx(x+5)
    myPen.sety(y+5)
    myPen.color("black")
    myPen.pendown()
    myPen.write(z)
    # myPen.setx(x + 15)
    # myPen.sety(y + 15)
    # myPen.color("black")
    # myPen.pendown()
    # myPen.write(z)
pathGreedy=[]
def diffDrawGreedy(pState,cState):

    for i in range(0,slabs):
        if pState[i]==cState[i]:
            #print("same")
            continue
        elif len(pState[i])>len(cState[i]):
            #print("diff fi : " , pState[i],cState[i])
            xco = xmapGreedy[i]
            yco = 40 + (len(cState[i]))*25
            z = pState[i][(len(pState[i])-1)]
            #print("printing here : ",i , xco,yco)
            pathGreedy.append(z)
            erase(xco,yco,z,40)
        else :
            #print("diff se : ", pState[i], cState[i])
            xco = xmapGreedy[i]
            yco = 40+ len(pState[i])*25
            z = cState[i][(len(cState[i])-1)]
            func(xco,yco,z)


pathHC=[]
def diffDrawHC(pState,cState):
    for i in range(0,slabs):
        if pState[i]==cState[i]:
            #print("same")
            continue
        elif len(pState[i])>len(cState[i]):
            #print("diff fi : " , pState[i],cState[i])
            xco = xmapHC[i]
            yco = -250 + (len(cState[i]))*25
            z = pState[i][(len(pState[i])-1)]
            #print("printing here : ",i , xco,yco)
            pathHC.append(z)
            erase(xco,yco,z,-250)
        else :
            #print("diff se : ", pState[i], cState[i])
            xco = xmapHC[i]
            yco = -250+ len(pState[i])*25
            z = cState[i][(len(cState[i])-1)]
            func(xco,yco,z)

greedyTime = 0
def greedyBFS(it,c):
    start_time = timeit.default_timer()

    endstate = func2(it,c)[0]
    answer = []
    while (endstate!= None):
        answer.append(endstate.lis)
        endstate = endstate.parent

    answer.reverse()
    # #print(initmap[1])
    # print("hey look what I found : ", answer)
    # for x in answer :
    #     print("state : " , x)

    greedyTime = timeit.default_timer() - start_time

    print("greedyT :" , greedyTime)
    return answer

def writeH1Path(a,x,y):

    for i in a :
        writePathBlue.penup()
        writePathBlue.setx(x)
        writePathBlue.sety(y)
        writePathBlue.pendown()
        b = "remove " + str(i)
        writePathBlue.write(b)
        y = y-25

def writeH2Path(a,x,y):

    for i in a :
        writePathGreen.penup()
        writePathGreen.setx(x)
        writePathGreen.sety(y)
        writePathGreen.pendown()
        b = "remove " + str(i)
        writePathGreen.write(b)
        y = y-25


def greedyBFSDriver(i,c):
    answer = []
    answer = greedyBFS(i,c)
    # print(len(answer))
    # print(answer)
    #path = []
    for i in range(1, len(answer)):
        diffDrawGreedy(answer[i - 1], answer[i])
    x =0
    y =0
    if c==1 :
        x=-100
        y = 300
        writeH1Path(pathGreedy, x, y)
    else :
        x = -200
        y = 300
        writeH2Path(pathGreedy, x, y)


    return 0

beamTime = 0
def beamHC(it,c):
    start_time = timeit.default_timer()
    beamTime = timeit.default_timer() - start_time
    endstate = func3(it,c)[0]
    answer = []
    while (endstate!= None):
        answer.append(endstate.lis)
        endstate = endstate.parent

    answer.reverse()
    print("beamTime" ,beamTime)
    # #print(initmap[1])
    # print("hey look what I found : ", answer)
    # for x in answer :
    #     print("state : " , x)


    return answer

def beamHCDriver(i,c):
    answer = []
    answer = beamHC(i,c)
    #print(len(answer))
    #print(answer)
    for i in range(1, len(answer)):
        diffDrawHC(answer[i - 1], answer[i])
    x = 0
    y = 0
    if c==1 :
        x = -100
        y = -100
        writeH1Path(pathHC, x, y)
    else :
        x = -200
        y = -100
        writeH2Path(pathHC, x, y)

    return 0


xmapGreedy = {}
xmapHC = {}
def initialUI(i):
    basex = 50
    basey = 25
    currx = -10
    curry = 400
    index = 0
    state2 = initalState(i,1)
    #print("here : ",state2.lis)
    for i in state2.lis:
        xmapGreedy[index] = currx
        curry = 40
        for j in i:
            func(currx, curry, j)
            curry = curry + basey
        currx = currx + basex
        index = index + 1
    currx2 = -10
    curry2 = -250
    index = 0
    #state2 = initalState(i, 1)
    for i in state2.lis:
        xmapHC[index] = currx2
        curry2 = -250
        for j in i:
            func(currx2, curry2, j)
            curry2 = curry2 + basey
        currx2 = currx2 + basex
        index = index + 1
    # print(xmapGreedy)
    # print(xmapHC)




def driver():
    #print(initmap)
    #print(goalmap)
    c = 1
    for i in range(1,2):
        initialUI(i)
        greedyBFSDriver(i,1)
        beamHCDriver(i,1)

        writePathBlue.penup()
        writePathBlue.setx(-405)
        writePathBlue.sety(250)
        writePathBlue.pendown()
        b = "(gbfs) : " + str(greedyTime) + "(bhc) : " + str(beamTime)
        writePathBlue.write(b)

        writePathBlue.penup()
        writePathBlue.setx(-405)
        writePathBlue.sety(230)
        writePathBlue.pendown()
        b = "(gbfs) : " + str(len(pathGreedy)) + "(bhc) : " + str(len(pathHC))
        writePathBlue.write(b)
        pathGreedy.clear()
        pathHC.clear()
    myPen.reset()
    myPen.hideturtle()
    myPen.speed(0)

    c = 2
    for i in range(1,2):
        initialUI(i)
        greedyBFSDriver(i,2)
        beamHCDriver(i,2)
        writePathGreen.penup()
        writePathGreen.setx(-300)
        writePathGreen.sety(250)
        writePathGreen.pendown()
        b = "(gbfs) : " + str(greedyTime) + "(bhc) : " + str(beamTime)
        writePathGreen.write(b)

        writePathGreen.penup()
        writePathGreen.setx(-300)
        writePathGreen.sety(230)
        writePathGreen.pendown()
        b = "(gbfs) : " + str(len(pathGreedy)) + "(bhc) : " + str(len(pathHC))
        writePathGreen.write(b)
        pathGreedy.clear()
        pathHC.clear()


    return 0


init1()
init2()
driver()
#print("a path : " , pathGreedy)
turtle.done()