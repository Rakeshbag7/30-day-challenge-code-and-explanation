n, target = map(int, input().split())
nums = list(map(int, input().split()))

dp = [False] * (target + 1)
dp[0] = True

for num in nums:
    for j in range(target, num - 1, -1):
        dp[j] = dp[j] or dp[j - num]

if dp[target]:
    result = "YES"
    print(result)
else:
    result = "NO"
    print(result)

