import numpy as np
import random

randomSolnSet={};
templist = np.empty([8, 2])
sortedArr={}; 

def randomNumGenerator():
    for i in range(0, 15):
        for j in range(0, 8):
            randomSolnSet[i,j] = random.randrange(0,7);

def prepareForfitnessCalculation():
        for k in range(0,8):
            templist[k,0] = randomSolnSet[0,k];
            templist[k,1] = k;
        print(np.sort(templist, axis = 0));

def fitnessCalculation(positionList):
    h = 0
    for i in range(0,7):
        for j in range(i+1,7):
            if positionList[i,0] == positionList[j,0]:
                h = h+1
            else:
                t1 = abs(positionList[i,0] - positionList[j,0])
                t2 = abs(positionList[i,1] - positionList[j,1])
            if t1 == t2:
                h = h+1
    print(h);

        

randomNumGenerator();
prepareForfitnessCalculation();
fitnessCalculation(np.sort(templist, axis = 0));
