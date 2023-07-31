def printDataList(dataList, title):
    """データリストを標準出力します。

    Parameters:
        dataList (list): データリスト
        title (string): タイトル
    """

    print("■" + title)
    # print(dataList)

    count = 1
    for data in dataList:
        countStr = str(count) + " 位"
        keyStr = str(data[0])
        valueStr = str(data[1])
        # print(countStr + "\t" + data)
        print(countStr + "," + keyStr + "," + valueStr)
        # print(data)
        count += 1

    print("■■■")


def printDataDictionary(dataDictionary, title):
    """データディクショナリを標準出力します。

    Parameters:
        dataDictionary (dictionary): データディクショナリ
        title (string): タイトル
    """

    print("■" + title)
    # print(dataDictionary)

    for key, value in dataDictionary.items():
        # print(countStr + "\t" + data)
        print(str(key) + "," + str(value))
        # print(data)

    print("■■■")
