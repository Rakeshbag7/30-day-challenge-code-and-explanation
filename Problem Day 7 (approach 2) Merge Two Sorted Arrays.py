# Read input
n = int(input())
r = list(map(int, input().split()))
m = int(input())
s = list(map(int, input().split()))

# Check constraints using if-ladder with positive conditions
if 1 <= n <= 10**5 and 1 <= m <= 10**5:
    if len(r) == n and len(s) == m:
        if all(-10**9 <= x <= 10**9 for x in r + s):
            # Both arrays are sorted as per the problem, perform manual merge
            i = j = 0
            merged = []

            while i < n and j < m:
                if r[i] <= s[j]:
                    merged.append(r[i])
                    i += 1
                else:
                    merged.append(s[j])
                    j += 1

            # Append remaining elements from either array
            while i < n:
                merged.append(r[i])
                i += 1

            while j < m:
                merged.append(s[j])
                j += 1

# Print result
print(" ".join(map(str, merged)))
       