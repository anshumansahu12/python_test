from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(start):
    visited = set() # track of nodes
    queue = deque([start])


    while queue:
        node = queue.popleft()#using popleft first element was removed 
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

bfs('A')