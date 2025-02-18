JuliaString = "АААФФФФФФФЖЫЫЫЫБЫРВАААААЛГГГХЫХЫБЛИА"

def filterUniqueChars(inString):
    resultUniqueChars = list()
    for currentChar in inString:
        alreadyExists = False
        for letter in resultUniqueChars:
            if letter == currentChar:
                alreadyExists = True
                break
        if (not alreadyExists):
            resultUniqueChars.append(currentChar)
    return resultUniqueChars

print(filterUniqueChars(JuliaString))