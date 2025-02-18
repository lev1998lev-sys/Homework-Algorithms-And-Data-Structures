import sys

def findMinAboveBoundary(inList, bottomBoundary):
    if (not isinstance(inList, list)) or (not isinstance(bottomBoundary, int)):
        raise TypeError("The first argument of the function must be a list container, the second an int number.")

    currentMax = sys.maxsize
    for elem in inList:
        if elem > bottomBoundary:
            currentMax = min(currentMax, elem)
    return currentMax

def findBottomElement(inList, numberOfElements):
    if (not isinstance(inList, list)) or (not isinstance(numberOfElements, int)):
        raise TypeError("The first argument of the function must be a list container, the second an int number.")
    if (numberOfElements > len(inList)):
        raise ValueError("Number of elements cannot be more size of list")
    bottomElements = list()
    previousMax = -sys.maxsize

    for i in range(numberOfElements):
        currentMax = findMinAboveBoundary(inList, previousMax)
        previousMax = currentMax
        bottomElements.append(currentMax)

    return bottomElements

ages = [34, 94, 33, 102, 45, 10, 14]
bottom3ages = findBottomElement(ages, 3)
print(bottom3ages)