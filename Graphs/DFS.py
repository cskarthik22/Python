
graph = {
    'A': set(['B','C']),
    'B': set(['A','D','E']),
    'C': set(['A','F']),
    'D': set(['B']),
    'E': set(['B','F']),
    'F': set(['C','E'])
}

def dfs(graph,startVertex):
    visited = set()
    stack = [startVertex]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    return visited

def bfs(graph,startVertex):
    visited = set()
    queue = [startVertex]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            
            queue.extend(graph[vertex] - visited)
    return visited

print(dfs(graph,'A'))
print(bfs(graph,'C'))


