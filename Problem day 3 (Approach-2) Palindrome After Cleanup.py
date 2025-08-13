def ispalindrome(s):
    cleaned=[]
    
    for i in range (len(s)):
        if s[i].isalnum():
            cleaned.append(s[i].lower())
        
    if ''.join(cleaned) ==''.join(reversed(cleaned)):
         return "YES"
    else:
        return "NO"

s= input().strip()

print(ispalindrome(s))