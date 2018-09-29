#MONISHA NAIR ID:2017H1120241P
import turtle
import queue
import timeit
import sys

myPen = turtle.Turtle(visible='False')
window = turtle.Screen()
myPen2 = turtle.Turtle(visible='False')
window.bgcolor("#2288FF")
myPen3 = turtle.Turtle(visible='False')
myPen4 = turtle.Turtle(visible='False')
myPen5 = turtle.Turtle(visible='False')
class Stick:
    x =0
    y =0
    len =0
    type = 1
    present = False

    def setValues(self,x,y,len,type):
        self.x = x
        self.y = y
        self.len = len
        self.type = type


class Node :
    key =0
    edges=[]
    parent=None

# generates goal states
def goalTest():
    #    1  2  3  4  5  6  7  8  9  10  11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40

    a = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0,
         0, 0, 0]
    b = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0,
         0, 0, 0]
    c = [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0,
         0, 1, 0]
    d = [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1,
         0, 0, 1]
    e = [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0]
    f = [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0]
    g = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0]
    h = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0,
         0, 0, 0]
    i = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0,
         0, 0, 0]
    j = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
         0, 0, 0]
    k = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0,
         1, 0, 0]
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1,
         0, 1, 0]
    m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
         1, 0, 1]
    n = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0]
    o = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0]
    p = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0]
    q = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0]
    r = [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0]
    s = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0]
    t = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0]
    u = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0]
    v = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0,
         0, 0, 0]
    w = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
         0, 0, 0]
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0,
         0, 0, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
         0, 0, 0]
    z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
         0, 0, 0]
    a1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
          1, 0, 0]
    b1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          1, 1, 0]
    c1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 1, 1]
    d1 = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0,
          0,
          1, 0]
    ans = []
    ans.append(a)
    ans.append(b)
    ans.append(c)
    ans.append(d)
    ans.append(e)
    ans.append(f)
    ans.append(g)
    ans.append(h)
    ans.append(i)
    ans.append(j)
    ans.append(k)
    ans.append(l)
    ans.append(m)
    ans.append(n)
    ans.append(o)
    ans.append(p)
    ans.append(q)
    ans.append(r)
    ans.append(s)
    ans.append(t)
    ans.append(u)
    ans.append(v)
    ans.append(w)
    ans.append(x)
    ans.append(y)
    ans.append(z)
    ans.append(a1)
    ans.append(b1)
    ans.append(c1)
    # ans.append(d1)
    for x in ans:
        y = hashFunc(x)
        goalLookup.append(y)
    return goalLookup

#generates initial states
def initialStateGenerator(n):
    map={}
    map[1]=[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0,
         0, 1, 1]
    map[2]=[1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0,
         1, 0, 1]

    return map[n]

#initialises turtle screen
def initUISetting():
    myPen.penup()
    myPen.setpos(-250, 250)
    # myPen.setx(-250)
    # myPen.sety(250)

    myPen.hideturtle()
    myPen2.hideturtle()
    myPen3.hideturtle()
    myPen4.hideturtle()
    myPen5.hideturtle()
    myPen.width(3)
    myPen2.width(4)
    myPen2.color("#7CFC00")
    myPen.write("Comparative Analysis")
    myPen.setpos(100, 250)
    myPen.write("BFS Analysis")
    myPen.setpos(-100, 200)
    myPen.write("No of search tree nodes :")
    myPen.setpos(-100, 170)
    myPen.write("memory for one node :")
    myPen.setpos(-100, 140)
    myPen.write("max growth : ")
    myPen.setpos(-100, 110)
    myPen.write("cost : ")
    myPen.setpos(-100, 80)
    myPen.write("time : ")
    myPen.setpos(100, -50)
    myPen.write("DFS Analysis")
    myPen.setpos(-100, -70)
    myPen.write("No of search tree nodes :")
    myPen.setpos(-100, -100)
    myPen.write("memory for one node :")
    myPen.setpos(-100, -130)
    myPen.write("max growth : ")
    myPen.setpos(-100, -160)
    myPen.write("cost : ")
    myPen.setpos(-100, -190)
    myPen.write("time : ")
    myPen.pendown()
