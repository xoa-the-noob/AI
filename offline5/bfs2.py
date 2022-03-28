import copy

heuristic = {'S': 10, 'A': 9, 'B': 7, 'C': 8, 'D': 8, 'H': 6, 'L': 6, 'F': 6, 'G': 3, 'I': 4, 'J': 4, 'K': 3, 'E': 0}

traversal = {
    'S': ['A', 'B', 'C'],
    'A': ['B', 'D'],
    'B': {'H', 'D'},
    'C': ['L'],
    'D': ['F'],
    'H': ['F', 'G'],
    'L': ['I', 'J'],
    'G': ['E'],
    'I': ['K'],
    'J': ['K'],
    'K': ['E']
}


def Best_First_Search(start, end):
    path = []
    Q = []
    priorityQueue = [[[start], heuristic[start]]]
    visited = []

    while priorityQueue != []:
        Q = priorityQueue.copy()
        path.append(priorityQueue.pop(0))
        node = path[-1][0][-1]
        visited.append(node)

        if node == end:
            finalPath = copy.deepcopy(path[-1])
            print("Final Path", finalPath[0:1])
            return "Found"

        for neighbor in traversal[node]:
            if neighbor not in visited:
                newPath = copy.deepcopy(path[-1])
                newPath[0].append(neighbor)
                newPath[1] = heuristic[neighbor]
                priorityQueue.append(newPath)

        priorityQueue.sort(key=lambda x: x[1])
    print("Visited", visited)

Best_First_Search('S', 'E')
