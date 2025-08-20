def rotatethearray(arr, k): #------function deefinition-------
    n = len(arr)
    k = k % n  # ---- Handle large k by taking modulo with n ----
    
    # ---- Perform right rotation k times ----
    for i in range(k):
        last = arr[-1]  # Store the last element
        for j in range(n - 1, 0, -1):
            arr[j] = arr[j - 1]  # Shift elements to the right
        arr[0] = last  # Place the last element at the beginning

    return arr

# ---- Main Program ----
n, k = map(int, input().split())  # Read size and rotation count
arr = list(map(int, input().split()))  # Read array elements

# ---- Validate input constraints ----
if 1 <= n <= 10**5 and 0 <= k <= 10**9:
    valid = True
    for x in arr:
        if x < -10**9 or x > 10**9:
            valid = False
            break

    # ---- Perform rotation and output result ----
    if valid:
        result = rotatethearray(arr, k)
        print(" ".join(map(str, result)))
