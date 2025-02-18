def findMaxElem(inList):
    maxElem = inList[0]
    if len(inList) != 0:
        for elem in inList:
            maxElem = max(maxElem, elem)
    return maxElem

belowZeroNumbers = [-1392, -1920, -7, -453, -91234]

print(findMaxElem(belowZeroNumbers))