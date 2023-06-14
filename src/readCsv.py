

import pandas as pd

def readCsv(csvFilePath):
    """CSVファイルを読み込みます

    Parameters:
    ----------
    x : string csvFilePath
        operand1 of addition

    Returns:
    ----------
    string
        CSVの内容
    """
    dataList = pd.read_csv(csvFilePath).values.tolist()

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