#global variables
hashmap={}
goalLookup=[]
lookup={}
bfsmemory =[]
dfsmemory=[]
bfscost=[]
dfscost=[]


#function to print areporting messages
def displayMessage(n):

    myPen2.penup()
    myPen2.setpos(0,0)
    # myPen.width(10)
    # myPen.color("#2288FF")
    # myPen.forward(100)
    # myPen.width(3)
    myPen2.clear()
    myPen2.write(n, font=('Lucida Sans Unicode', 15, 'normal'))
    myPen.pendown()

#function to intialise the grid
def initGrid(stand,x):
    base = 0
    baseY =0
    if(stand==1):
        base = 200
        baseY = 100
    else :
        base = -70
        baseY = 100

    a= initialStateGenerator(x)
    for i in range(1,41) :
        stick = Stick()
        if a[i-1]==1:
            stick.present = True
        else:
            stick.present = False
        hashmap[i] = stick
    setY = base
    counter = baseY
    for i in range(1,5):
        stick = hashmap[i]
        stick.setValues(counter,setY,25,1)
        counter = counter + 25
        hashmap[i] = stick
    setY = setY-25
    counter = baseY
    for i in range(5, 9):
        stick = hashmap[i]
        stick.setValues(counter, setY, 25, 1)
        counter = counter + 25
        hashmap[i] = stick
    setY = setY-25
    counter = baseY
    for i in range(9, 13):
        stick = hashmap[i]
        stick.setValues(counter, setY, 25, 1)
        counter = counter + 25
        hashmap[i] = stick
    setY = setY-25
    counter = baseY
    for i in range(13, 17):
        stick = hashmap[i]
        stick.setValues(counter, setY, 25, 1)
        counter = counter + 25
        hashmap[i] = stick
    setY = setY-25
    counter = baseY
    for i in range(17, 21):
        stick = hashmap[i]
        stick.setValues(counter, setY, 25, 1)
        counter = counter + 25
        hashmap[i] = stick
    setY = base
    counter = baseY
    for i in range(21, 26):
        stick = hashmap[i]
        stick.setValues(counter,setY,-25, 2)
        counter = counter + 25
        hashmap[i] = stick
    setY = setY-25
    counter = baseY
    for i in range(26, 31):
        stick = hashmap[i]
        stick.setValues(counter,setY, -25, 2)
        counter = counter + 25
        hashmap[i] = stick
    setY = setY-25
    counter = baseY
    for i in range(31, 36):
        stick = hashmap[i]
        stick.setValues(counter,setY, -25, 2)
        counter = counter + 25
        hashmap[i] = stick
    setY = setY-25
    counter = baseY
    for i in range(36, 41):
        stick = hashmap[i]
        stick.setValues(counter,setY, -25, 2)
        counter = counter + 25
        hashmap[i] = stick

#function to display the intial grid
def drawGrid():
    a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1]
    for i in range(1, 41):
        myPen.setheading(0)
        if (a[i - 1] == 1):
            myPen.color('#FFFFFF')
        else:
            myPen.color('#2288FF')
        stick = hashmap[i]
        myPen.penup()
        myPen.setx(stick.x)
        myPen.sety(stick.y)
        myPen.pendown()
        if (stick.type == 2):
            myPen.setheading(90)
            # myPen.right(90)
        myPen.forward(stick.len)

        myPen.dot('yellow')
        return hashmap

#function to display state
def drawState(a):
    for i in range(1, 41):
        myPen.setheading(0)
        if (a[i-1] == 1):
            myPen.color('red')
        else:
            myPen.color('#FFFFFF')
        stick = hashmap[i]
        myPen.penup()
        myPen.setx(stick.x)
        myPen.sety(stick.y)
        myPen.pendown()
        if (stick.type == 2):
            myPen.setheading(90)
            # myPen.right(90)
        myPen.forward(stick.len)

        myPen.dot('yellow')

# hash function
def hashFunc(poly):
    b = ''.join(str(x) for x in poly)
    #print(b)
    x = int(b, 2)
    return x

#helper function used to calculate the number of edges present in a state
def calEdges(poly):
    ans=[]
    for i in range(0,40):
        if(poly[i]==1):
            ans.append(i+1)

    return ans
