# Problem 2667:

def dfs(i, j, n):
    # check for within bounds of map, and if no house
    if i < 0 or i >= n or j < 0 or j >= n or graph[i][j] == '0':
        return 0
    
    # amrk as visited and inc count
    graph[i][j] = '0'
    c = 1
    
    # run same up, down, right, left to check for neighboring houses, add to count
    c += dfs(i + 1, j, n) 
    c += dfs(i - 1, j, n) 
    c += dfs(i, j + 1, n) 
    c += dfs(i, j - 1, n) 
    
    return c

# run code
n = int(input())

# turns into list of lists for traversal
graph = []

for i in range(n):
    line = input().strip()
    row = list(line)
    graph.append(row)

groupcount = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            size = dfs(i, j, n)
            groupcount.append(size)

print(len(groupcount))
groupcount.sort()
for size in groupcount:
    print(size)













