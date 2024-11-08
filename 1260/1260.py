# Problem 1260:

from collections import defaultdict, deque

def dfs(g, startnode, visited):
    # visited is stack for dfs
    visited.append(startnode)

    # for all neighbors of the start node in ascending order
    for neighbor in sorted(g[startnode]):
        # if the neighbor hasn't been visited
        if neighbor not in visited:
            # run dfs on that vertex (go deeper into it's children etc)
            dfs(g, neighbor, visited)

    return visited

def bfs(g, startnode):
    visited = []
    queue = deque([startnode])

    # while there are values in the queue
    while queue:
        # dequeue the next vertex
        vertex = queue.popleft()
        # if the vertex hasn't been visited
        if vertex not in visited:
            # add it to visited list
            visited.append(vertex)
            # add all neighbors in ascending order (as specified in problem) to the queue
            # backtrack to visit all neighbors that were previously unvisited after reaching depth
            queue.extend(sorted(g[vertex]))
    # return the visit order of graph nodes
    return visited


# run code
n, m, v = map(int, input().split())

# provides key value for values that don't exist
# creates adjacency list for the graph (googled for the defaultdict tbh)
graph = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)

dfs_result = dfs(graph, v, [])
bfs_result = bfs(graph, v)

print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))


