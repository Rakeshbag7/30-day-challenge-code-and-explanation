# Dynamic Programming with State Compression (Kadane's Algorithm with up to K deletions)

# Compute the maximum sum of a non-empty subarray after deleting at most K elements
def maxSumAfterKDeletions(n: int, K: int, A: list[int]) -> int:
    # Run only if all constraints are satisfied
    if not (1 <= n <= 10**5):
        return 0
    if not (0 <= K <= 10):
        return 0
    for x in A:
        if not (-10**9 <= x <= 10**9):
            return 0

    # dp[j] = best subarray sum ending at current index with at most j deletions
    dp = [-10**18] * (K + 1)
    ans = -10**18

    for x in A:
        new = [-10**18] * (K + 1)
        for j in range(K + 1):
            # Case 1: Take current element (extend or start new subarray)
            take = max(dp[j] + x, x)
            new[j] = max(new[j], take)

            # Case 2: Delete current element (if deletions left)
            if j > 0:
                new[j] = max(new[j], dp[j - 1])

        dp = new
        ans = max(ans, max(dp))

    return ans

# -------- Main Program -------------------
n, K = map(int, input().split())
A = list(map(int, input().split()))
print(maxSumAfterKDeletions(n, K, A))
