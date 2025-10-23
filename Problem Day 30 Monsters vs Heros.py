import sys
import bisect

input = sys.stdin.readline

n, q = map(int, input().split())
positions = [[] for _ in range(100001)]

total = 0

for _ in range(n):
    l, r, s = map(int, input().split())
    for pos in range(l, r+1):
        positions[pos].append(s)
    total += (r - l + 1)

for pos in range(100001):
    if positions[pos]:
        positions[pos].sort()

answers = []
curr_total = total

for _ in range(q):
    x, p = map(int, input().split())
    arr = positions[x]
    if arr:
        idx = bisect.bisect_left(arr, p)  
        if idx > 0:
            curr_total -= idx
            positions[x] = arr[idx:] 
    answers.append(str(curr_total))

print(" ".join(answers))
