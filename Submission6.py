#MONISHA NAIR ID:2017H1120241P
#display basic UI
from tkinter import *
from tkinter import messagebox
import os
master = Tk()
master.geometry("900x800")

#global variables
graph ={}
probGraph={}
final_lis= []
cause = {}
effect = {}
l1 = Label(master,text = 'Quey Variables')
l1.grid(row = 0 , column = 15)
l2 = Label(master,text = 'Condition Variables')
l2.grid(row = 0 , column = 20)
query = []
condition = []
l3 = Label(master,text = 'FinalQuery')
l3.grid(row = 35 , column = 8)

#read file
file = open('input1.txt', 'r')
input1 = file.read()
filelist = input1.split('\n')

#parse and populate graphs
def parseFile():
    for i in range(0, len(filelist) - 2):
        val = filelist[i]
        info = val.split('>>')
        name = info[0]
        name = name.replace(" ", "")
        name = name.replace(' ', '')
        if name not in graph:
            graph[name] = []
        lis = info[1]
        index = lis.index(']')
        lis = lis.replace(']', '')
        lis = lis.replace('[', '')
        lis2 = lis.split(',')
        parentList = []
        for parent in lis2:
            parent = parent.replace("'", "")
            parent = parent.replace(' ', '')
            # print('parent : ' , parent)
            parentList.append(parent)
            prevp = graph[name]
            if parent not in prevp:
                prevp.append(parent)

        probStr = info[2]

        probLis = probStr.split(" ")
        probLis.pop(0)
        if len(parentList) == 0:
            keyString = '' + name
            probGraph[keyString] = probLis[0]
        else:
            negate = []
            for i in parentList:
                negate.append('~' + i)
            lis = []
            lis.append(negate)
            ind = len(negate) - 1

            while (ind >= 0):
                lis2 = []
                for element in lis:
                    element2 = []
                    element2.extend(element)
                    # print(element," ind : " , ind)
                    element2[ind] = element2[ind].replace("~", "")
                    # rint(element2)
                    lis2.append(element2)
                # print(lis)
                for x in lis2:
                    lis.append(x)
                ind = ind - 1

            #print(lis)
            if len(lis) == 2:
                if lis[0][0] == "~":
                    key = name
                    probGraph[key] = probLis[0]
                else:
                    for i in range(0, len(lis)):
                        key = name + "|" + ''.join(lis[i])
                        probGraph[key] = probLis[i]
            else:
                for i in range(0, len(lis)):
                    key = name + "|" + ''.join(lis[i])
                    probGraph[key] = probLis[i]

#print graphs
def printGraph():
    print('graph ',graph)
    print('prob graph ',probGraph)

#display on screen
def display_var():
    i = 1
    for x in graph.keys():
        cause[x] = False
        cause['~'+x] = False
        effect[x] = False
        effect['~' + x] = False
    for x in graph.keys():
        var1 = IntVar()
        Checkbutton(master, text=x, variable=var1).grid(row = i,pady = 0,column = 15)
        cause[x] = var1
        var2 = IntVar()
        Checkbutton(master, text='~'+x, variable=var2).grid(row = i, pady = 0, column = 17)
        cause['~' + x] = var2
        var3 = IntVar()
        Checkbutton(master, text=x, variable=var3).grid(row=i, pady=0, column=20)
        effect[x] = var3
        var4 = IntVar()
        Checkbutton(master, text='~'+x, variable=var4).grid(row=i, pady=0, column=22)
        effect["~" + x] = var4
        i =i + 1

#function to save query
def computeExpression():
    global l4
    for i in cause.keys():
        if cause[i].get()==1 :
            query.append(i)
    for i in effect.keys():
        if effect[i].get()==1 :
            condition.append(i)
    print('q: ',query)
    print('co : ' , condition)
    final_query = ','.join(query) + "|" + ','.join(condition)
    final_lis.append(final_query)
    l4 = Label(master,text = final_query)
    l4.grid(row=35, column=10)


#clear query variables
def reset():
    for q in query :
        cause[q].set(0)
    query.clear()
    for q in condition :
        effect[q].set(0)
    condition.clear()
    l4.grid_forget()
    l6.grid_forget()


#display ui
def start_ui() :
    display_var()
    b1 = Button(master, text="SaveQuery", command=computeExpression)
    b1.grid(row=20, column=35)
    b2 = Button(master, text="ResetQuery", command=reset)
    b2.grid(row=30, column=35)

#To compute Markov Blanket
def computeMarkovBlanket(variables):
    markov = {}
    print('variables  :' ,variables)
    try:
        for var in variables :
            if var not in '':
                if '~' in var :
                    markov[var] = graph[var.replace('~','')]
                else :
                    markov[var]=graph[var]
                if '~' in var :
                    lis= graph[var.replace('~','')]
                else :
                    lis=graph[var]
                #print("what lis : " , lis)
                for y in lis :
                    if y not in markov.keys():
                        if '~' + y not in variables:
                            variables.append(y)

        #print('markov : ', markov)
        return markov
    except :
        print("problem in markov blanket generation")

