def countElsWithMaxFreq(elems):
    sol = 0
    maxFreq = 0
    occurenceFreq = {}
    for el in elems:
        if el not in occurenceFreq:
            occurenceFreq[el] = 1
        else:
            occurenceFreq[el] += 1

        if maxFreq < occurenceFreq[el]:
            maxFreq = occurenceFreq[el]
            sol = maxFreq
        elif maxFreq == occurenceFreq[el]:
            sol += maxFreq
    return sol
