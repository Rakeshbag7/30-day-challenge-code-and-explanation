from collections import deque

def min_steps(A, B):
    q = deque([(A, 0)])
    visited = set([A])

    while q:
        val, steps = q.popleft()

        if val == B:
            return steps

        for nxt in (val + 3, val - 2):
            if 1 <= nxt <= 100 and nxt not in visited:
                visited.add(nxt)
                q.append((nxt, steps + 1))

    return -1  

A, B = map(int, input().split())
print(min_steps(A, B))