#given markov blanket and expression calculates the conditional probabiltity using cause and effect
def computeProbability(Markov,expression) :
    num = 1.0
    deno = 1.0

    exp = expression.split("|")
    exp2 = expression.replace(",","|").split("|")

    print("numerator expression :" , exp2)
    print("denominator expression : ", exp[1])

    num = compute(Markov,exp2)
    if len(exp[1])>0 :
        deno = compute(Markov,exp[1].split(","))

    print('Final Answer : ',num/deno)
    return num/deno

#helper function for calculating conditional Probability
def compute(Markov , expression):
    donotvary =  []
    donotvary.extend(expression)
    #print('donotvary : ', donotvary)
    vary  = []
    newlis = []
    newlis.extend(donotvary)
    for x in newlis :
        if x not in '' :
            if x not in Markov.keys():
                if "~" in x :
                    parentList = Markov[x.replace("~","")]
                else:
                    parentList = Markov["~" + x]
            else:
                parentList = Markov[x]
            for parent in parentList :
                if (parent not in vary and parent not in donotvary) and ("~"+parent not in vary and "~"+parent not in donotvary) and parent not in'' :
                    vary.append(parent)
                    newlis.append(parent)
    if '' in vary :
        vary.remove('')
    if '' in donotvary :
        donotvary.remove('')

    #print('vary : ',vary)

    anslis = []

    generateAllCominations(vary,0,anslis)

    #print("all : " , anslis)
    combos = []
    num = 0
    for v in anslis :
        temp = []
        temp.extend(donotvary)
        temp.extend(v)
        combos.append(temp)
        val2 = calculateJointProbabilty(temp,Markov)
        print(temp,' : ' , val2)
        num = num + val2

    print("all combinations : " , combos)

    return num

#helper function to enumenrate expression to calculate conditional probability (done using inference by enumeration)
def generateAllCominations(lis, i, anslis):
    if (i <=len(lis)):
        str = "".join(lis)
        #print(str)
        if lis not in anslis:
            anslis.append(lis)

        lis2 = []
        lis3 = []
        lis2.extend(lis)
        lis3.extend(lis)
        if i<len(lis):
            lis2[i] = '~' + lis2[i]
            generateAllCominations(lis2, i + 1, anslis)
            generateAllCominations(lis3, i + 1, anslis)

# given any expression lis and the markov blanket joint probability calculated using marginalisation and chain rule
def calculateJointProbabilty(lis,markov):
    try :
        val = 1.0
        #print("here " , markov)
        for x in lis :
            if x not in markov.keys():
                if "~" in x:
                    parentsOfX = markov[x.replace("~",'')]
                else:
                    parentsOfX = markov['~'+x]
            else:
                 parentsOfX = markov[x]
            if '' in parentsOfX :
                parentsOfX.remove('')
            if len(parentsOfX)==0:
                if '~' in x :
                    val = val * (1-(float)(probGraph[x.replace("~","")]))
                else:
                    val = val * (float)(probGraph[x])
            else :
                term = ""
                for parent in parentsOfX :
                    if parent in lis :
                        term = term+''+parent
                    else :
                        term = term+'~'+parent
                if "~" in x :
                    fTerm = x.replace("~","")+"|"+term
                    val = val * (1- (float)(probGraph[fTerm]))
                else :
                    fTerm = x+'|'+term
                    val = val * (float)(probGraph[fTerm])

        return val
    except :
        print('Exception in ',lis,' having ', markov)

#checks input variables for correct combination given or not
def input_checks():
    if len(query)==0  or len(query)>10:
        return False
    if len(condition)>10:
        return False
    for x in query :
        if x in condition or "~"+x in condition :
            return False
    return True

#query processing
def process():
    if input_checks()==False :
        messagebox.showerror("Error", "Incorrect Input Try Again")
        master.quit()
    else :
        try:
            global l6
            final_query = final_lis[0]
            print('final query is : ',final_query)
            param = final_query.replace(",","|").split("|")
            markov = computeMarkovBlanket(param)
            print("markov blanket : " , markov)
            val = computeProbability(markov,final_query)
            l5 = Label(master, text='Result : ')
            l5.grid(row=50, column=8)
            l6 = Label(master, text=val)
            l6.grid(row=50, column=10)
            l7 = Label(master, text='Markov Blanket : ')
            l7.grid(row=60, column=8)
            S = Scrollbar(master)
            T = Text(master, height=15, width=50)
            S.grid(row = 80,column=10)
            T.grid(row = 80,column=10)
            T.columnconfigure(20)
            S.config(command=T.yview)
            T.config(yscrollcommand=S.set)
            quote =""
            for x in markov.keys():
                if len(markov[x])==0 :
                    quote = quote + "Node : " + x + ' has no parents'
                else :
                    quote = quote + "Node : " + x + ' has parents :'
                for p in markov[x] :
                    quote = quote + '' + p +" "
                quote = quote + '\n'
            T.insert(END, quote)
        except :
            messagebox.showerror("Error", "Something went wrong")
            master.quit()

############################################################################################
parseFile()
start_ui()
b3 = Button(master, text="ProcessQuery", command =process)
b3.grid(row=40, column=35)

master.mainloop()
