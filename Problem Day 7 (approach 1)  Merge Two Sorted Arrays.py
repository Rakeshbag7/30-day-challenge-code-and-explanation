# Two pointer concept
def merge_sorted_arrays(n, r, m, s):
    # Use positive logic to validate constraints
    if 1 <= n <= 10**5 and 1 <= m <= 10**5:
        if len(r) == n and len(s) == m:
            if all(-10**9 <= x <= 10**9 for x in r + s):

                # Merge logic
                i = j = 0
                merged = []

                while i < n and j < m:
                    if r[i] <= s[j]:
                        merged.append(r[i])
                        i += 1
                    else:
                        merged.append(s[j])
                        j += 1

                while i < n:
                    merged.append(r[i])
                    i += 1

                while j < m:
                    merged.append(s[j])
                    j += 1

                return merged  # All checks passed and merged list created

   # return [] # If any condition fails


n = int(input())
r = list(map(int, input().split()))
m = int(input())
s = list(map(int, input().split()))

merged = merge_sorted_arrays(n, r, m, s)


print(" ".join(map(str, merged)))
