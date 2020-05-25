def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(1, change + 1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        minCoins[cents] = coinCount
    return minCoins[change]


# print(dpMakeChange([1, 5, 10, 21, 25], 63, [0]*64))

def dpMakeChange2(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin -= thisCoin


def use2():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coinCount = [0] * (amnt + 1)
    coinUsed = [0] * (amnt + 1)

    print("make change for ", amnt, "requires")
    print(dpMakeChange2(clist, amnt, coinCount, coinUsed), "coins")
    print("they are:")
    printCoins(coinUsed, amnt)


use2()
