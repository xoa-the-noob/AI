import numpy as np
import random

inputSet = []

def randomNumGenerator():
    for i in range(0, 15):
        a = []
        for j in range(0, 8):
            a.append(random.randrange(0,7));
        inputSet.append(a)

def prepareForfitnessCalculation():
    for i in range(0,15):
        b = []
        for j in range(0,8):
            tempLst = []
            for k in range(0,1):
                tempLst.append(inputSet[i][j])
                tempLst.append(j)
            b.append(tempLst)
        fitnessCalculation(sorted(b),i)
    
def fitnessCalculation(positionList,k):
    h = 0
    for i in range(0,7):
        for j in range(i+1,7):
            t1 = abs(positionList[i][0] - positionList[j][0])
            t2 = abs(positionList[i][1] - positionList[j][1])
            if positionList[i][0] == positionList[j][0]:
                h = h+1
            elif t1 == t2:
                h = h+1
    thisdict[k] = h

def getFirstTwoKeys(dictionary):
    n = 0
    Index = []
    for state in dictionary:
        Index.append(state)
        n = n+1
        if n == 2:
            break
    return Index

def crossover():
    n = 0; IndexAsc = []; IndexDes = []
    Parent1 = []; Parent2 = []
    Child1 = []; Child2 = []
    
    IndexAsc = getFirstTwoKeys(sort_dict)
    IndexDes = getFirstTwoKeys(sort_dict_rev)

    for i in range(0,15):
        if(i == IndexAsc[0]):
             for j in range(0,8):
                 Parent1.append(inputSet[i][j])
        elif(i == IndexAsc[1]):
             for j in range(0,8):
                 Parent2.append(inputSet[i][j])

    for j in range(0,4):
        Child1.append(Parent1[j])
        Child2.append(Parent2[j])

    for j in range(4,8):
        Child1.append(Parent2[j])
        Child2.append(Parent1[j])
        
    m = random.randrange(0,7)
    n = random.randrange(0,7)
    Child1[m], Child1[n] = Child1[n], Child1[m]
    Child2[m], Child2[n] = Child2[n], Child2[m]
    
    for i in range(0,15):
        if(i == IndexDes[0]):
             for j in range(0,8):
                 inputSet[i][j] = Child1[j]
        elif(i == IndexDes[1]):
             for j in range(0,8):
                 inputSet[i][j] = Child2[j]

    print("\nThe children after crossover:")
    print(Child1)
    print(Child2)
    print("\nThe input set after rearranging:")
    print(inputSet)


randomNumGenerator()
for d in range(0,10):
    thisdict = {}
    prepareForfitnessCalculation()  
    print("\nThe input set at first:")
    print(inputSet)
    print("\nThe entry numbers vs fitness scores:")
    print(thisdict)  
    sort_dict = dict(sorted(thisdict.items(), key=lambda item: item[1]))
    sort_dict_rev = dict(sorted(thisdict.items(), key=lambda item: item[1],reverse=True))
    crossover()


