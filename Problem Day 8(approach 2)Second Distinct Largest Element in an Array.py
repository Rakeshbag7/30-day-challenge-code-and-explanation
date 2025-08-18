# using tree-set
def second_largest_with_treeset(arr):
    n = len(arr)

    # Apply constraints positively
    if 2 <= n <= 10**5 and all(-10**9 <= x <= 10**9 for x in arr):
        # Use set to remove duplicates
        unique_elements = set(arr)

        # Check if at least two distinct elements exist
        if len(unique_elements) >= 2:
            # Sort the set in ascending order
            sorted_elements = sorted(unique_elements)
            # Return the second largest (2nd last)
            return sorted_elements[-2]
        else:
            return "NO"
    else:
        return "NO"


n = int(input())
arr = list(map(int, input().split()))

result = second_largest_with_treeset(arr)
print(result)
