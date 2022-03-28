class Graph:
    def __init__(self, graph):
        self.graph = graph

    def get_neighbors(self, v):
        return self.graph[v]

    def h(self, n):
        Heuristic = {'S': 10, 'A': 9, 'B': 7, 'C': 8, 'D': 8, 'H': 6, 'L': 6, 'F': 6, 'G': 3, 'I': 4, 'J': 4, 'K': 3, 'E': 0}
            
        return Heuristic[n]

    def A_star_algorithm(self, start_node, end_node):
         open_list = set([start_node])
         closed_list = set([])
         li = []
         g = {}
         g[start_node] = 0
         parents = {}
         parents[start_node] = start_node

         while len(open_list) > 0:
             n = None

             for v in open_list:
                 if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                     n = v

             if n == None:
                 print('Path does not exist!')
                 return None

             if n == end_node:
                 li.append(n)

                 print("Visited: ", li)
                 reconst_path = []

                 while parents[n] != n:
                     reconst_path.append(n)
                     n = parents[n]

                 reconst_path.append(start_node)

                 reconst_path.reverse()

                 print('Final Path: {}'.format(reconst_path))
                 return reconst_path

             for (m, weight) in self.get_neighbors(n):
                 if m not in open_list and m not in closed_list:
                     open_list.add(m)
                     parents[m] = n
                     g[m] = g[n] + weight

                 else:
                     if g[m] > g[n] + weight:
                         g[m] = g[n] + weight
                         parents[m] = n

                         if m in closed_list:
                             closed_list.remove(m)
                             open_list.add(m)

             li.append(n)
             print("Visited: ", li)
             open_list.remove(n)
             closed_list.add(n)

         print('Path does not exist!')
         return None

graph = {
     'S': [('A', 7), ('B', 2), ('C', 3)],
     'A': [('B', 3), ('D', 4)],
     'B': [('D', 4), ('H', 1)],
     'C': [('L', 2)],
     'D': [('F', 5)],
     'H': [('F', 3), ('G', 2)],
     'L': [('I', 4), ('J', 4)],
     'F': [],
     'G': [('E', 2)],
     'I': [('K', 4)],
     'J': [('K', 4)],
     'K': [('E', 5)],
     'E': []
}
graph1 = Graph(graph)
graph1.A_star_algorithm('S', 'E')
