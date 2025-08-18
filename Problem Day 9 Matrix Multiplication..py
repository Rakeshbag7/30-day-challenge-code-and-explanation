def multiplication_of_matrices(A, B, p, q, r):
    # Initialize result matrix C as p x r matrix filled with 0
    C = []
    for i in range(p):
        row = []
        for j in range(r):
            row.append(0)
        C.append(row)

    # Perform matrix multiplication
    for i in range(p):
        for j in range(r):
            for k in range(q):
                C[i][j] += A[i][k] * B[k][j]

    return C

# -------- Main Program --------
p, q, r = map(int, input().split())

# Read matrix A (p x q)
A = []
for i in range(p):
    row = list(map(int, input().split()))
    A.append(row)

# Read matrix B (q x r)
B = []
for i in range(q):
    row = list(map(int, input().split()))
    B.append(row)

# -------- Matrix Element Constraints Validation --------
valid_A = True
for i in range(p):
    for j in range(q):
        if not (-10**4 <= A[i][j] <= 10**4):
            valid_A = False
            break
    if not valid_A:
        break

valid_B = True
for i in range(q):
    for j in range(r):
        if not (-10**4 <= B[i][j] <= 10**4):
            valid_B = False
            break
    if not valid_B:
        break

# -------- Final Check Before Multiplication --------
if 1 <= p <= 200 and 1 <= q <= 200 and 1 <= r <= 200:
    if valid_A:
        if valid_B:
            C = multiplication_of_matrices(A, B, p, q, r)
            
#_________ Print result matrix C____________
            for row in C:
                print(" ".join(map(str, row)))
