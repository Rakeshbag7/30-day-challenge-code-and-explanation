# Read n = size of array, q = number of queries
n, q = map(int, input().split())

# Check if n and q are within valid constraints
if 1 <= n <= 10**5 and 1 <= q <= 10**5:
    
# Read the array and check if elements are within the valid range
    arr = list(map(int, input().split()))
    if len(arr) == n:
        validvalues = True
        for value in arr:
            if value < -10000 or value > 10000:
                validvalues = False
                break

        if validvalues:
            # Create prefix sum array (simple version)
            prefix = []
            for i in range(n + 1):
                prefix.append(0)

            # Fill prefix sum values
            for j in range(n):
                prefix[j + 1] = prefix[j] + arr[j]

            # Handle each query
            for k in range(q):
                l, r = map(int, input().split())

                # Check if L and R are within valid constraints
                if l >= 1 and r >= l and r <= n:
                    result = prefix[r] - prefix[l - 1]
                    print(result)
               
