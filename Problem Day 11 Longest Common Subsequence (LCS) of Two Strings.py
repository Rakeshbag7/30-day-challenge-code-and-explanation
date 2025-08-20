def lcs(A, B):
    n = len(A)
    m = len(B)

    # Create a (n+1) x (m+1) matrix table initialized with 0
    matrix = []
    for i in range(n + 1):
        row = [0] * (m + 1)
        matrix.append(row)

    # Build the table in a bottom-up manner using positive logic
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    # The bottom-right cell contains the length of LCS
    return matrix[n][m]

# Input reading
A = input().strip()
B = input().strip()

# Output
print(lcs(A, B))
