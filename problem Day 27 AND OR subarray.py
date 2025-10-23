# Brute-force algorithm

# check all subarrays

def largest_subarray_or_and(n, A, B):
    max_len = 0  # stores maximum valid subarray length
    for i in range(n):
        or_val = 0       # OR of current subarray from A
        and_val = B[i]   # AND of current subarray from B
        for j in range(i, n):
            or_val |= A[j]      # update OR with A[j]
            and_val &= B[j]     # update AND with B[j]
            if or_val == and_val:  # check condition
                max_len = max(max_len, j - i + 1)  # update max length
    return max_len


def solve():
    t = int(input())  # number of test cases

    # constraints: 1 <= T <= 10
    if 1 <= t <= 10:
        results = []  # to store answers for each test case
    else:
        return  # stop if T is invalid

    for k in range(t):
        n = int(input())  # size of arrays

        # constraints: 1 <= N <= 5*10^4
        if not (1 <= n <= 5 * 10**4):
            return  # stop if N is invalid

        A = list(map(int, input().split()))  # array A
        B = list(map(int, input().split()))  # array B

        # compute answer for this test case
        results.append(largest_subarray_or_and(n, A, B))

    # print all results, one per line
    for ans in results:
        print(ans)


#-------Main Program----------
solve()
