def findMinElem(inList):
    if len(inList) != 0:
        minElem = inList[0]
        for elem in inList:
            minElem = min(minElem, elem)
    return minElem

minValueArray = [9, 4, 1, 8, 7, 13, 6, 5]

print(findMinElem(minValueArray))