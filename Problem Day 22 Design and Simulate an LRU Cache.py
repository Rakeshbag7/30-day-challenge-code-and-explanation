# Using LRU (Least Recently Used) Cache Simulation using OrderedDict

from collections import OrderedDict

def lru_cache_simulation(capacity, queries):
    # constraints checking for capacity 
    if 1 <= capacity <= 10**5 and 1 <= len(queries) <= 10**5:
        cache = OrderedDict()
        output = []

        for op in queries:
            if op[0] == "GET":
                k = int(op[1])
                # constraints checking for range
                if 0 <= k <= 10**9:
                    if k in cache:
                        v = cache.pop(k)  # Remove and re-insert to mark as recently used
                        cache[k] = v
                        output.append(v)
                    else:
                        output.append(-1)
                else:
                    output.append(-1)  # Treat invalid keys as not found
            else:  # PUT operation
                k, v = int(op[1]), int(op[2])
                # constraints checking for key & value 
                if 0 <= k <= 10**9 and 0 <= v <= 10**9:
                    if k in cache:
                        cache.pop(k)
                    elif len(cache) == capacity:
                        cache.popitem(last=False)  # Remove least recently used
                    cache[k] = v
        return output
    else:
        return []  # No processing if constraints not met


# Direct execution
c, q = map(int, input().split())
queries = [input().split() for _ in range(q)]

results = lru_cache_simulation(c, queries)

for res in results:
    print(res) # Print the result
