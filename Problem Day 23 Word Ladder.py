# Using BFS 

# Function to find shortest transformation from beginWord to endWord
def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    if endWord in wordList:   # Only possible if endWord is in list
        nei = {}              # Pattern to  words mapping
        wordList.append(beginWord)

        # Build adjacency list using patterns
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                if pattern not in nei:
                    nei[pattern] = []
                nei[pattern].append(word)

        visit = set([beginWord])   # Track visited words
        q = [beginWord]            # BFS queue
        res = 1                    # Transformation count

        while q:
            new_q = []
            for word in q:
                if word == endWord:   # Found answer
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei.get(pattern, []):
                        if neiWord not in visit:
                            visit.add(neiWord)
                            new_q.append(neiWord)
            q = new_q
            res += 1
        return 0
    else:
        return 0

#---------- Main Code ------------
# -------- Input Handling --------
beginWord = input().strip()
endWord = input().strip()
n = int(input().strip())
wordList = [input().strip() for i in range(n)]

# Check constraints
if 1 <= n <= 10**4:
    valid = True
    for x in wordList:
        if not (1 <= len(x) <= 10 and x.islower()):
            valid = False
            break
else:
    valid = False

# Run only if constraints are valid
if valid:
    print(ladderLength(beginWord, endWord, wordList))
else:
    print(0)
