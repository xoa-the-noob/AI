def pathValue(x,y):
    if (x,y) in neighborList:
        return neighborDict[(x,y)]
    for (i, j) in neighborList:
        if i == x:
            t1 = neighborDict[(x, j)]
            t2 = pathValue(j,y)
            return t1+t2

neighborDict = {('a', 'd') : 7,('d', 'a') : 7, ('a', 'c') : 2,('c', 'a') : 2, ('c', 'b') : 3, ('b', 'c') : 3,
             ('b', 'e') : 1, ('e', 'b') : 1, ('e', 'h') : 3, ('h', 'e') : 3,
             ('g', 'h') : 6, ('h', 'g') : 6, ('f', 'g') : 4,('g', 'f') : 4}
neighborList = [('a', 'd'),('d', 'a'), ('a', 'c'),('c', 'a'), ('c', 'b'), ('b', 'c'),
             ('b', 'e'), ('e', 'b'), ('e', 'h'), ('h', 'e'),
             ('g', 'h'), ('h', 'g'), ('f', 'g'),('g', 'f')]

start = str(input('Enter Starting point: '))
end = str(input('Enter Ending point: '))
print('The length of path is: ')
print(pathValue(start, end))
