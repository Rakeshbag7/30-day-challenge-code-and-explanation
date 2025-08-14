def count_cleaned(s):
    cleaned=[]
    count=[]
    
    #step 1: clean (keep only letters & digits, lowercase) and convert the given string 
    for i in range (len(s)):
        if s[i].isalnum():
            cleaned.append(s[i].lower())
    
    #step 2: sort the cleaned and converted list 
    cleaned.sort()

    # Step 3: Count frequencies manually and store in 'count' list
    i = 0
    while i < len(cleaned):
        current = cleaned[i]
        freq = 1
        j = i + 1
        while j < len(cleaned) and cleaned[j] == current:
            freq += 1
            j += 1
        count.append([current, freq])
        i = j

    # Step 4: Print result
    for i in range(len(count)):
        print(count[i][0], ":", count[i][1])
        
   
s= input().strip()
if 1 <= len(s) <= 10**5:
    count_cleaned(s)