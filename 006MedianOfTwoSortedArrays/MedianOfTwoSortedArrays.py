# TODO: calculated in O(m+n) complexity, but the goal is O(log(n + m))

def calculateMedian(firstSequence, secondSequence):
    mergedSorted = mergeSorted(firstSequence, secondSequence)
    
    mergedLength = len(mergedSorted)
    if mergedLength % 2 == 1:
        return mergedSorted[mergedLength // 2]
    else:
        secondSummandIndex = mergedLength // 2
        firstSummandIndex = secondSummandIndex - 1
        return (mergedSorted[firstSummandIndex] + mergedSorted[secondSummandIndex]) / 2
    
def mergeSorted(firstSequence, secondSequence):
    firstSeqLength = len(firstSequence)
    secondSeqLength = len(secondSequence)
    curFirstSeqIndex = 0
    curSecondSeqIndex = 0
    mergedSorted = []
    while curFirstSeqIndex < firstSeqLength or curSecondSeqIndex < secondSeqLength:
        if curFirstSeqIndex < firstSeqLength and curSecondSeqIndex < secondSeqLength:   # both arrays provide elements        
            firstSeqEl = firstSequence[curFirstSeqIndex]
            secondSeqEl = secondSequence[curSecondSeqIndex]
            if firstSequence[curFirstSeqIndex] < secondSequence[curSecondSeqIndex]:
                mergedSorted.append(firstSeqEl)
                curFirstSeqIndex += 1
            else:
                mergedSorted.append(secondSeqEl)
                curSecondSeqIndex += 1
        elif curFirstSeqIndex < firstSeqLength and curSecondSeqIndex >= secondSeqLength:    # only first array provides elements
            mergedSorted.append(firstSequence[curFirstSeqIndex])
            curFirstSeqIndex += 1
        else:   # only second array provides elements
            mergedSorted.append(secondSequence[curSecondSeqIndex])
            curSecondSeqIndex += 1
    return mergedSorted
