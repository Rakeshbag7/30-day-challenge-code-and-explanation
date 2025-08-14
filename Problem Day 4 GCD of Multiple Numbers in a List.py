def gcd_of_list(a, n):
    gcd = a[0]
    temp = 0

    for i in range(1, len(a)):
        x = gcd
        y = a[i]

        if x == 0 and y == 0:
            continue
        elif x == 0:
            gcd = y
            continue
        elif y == 0:
            gcd = x
            continue

        while y != 0:
            temp = y
            y = x % y
            x = temp
        gcd = x

    return gcd


n = int(input())
a = list(map(int, input().split()))
print(gcd_of_list(a, n))