#function to create the root node of the tree
def createRoot(x):
    a = initialStateGenerator(x)
    node = Node()
    node.key = hashFunc(a)
    node.edges=calEdges(a)
    lookup[node.key]=a
    return node
#function to add children to any node
def addChildren(parent) :
    state = lookup[parent.key]
    children =[]
    for i in parent.edges :
        copyState = state.copy()
        copyState[i-1] = 0
        val = hashFunc(copyState)
        if val in lookup :
            continue
        else :
            child = Node()
            child.key = val
            childEdges = []
            for j in parent.edges :
                if(j!=i):
                    childEdges.append(j)
            lookup[val] = copyState
            child.parent = parent
            child.edges = childEdges
            children.append(child)

    return children

#helper function used in dfs
def givePath(node):
    res =[]
    while(node is not None):
        res.append(node.key)
        node = node.parent
    return res


#breadth first search
def bfs(n):
    max_qlen = 1
    no_of_nodes = 0
    q = queue.Queue()
    rootNode = createRoot(n)
    size_of_node = sys.getsizeof(rootNode)
    q.put(rootNode)
    res = []
    level  = -1
    start_time = timeit.default_timer()
    while (q.empty() == False):
        q2 = []
        level = level + 1
        no_of_nodes = no_of_nodes + q.qsize()
        found = False
        if q.qsize() >= max_qlen:
            max_qlen = q.qsize()
        while (q.empty() == False):
            currNode = q.get()
            print(calEdges(lookup[currNode.key]))
            # print(currNode.key)
            # print(currNode)
            if currNode.key in goalLookup:
                res = givePath(currNode)
                found = True
                break
            else:
                children = addChildren(currNode)
                # print('child ' , len(children))
                for x in children:
                    q2.append(x)

        # print('len of q2 ',len(q2),'len of q ',q.qsize())
        if found == False:
            for x in q2:
                q.put(x)
        else:
            break
    elapsed = timeit.default_timer() - start_time
    for x in res:
        print(calEdges(lookup[x]))

    res.reverse()
    cost_bfs = len(calEdges(lookup[res[0]]))
    for x in res:
        drawState(lookup[x])
    return (no_of_nodes,elapsed,max_qlen,size_of_node,level)

# function to display the results of bfs on screen
def bfsParams(no_of_nodes,elapsed,max_qlen,size_of_node,cost):
    myPen3.clear()
    myPen3.penup()
    myPen3.setx(30)
    myPen3.sety(200)
    myPen3.write(no_of_nodes)
    myPen3.pendown()

    myPen3.penup()
    myPen3.setx(30)
    myPen3.sety(170)
    myPen3.write(size_of_node)
    myPen3.pendown()

    memory = size_of_node*no_of_nodes
    bfsmemory.append(memory)
    myPen3.penup()
    myPen3.setx(-70)
    myPen3.sety(110)
    myPen3.write(cost)
    bfscost.append(cost)

    myPen3.pendown()

    myPen3.penup()
    myPen3.setpos(-40, 140)
    myPen3.write(max_qlen)
    myPen3.pendown()

    myPen3.penup()
    myPen3.setpos(-70, 80)
    myPen3.write(elapsed)
    myPen3.pendown()
#function that integrates bfs and the its results to be displayed on screen
def bfsDriver(n):
    (no_of_nodes,elapsed,max_qlen,x,y) = bfs(n)
    bfsParams(no_of_nodes,elapsed,max_qlen,x,y)

found = False
dfs_goalLength =[]
dfs_goalLength.append(0)
max_ssize=[]
max_ssize.append(0)
#depth first seaarch
def dfs(node,res,visited,ans2,max_ssize):
    #explored[node.key]=node.state

    visited.add(node.key)
    res.append(node)
    if len(res)> max_ssize[0]:
        max_ssize[0] = len(res)
    value=lookup[node.key]
    #print(len(res))
    # if(calNum(value)==12):
    #     print(node.key ,":" , calEdges(value),":",calNum(value))
    if node.key in goalLookup :
        print("anytime")
        dfs_goalLength[0]=len(calEdges(lookup[node.key]))
        #found=True

        ans2.append(res.copy())
        for y in res:
            print(calEdges(lookup[y.key]))
        return res
    else:
        for i in node.edges :
            state=[]
            state = value.copy()
            state[i-1]=0
            key2 = hashFunc(state)
            if(key2 in visited):
                #print("anytime2 ")
                continue
            else :
                newNode = Node()
                newNode.key = key2
                newNode.edges = calEdges(state)
                lookup[key2]=state
                dfs(newNode,res,visited,ans2,max_ssize)
        res.pop()
    return res
