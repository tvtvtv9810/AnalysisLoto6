import readCsv
import converter
import printData

import os
import datetime

import csv

import sys


tmpDictionary = {"key1": 11, "key2": 22}


# CSV全データ
allDataList = readCsv.readCsv("input/loto6_result_set.csv")
# 全データ数
allDataNum = len(allDataList)

# スクリプト名を除いたコマンドライン引数
args = sys.argv[1:]

# １つめの引数が「出力する回」
outputNum = allDataNum
if len(args) > 0:
    outputNum = int(args[0])

print("--info--")
print(str(allDataNum) + "回目までデータあり")
print(str(outputNum) + "回目まで出力")
print("---")

# 処理対象のリスト（引数で指定された回までのデータを切り取る）
targetDataList = allDataList[0:outputNum]

# セット球ごと
convertedDictBySet = converter.convertToMapBySet(targetDataList)
printData.printDataDictionary(convertedDictBySet, 'セット球ごと')
# 全部：番号ごと
dataDictByAllNum = converter.convertToMapByNum(targetDataList)
printData.printDataDictionary(dataDictByAllNum, '１～６（セット球：all）ごと')

# データリストのリスト
dataListDictionary = {}
dataListDictionary["all"] = dataDictByAllNum

# セット球ごとの番号の出現回数
for setNum, times in convertedDictBySet.items():
    # セット球で絞った、番号ごと
    noteByNumFilterSet = setNum + "：セット球で絞ったの番号ごと"
    convertedDictByNumFilterSet = converter.convertToMapByNumFilterSet(
        targetDataList, setNum)
    dataListDictionary[setNum] = convertedDictByNumFilterSet

# 現在日付
dt_now = datetime.datetime.now()

# 結果出力
fileName = dt_now.strftime('%Y%m%d_%H%M%S')
# os.mkdir(new_dir)
with open('output/' + fileName + '.csv', 'w', encoding="utf_8_sig") as f:
    writer = csv.writer(f)
    lastData = allDataList[allDataNum-1]
    writer.writerow([lastData[7] + "（" + lastData[8] + '）までデータあり'])
    writer.writerow([str(outputNum) + "回目まで出力"])

    setNumList = sorted(convertedDictBySet.items())
    writer.writerow(['■セット球ごと', '回数'])
    for data in setNumList:
        writer.writerow([data[0], data[1]])

    writer.writerow(['■数値ごと'])
    titleRow = ['■ 数値', 'all']
    for data in setNumList:
        titleRow.append(data[0])
    writer.writerow(titleRow)

    for i in range(43):
        targetNum = i + 1
        numLow = [targetNum]

        if targetNum in dataListDictionary["all"]:
            numLow.append(dataListDictionary["all"][targetNum])
        else:
            numLow.append(0)

        for data in setNumList:
            targetSetNum = data[0]

            if targetNum in dataListDictionary[targetSetNum]:
                numLow.append(dataListDictionary[targetSetNum][targetNum])
            else:
                numLow.append(0)

        writer.writerow(numLow)

    # writer.writerow([0, 1, 2])
    # writer.writerow(['a', 'b', 'c'])


# 出力
# for i in range(len(dataListByAllNum)):

#     oneRowStrHeader = "順位"
#     oneRowStr = str(i+1) + "位"
#     for key in dataListDictionary:

#         targetNum = str(dataListDictionary[key][i][0]) if not len(
#             dataListDictionary[key]) - 1 < i else "-"

#         targetTimes = str(dataListDictionary[key][i][1]) if not len(
#             dataListDictionary[key]) - 1 < i else "-"

#         if i == 0:
#             oneRowStrHeader = oneRowStrHeader + ",■," + key + ", 回数"
#         oneRowStr = oneRowStr + ",■," + targetNum + "," + targetTimes
#     if i == 0:
#         print(oneRowStrHeader)
#     print(oneRowStr)
