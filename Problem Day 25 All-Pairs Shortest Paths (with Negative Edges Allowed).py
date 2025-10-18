# Using Floyd-Warshall

# Finds all-pairs shortest paths in a directed weighted graph

def all_pairs_shortest_path():
    INF = float("inf")

    # number of vertices and edges
    n, m = map(int, input().split())

    # --- constraint check for graph size ---
    if 1 <= n <= 300 and 0 <= m <= n * (n - 1):
        # If valid then continue program
        pass
    else:
        return  # Invalid input, stop execution

    # Create distance matrix
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    # Read graph edges with positive constraint check
    for _ in range(m):
        u, v, w = map(int, input().split())
        if 1 <= u <= n and 1 <= v <= n and -10**6 <= w <= 10**6:
            u -= 1
            v -= 1
            if w < dist[u][v]:
                dist[u][v] = w
        else:
            return  # Invalid edge, stop execution

    # Main Floyd-Warshall loop
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Print the result matrix
    for i in range(n):
        row = []
        for j in range(n):
            row.append("INF" if dist[i][j] == INF else str(dist[i][j]))
        print(" ".join(row))


#------Main Program ----------------
all_pairs_shortest_path()
