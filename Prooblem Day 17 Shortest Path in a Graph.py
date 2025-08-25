# Read inputs
n, m, s, t = map(int, input().split())

# Build adjacency list
graph = []
for n in range(n + 1):
    graph.append([])

for x in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# Dijkstra alogrithm
dist = []
for i in range(n + 1):
    dist.append(float('inf'))

visited = []
for j in range(n + 1):
    visited.append(False)

dist[s] = 0

for k in range(n):
    # Pick the unvisited node with the smallest distance
    u = -1
    min_dist = float('inf')
    for i in range(1, n + 1):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i
    
    if u == -1:
        break  # No more reachable nodes
    
    visited[u] = True
    
   # Update shortest distances
    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w

# Print the result
if dist[t] != float('inf'):
    print(dist[t])
else:
    print(-1)
