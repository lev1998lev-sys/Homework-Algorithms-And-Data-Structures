phoneRegistry = [+79000000001, +79000000001, +79000000002, +79000000003, +79000000003, +79000000004, +79000000004, +79000000004, +79000000004, +79000000005]

def countNumberOfElement(inList, inElement):
    summation = 0
    for elem in inList:
        if (elem == inElement):
            summation += 1
    return summation

def showPhoneCalls(inPhoneRegistry):
    resultUniquePhoneNumbers = list()
    for phoneNumber in inPhoneRegistry:
        alreadyExists = False
        for currentNumber in resultUniquePhoneNumbers:
            if currentNumber == phoneNumber:
                alreadyExists = True
        if (not alreadyExists):
            resultUniquePhoneNumbers.append(phoneNumber)
            print(phoneNumber, " - поступило заявок: ", countNumberOfElement(inPhoneRegistry, phoneNumber))

showPhoneCalls(phoneRegistry)