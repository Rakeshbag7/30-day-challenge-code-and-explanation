def second_largest_distinct(arr):
    n = len(arr)

    # Check constraints using positive logic
    if 2 <= n <= 10**5:
        if all(-10**9 <= x <= 10**9 for x in arr):
            first = float('-inf')
            second = float('-inf')

            for num in arr:
                if num > first:
                    second = first
                    first = num
                else:
                    if num != first and num > second:
                        second = num

            if second != float('-inf'):
                return second
            else:
                return "NO"
        else:
            return "NO"
    else:
        return "NO"


n = int(input())
arr = list(map(int, input().split()))

result = second_largest_distinct(arr)
print(result)
