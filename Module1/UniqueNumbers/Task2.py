statements = [[12391203, 3828382, 334934939], [45345345, 5341312, 55345345], [334934939, 1234122, 657657]]

def countNumberOfElement(inListDouble, inElement):
    summation = 0
    for elemList in inListDouble:
        for elem in elemList:
            if elem == inElement:
                summation += 1
    return summation

def repeatedValue(inStatements):
    for payout in inStatements:
        for producer in payout:
            if (countNumberOfElement(inStatements, producer) > 1):
                return producer
    return -1

print(repeatedValue(statements))