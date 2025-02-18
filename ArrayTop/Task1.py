import sys

def findMaxUnderBoundary(inList, topBoundary):
    if (not isinstance(inList, list)) or (not isinstance(topBoundary, int)):
        raise TypeError("The first argument of the function must be a list container, the second an int number.")

    currentMax = -sys.maxsize
    for elem in inList:
        if elem < topBoundary:
            currentMax = max(currentMax, elem)
    return currentMax

def findTopElement(inList, numberOfElements):
    if (not isinstance(inList, list)) or (not isinstance(numberOfElements, int)):
        raise TypeError("The first argument of the function must be a list container, the second an int number.")
    if (numberOfElements > len(inList)):
        raise ValueError("Number of elements cannot be more size of list")
    topElements = list()
    previousMax = sys.maxsize

    for i in range(numberOfElements):
        currentMax = findMaxUnderBoundary(inList, previousMax)
        previousMax = currentMax
        topElements.append(currentMax)

    return topElements

ages = [34, 94, 33, 102, 45, 10, 14]
top3ages = findTopElement(ages, 3)

print(top3ages)