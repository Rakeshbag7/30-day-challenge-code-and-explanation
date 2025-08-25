# Read the number of nodes
n = int(input())

# Read the values of the linked list nodes
arr = list(map(int, input().split()))

# Read the position to form a cycle (-1 if no cycle)
pos = int(input())

# ---------- Constraint Checks ----------

# Check if number of nodes is within valid range
if 0 <= n <= 10**5:
    valid_n = True
else:
    valid_n = False

# Check if pos is either -1 or a valid index within the list
if pos == -1:
    valid_pos = True
elif 0 <= pos < n:
    valid_pos = True
else:
    valid_pos = False



# Check if the number of elements in the list matches n
if len(arr) == n:
    valid_length = True
else:
    valid_length = False

# Check if all node values are within the valid range
if all(-10**9 <= x <= 10**9 for x in arr):
    valid_values = True
else:
    valid_values = False

# ---------- Main Logic ----------

# Only proceed if all input constraints are valid
if valid_n and valid_pos and valid_length and valid_values:
    
    # Create the 'next' pointers for the linked list
    nexts = [-1] * n  # Initialize all as -1 (no next node)
    for i in range(n - 1):
        nexts[i] = i + 1  # Point each node to the next node
    
    # If there's a cycle, connect last node to the 'pos' node
    if pos != -1:
        nexts[n - 1] = pos

    # Apply Floyd's Cycle Detection Algorithm
    slow = fast = 0  # Start both pointers at the head

    while fast != -1 and nexts[fast] != -1:
        slow = nexts[slow]           # Move slow by 1 step
        fast = nexts[nexts[fast]]    # Move fast by 2 steps

        if slow == fast:
            print("true")  # Cycle detected
            break
    else:
        print("false")  # No cycle found

else:
    # If any constraint fails, return false
    print("false")

