import sys

def findMaxUnderBoundary(inList, topBoundary):
    if (not isinstance(inList, list)) or (not isinstance(topBoundary, int)):
        raise TypeError("The first argument of the function must be a list container, the second an int number.")

    currentMax = -sys.maxsize
    for elem in inList:
        if elem < topBoundary:  #в условии вместо "<" теперь используется "<="
            currentMax = max(currentMax, elem)

    accountOfMaxElem = list()
    for elem in inList:
        if elem == currentMax:
            accountOfMaxElem.append(elem);
    return accountOfMaxElem

def findTopElement(inList, numberOfElements):
    if (not isinstance(inList, list)) or (not isinstance(numberOfElements, int)):
        raise TypeError("The first argument of the function must be a list container, the second an int number.")
    if (numberOfElements > len(inList)):
        raise ValueError("Number of elements cannot be more size of list")
    topElements = list()
    previousMax = sys.maxsize
    i = 0
    while(i < numberOfElements):
        currentMax = findMaxUnderBoundary(inList, previousMax)
        i += len(currentMax)
        previousMax = currentMax[0]
        topElements += currentMax

    return topElements[:numberOfElements]

top3ages = findTopElement([100, 100, 100, 55, 8], 3)

print(top3ages)