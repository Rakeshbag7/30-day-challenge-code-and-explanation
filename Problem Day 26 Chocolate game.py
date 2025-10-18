# Using Euclidean Algorithm 
# Count chocolate game steps

def chocolate_game(a, b):
    steps = 0
    while a > 0 and b > 0:
        if a >= b:
            steps += a // b
            a %= b
        else:
            steps += b // a
            b %= a
    return steps


# main program
a, b = map(int, input().split())
print(chocolate_game(a, b))
