def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1+recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins


def recDC(coinValueList, change, konwResults):
    minCoins = change
    if change in coinValueList:
        konwResults[change] = 1
        return 1
    elif konwResults[change] > 0:
        return konwResults[change]
    for i in [c for c in coinValueList if c <= change]:
        numCoins = 1+recDC(coinValueList, change-i, konwResults)
        if numCoins < minCoins:
            minCoins = numCoins
            konwResults[change] = minCoins
    return minCoins


print(recDC([1, 5, 10, 25], 63, [0]*64))
