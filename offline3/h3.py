positionList = [(1,2),(1,8),(3,6),(4,5),(5,3),(6,1),(7,4),(8,7)]

h = 0

for i in range(0,7):
    for j in range(i+1,7):
        if positionList[i][0] == positionList[j][0]:
            h = h+1
        else:
            t1 = abs(positionList[i][0] - positionList[j][0])
            t2 = abs(positionList[i][1] - positionList[j][1])
            if t1 == t2:
                h = h+1

print("Heuristic 3: ",h)
print(type(positionList))
