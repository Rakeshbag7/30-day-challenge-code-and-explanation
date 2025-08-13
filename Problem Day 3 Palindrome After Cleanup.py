def ispalindrome(s):
    cleaned=""
    
    for i in range (len(s)):
        if s[i].isalnum():
            cleaned+=s[i].lower()
        
    if cleaned == ''.join(reversed(cleaned)):
        
         return "YES"
    else:
        return "NO"

s= input().strip()

print(ispalindrome(s))