#function to display dfs results onscreen
def dfsParams(no_of_nodes,elapsed,max_qlen,size_of_node,cost):
    # myPen.setpos(-100, -70)
    # myPen.write("No of search tree nodes :")
    # myPen.setpos(-100, -100)
    # myPen.write("memory for one node :")
    # myPen.setpos(-100, -130)
    # myPen.write("max growth : ")
    # myPen.setpos(-100, -160)
    # myPen.write("cost : ")
    # myPen.setpos(-100, -190)
    # myPen.write("time : ")
    myPen4.clear()
    myPen4.penup()
    myPen4.setx(30)
    myPen4.sety(-70)
    myPen4.write(no_of_nodes)
    myPen4.pendown()

    myPen4.penup()
    myPen4.setx(10)
    myPen4.sety(-100)
    myPen4.write(size_of_node)
    myPen4.pendown()

    memory = size_of_node*max_qlen
    dfsmemory.append(memory)
    myPen4.penup()
    myPen4.setx(-70)
    myPen4.sety(-160)
    myPen4.write(cost)
    dfscost.append(cost)
    myPen4.pendown()

    myPen4.penup()
    myPen4.setpos(-40, -130)
    myPen4.write(max_qlen)
    myPen4.pendown()

    myPen4.penup()
    myPen4.setpos(-70, -190)
    myPen4.write(elapsed)
    myPen4.pendown()

#helper function
def answer(ans):
    lis =[]
    minlen = 100000

    for x in ans :
        if len(x)<minlen:
            minlen = len(x)
            lis=[]
            lis.append(x)
    return lis


#function that integrates dfs and its results
def dfsDriver(n):
    visited = set()
    res = []
    #goalLookup = goalTest()
    ans2 = []
    start_time = timeit.default_timer()
    initSticks = len(calEdges(initialStateGenerator(n)))
    rootNode = createRoot(n)
    size_of_node = sys.getsizeof(rootNode)
    dfs(rootNode,res,visited,ans2,max_ssize)
    elapsed = timeit.default_timer() - start_time
    lis = answer(ans2)
    print("maybe")
    for res in lis:
        print("**********************")
        for y in res:
            print(calEdges(lookup[y.key]))

        print("***********************")

    y = lis[0]
    for x in y:
        drawState(lookup[x.key])

    dfsParams(len(visited),elapsed,max_ssize[0],size_of_node,initSticks-dfs_goalLength[0])


goalLookup = goalTest()
#main driver function
def driver():
    initUISetting()
    for x in range(1,3):
        hashmap = initGrid(1, x)
        displayMessage("Inital State for BFS")
        drawGrid()
        displayMessage("Executing BFS")
        bfsDriver(x)
        displayMessage("BFS Complete")
        displayMessage("Inital State for DFS")
        hashmap = initGrid(2,x)

        drawGrid()
        displayMessage("Executing DFS")
        dfsDriver(x)
        displayMessage("DFS Complete")

    iters = len(bfsmemory)
    bmemory =0
    for x in bfsmemory :
        bmemory = bmemory + x
    myPen5.penup()
    myPen5.setpos(-300,150)
    myPen5.write("BFSAvgMemory : ")
    myPen5.pendown()
    myPen5.penup()
    myPen5.setpos(-180, 150)
    myPen5.write(bmemory/iters)
    myPen5.pendown()

    dmemory = 0
    for x in dfsmemory:
        dmemory = dmemory + x
    myPen5.penup()
    myPen5.setpos(-300, 100)
    myPen5.write("DFSAvgMemory : ")
    myPen5.pendown()
    myPen5.penup()
    myPen5.setpos(-180, 100)
    myPen5.write(dmemory / iters)
    myPen5.pendown()


driver()

turtle.done()