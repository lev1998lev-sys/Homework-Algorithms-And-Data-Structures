def findMostProfitable(inCustomersByDay):
    result = list()
    for customer in inCustomersByDay:
        summation = 0
        for incomePerDay in customer:
            summation += incomePerDay
        result.append(summation)
    maxElem = result[0]
    index = 0
    for i in range(len(result)):
        if result[i] > maxElem:
            maxElem = result[i]
            index = i
    return index

customers = [[95, 67, 13, 55, 44, 11, 10], [7,190, 4, 44, 11, 1, 99], [0, 5, -1, 500, 14, 90, 1]]

print(findMostProfitable(customers))