# value -> node's value
# count -> total number of nodes in the subtree rooted at this node (including itself)
# left  -> left child node
# right -> right child node


# Create a new node with count = 1 and no children
def create_node(val):
    
    return [val, 1, None, None]
# Insert val into BST (iteratively) and maintain subtree counts
def insert_iter(root, val):
   
    if root is None:
        return create_node(val)

    cur = root # Cur is a flag varriable
    while True:
        cur[1] += 1          # increment subtree count for this node
        if val < cur[0]:
            if cur[2] is None:
                cur[2] = create_node(val)
                break
            cur = cur[2]
        else:
            if cur[3] is None:
                cur[3] = create_node(val)
                break
            cur = cur[3]
    return root

# Find k-th smallest (1-indexed) iteratively using subtree counts
def kth_smallest_iter(root, k):
    cur = root
    while cur is not None:
        # Two-line leftcount assignment (safe)
        left_count = 0
        if cur[2]:
            left_count = cur[2][1]

        if k == left_count + 1:
            return cur[0]
        elif k <= left_count:
            cur = cur[2]
        else:
            k -= (left_count + 1)
            cur = cur[3]
    return None

# ---------------- Main Code ----------------

# Read inputs
n = int(input().strip())
arr = list(map(int, input().strip().split()))
k = int(input().strip())

# --- Constraints checks ---
valid_n = 1 <= n <= 10**5
valid_length = len(arr) == n
valid_values = all(1 <= x <= 10**9 for x in arr)  # per problem statement
unique_values = len(set(arr)) == n                # BST values are unique per statement
valid_k = 1 <= k <= n

if not (valid_n and valid_length and valid_values and unique_values and valid_k):
    print(-1)
else:
    # Build BST
    root = None
    for v in arr:
        root = insert_iter(root, v)

    ans = kth_smallest_iter(root, k)
    if ans is None:
        print(-1)
    else:
        print(ans)
