# Using prefix sum based algo

def process_queries(n, q, arr, queries):
    # Prefix sum array for fast range sum calculation
    s = [0] * (n + 1)
    for i in range(n):
        s[i+1] = s[i] + arr[i]  # s[i+1] = sum of first i+1 elements

    # Update function: updates element at index i to value x
    def upd(i, x):
        # Calculate the difference between new value and old value
        d = x - arr[i-1]
        arr[i-1] = x  # Update original array
        # Update prefix sums from index i to end
        for j in range(i, n+1):
            s[j] += d

    # Range sum function: returns sum from index l to r (1-based indexing)
    def rng(l, r):
        return s[r] - s[l-1]

    output = []
    for query in queries:
        t, *v = query
        if t == 1:
            # Type 1 query -> Update
            upd(v[0], v[1])
        else:
            # Type 2 query -> Range sum
            output.append(rng(v[0], v[1]))
    return output


# ---- MAIN PROGRAM ----
n, q = map(int, input().split())  # Number of elements and queries
arr = list(map(int, input().split()))  # Initial array
queries = []
for x in range(q):
    queries.append(list(map(int, input().split())))

# Process and get results
results = process_queries(n, q, arr, queries)

# Output results for all Type 2 queries
for res in results:
    print(res)