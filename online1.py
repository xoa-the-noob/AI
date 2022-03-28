def pathValue(x,y):
    if (x,y) in neighborList:
        return neighborDict[(x,y)]
    for (i, j) in neighborList:
        if i == x:
            t1 = neighborDict[(x, j)]
            t2 = pathValue(j,y)
            return t1+t2

neighborDict = {('i', 'a') : 35, ('i', 'b') : 45, ('a', 'c') : 22, ('a', 'd') : 32,
             ('b', 'd') : 28, ('b', 'e') : 36, ('b', 'f') : 27, ('c', 'd') : 31,
             ('c', 'g') : 47, ('d', 'g') : 30, ('e', 'g') : 26}
neighborList = [('i', 'a'), ('i', 'b'), ('a', 'c'), ('a', 'd'),
            ('b', 'd'), ('b', 'e'), ('b', 'f'), ('c', 'd'),
            ('c', 'g'), ('d', 'g'), ('e', 'g')]

start = str(input('Enter Starting point: '))
end = str(input('Enter Ending point: '))
print('The length of path is: ')
print(pathValue(start, end))
