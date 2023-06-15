

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

    return dataList
