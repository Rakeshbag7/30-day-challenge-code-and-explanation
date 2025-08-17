# Read input
n = int(input())
arr = list(map(int, input().split()))

# Use a set to keep track of seen elements
seen = set()
unique_elements = []

# Iterate and collect only the first occurrence of each element
for num in arr:
    if num not in seen:
        seen.add(num)
        unique_elements.append(num)

# Print the result
print(' '.join(map(str, unique_elements)))
