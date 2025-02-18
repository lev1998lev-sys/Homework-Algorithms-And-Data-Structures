currencies = ["BTC", "BTC", "BTC", "DOGE", "DOGE", "ETH", "ETH", "XMR", "XMR"]
investments = [42, 600, 900, 123456, 69420, 220, 666, 14, 88]

def averageInvestmentInCurrency(inCurrencies, inInvestments):
    previousCurrency = inCurrencies[0]
    summation = 0
    accountOfRecords = 0
    for i in range(len(inCurrencies)):
        if (inCurrencies[i] == previousCurrency):
            summation += inInvestments[i]
            accountOfRecords += 1
        else:
            print(previousCurrency, ": ", summation / accountOfRecords)
            previousCurrency = inCurrencies[i]
            summation = investments[i]
            accountOfRecords = 1
    print(previousCurrency, ": ", summation / accountOfRecords)

averageInvestmentInCurrency(currencies, investments)