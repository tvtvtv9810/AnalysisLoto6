import pandas as pd


def readCsv(csvFilePath):
    """CSVファイルを読み込みます

    Parameters:
        csvFilePath (str): CSVファイルパス

    Returns:
        (list) CSV行リスト : [[CSV1行分],...]
    """
    dataList = pd.read_csv(csvFilePath).values.tolist()

    return dataList
