

def convertToMapByNum(dataList):
    """１～６の番号ごとの出現回数をカウントします。

    Parameters
        dataList (list): データリスト[{No1,No2,No3,...}]

    Returns
        (dictionary): 番号ごとの出現回数Map

    Examples
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
                countDictionary[number] = 1

    return countDictionary

    # キー（Loto6番号）でソート
    ret = sorted(countDictionary.items())
    # 回数でソート
    # ret = sorted(countDictionary.items(), key=lambda x: x[1])
    # print(ret)
    # return ret


# セット球：出現回数のカウント
def convertToMapBySet(dataList):
    """セット球の出現回数のカウントします。

    Parameters
        dataList (list): データリスト[{No1,No2,No3,...}]

    Returns
        (dictionary): セット球ごとの出現回数Map

    Examples
        >>> convertToMapBySet({1,2,3,4,5,6},{3,4,5,7,12,16})
        {{A:1},{B:2},...}
    """

    # 数値ごとの回数をカウントしてマップ化
    countDictionary = {}
    for data in dataList:

        setNum = data[9]
        if setNum in countDictionary:
            countDictionary[setNum] += 1
        else:
            countDictionary[setNum] = 1

    return countDictionary

    # キー（Loto6番号）でソート
    # ret = sorted(countDictionary.items())
    # 回数でソート
    # ret = sorted(countDictionary.items(), key=lambda x: x[1])
    # print(ret)
    # return ret


def convertToMapByNumFilterSet(dataList, targetSetNum):
    """１～６の番号ごとの出現回数をカウントします。（セット球を指定）

    Parameters
        dataList (list): データリスト[{No1,No2,No3,...}]
        targetSetNum (string): 対象のセット球

    Returns
        (dictionary): 番号ごとの出現回数Map

    Examples
        >>> convertToMapByNum({1,2,3,4,5,6},{3,4,5,7,12,16})
        {{1:1},{2:2},...}
    """

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
                countDictionary[number] = 1

    return countDictionary

    # キー（Loto6番号）でソート
    # ret = sorted(countDictionary.items())
    # 回数でソート
    # ret = sorted(countDictionary.items(), key=lambda x: x[1])
    # print(ret)
    # return ret
