def findLongestSubstring(sequence):
    startIndex = 0
    currentIndex = 0
    sol = 0
    seen = {}
    for char in sequence:
        if char in seen:
            lastSeenIndex = seen[char]
            if lastSeenIndex >= startIndex:
                startIndex = lastSeenIndex + 1
        seen[char] = currentIndex

        currentIndex += 1
        currentSubstringLength = currentIndex - startIndex
        if currentSubstringLength > sol:
            sol = currentSubstringLength
    
    return sol
