def arraysIntersection(elemsFirst, elemsSecond):
    elemsFirstUnique = set(elemsFirst)
    sol = set()
    for elem in elemsSecond:
        if elem in elemsFirstUnique:
            sol.add(elem)
    return list(sol)
