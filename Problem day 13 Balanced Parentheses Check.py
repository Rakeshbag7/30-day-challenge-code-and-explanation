# -------- Function to check if brackets are balanced using dictionary --------
def BalancedParentheses(s):
    stack = []  # Stack to hold opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}  # Matching pairs

    for char in s:
        if char in bracket_map.values():  # If it's an opening bracket
            stack.append(char)
        else:  # If it's a closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()

    if len(stack) == 0:
        
        return True  # True if all brackets matched
    else:
        return False  

# -------- Main Program --------
s = input().strip()

# Check length and character constraint
if 1 <= len(s) <= 100000:
    
    if BalancedParentheses(s): # Print the result
        print("YES")
    else:
        print("NO")
