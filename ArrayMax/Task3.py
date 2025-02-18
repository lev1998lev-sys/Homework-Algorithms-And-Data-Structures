def findAverageNumber(inList):
    summation = 0
    for elem in inList:
        summation += elem
    return round((summation / len(inList)), 2)

timeSpentArray = [9, 4, 1, 8, 7, 9, 4, 1, 8, 7, 8, 7, 18, 3, 13, 6, 5]

print(findAverageNumber(timeSpentArray))