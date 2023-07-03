

import pandas as pd


def readCsv(csvFilePath):
    """CSVファイルを読み込みます

    Parameters:
    ----------
    csvFilePath : str
        CSVファイルパス

    Returns:
    ----------
        CSVの内容 : [[CSV1行分],...]
    """
    dataList = pd.read_csv(csvFilePath).values.tolist()

    return dataList
