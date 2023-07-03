
# １～６の番号：出現回数のカウント
def convertToMapByNum(dataList):
    """
    番号ごとの出現回数をカウントします。

    Parameters
    ----------
    dataList : list
        データリスト[{No1,No2,No3,...}]

    Returns
    ----------
        番号ごとの出現回数Map

    Examples
    --------
    >>> convertToMapByNum({1,2,3,4,5,6},{3,4,5,7,12,16})
    {{1:1},{2:2},...}

    """

    # 数値ごとの回数をカウントしてマップ化
    countDictionary = {}
    for data in dataList:
        # print('■')
        for i in range(6):
            # print(data[i])
            number = data[i]
            if number in countDictionary:
                countDictionary[number] += 1
            else:
                countDictionary[number] = 0

    # # キー（Loto6番号）でソート
    # print(sorted(countDictionary.items()))
    # return sorted(countDictionary.items())

    # print("-------")

    # # 回数でソート
    # print(sorted(countDictionary.items(), key=lambda x: x[1]))
    return sorted(countDictionary.items(), key=lambda x: x[1])


# セット球：出現回数のカウント
def convertToMapBySet(dataList):

    # 数値ごとの回数をカウントしてマップ化
    countDictionary = {}
    for data in dataList:

        setNum = data[9]
        if setNum in countDictionary:
            countDictionary[setNum] += 1
        else:
            countDictionary[setNum] = 0

    # # キー（Loto6番号）でソート
    # print(sorted(countDictionary.items()))
    # return sorted(countDictionary.items())

    # print("-------")

    # # 回数でソート
    # print(sorted(countDictionary.items(), key=lambda x: x[1]))
    return sorted(countDictionary.items(), key=lambda x: x[1])


# １～６の番号：出現回数のカウント（セット球を指定）
def convertToMapByNumFilterSet(dataList, targetSetNum):

    # 数値ごとの回数をカウントしてマップ化
    countDictionary = {}
    for data in dataList:

        setNum = data[9]
        if (targetSetNum != setNum):
            continue

        for i in range(6):
            # print(data[i])
            number = data[i]
            if number in countDictionary:
                countDictionary[number] += 1
            else:
                countDictionary[number] = 0

    # # キー（Loto6番号）でソート
    # print(sorted(countDictionary.items()))
    # return sorted(countDictionary.items())

    # print("-------")

    # # 回数でソート
    # print(sorted(countDictionary.items(), key=lambda x: x[1]))
    return sorted(countDictionary.items(), key=lambda x: x[1])
