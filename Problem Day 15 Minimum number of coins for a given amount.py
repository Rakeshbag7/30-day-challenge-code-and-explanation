# Read number of coins and target amount
n, amount = map(int, input().split())

# Read coin denominations
coins = list(map(int, input().split()))

# Initialize an array with 'infinity' (for large value)
x = []
for k in range(amount + 1):
    x.append(float('inf'))

# Base case: 0 coins needed to make amount 0
x[0] = 0

# Fill the  array
for j in coins:
    for i in range(j, amount + 1):
        if x[i - j] != float('inf'):
            x[i] = min(x[i], x[i - j] + 1)

# Print result
if x[amount] == float('inf'):
    print(-1)
else:
    print(x[amount])
