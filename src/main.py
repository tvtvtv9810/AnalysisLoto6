import readCsv
import converter
import printData

dataList = readCsv.readCsv("input/loto6_result_set.csv")

print(str(len(dataList)) + "回目")

# セット球ごと
convertedListBySet = converter.convertToMapBySet(dataList)
printData.printData(convertedListBySet, "セット球")

# データリストのリスト
dataListDictionary = {}

# 全部：番号ごと
dataListByAllNum = converter.convertToMapByNum(dataList)
dataListDictionary["all"] = dataListByAllNum
# printData.printData(dataListByAllNum, "番号ごと")


# セット球ごとの番号の出現回数
# targetSetNum = convertedListBySet[0][0]
for data in convertedListBySet:
    setNum = data[0]

    # セット球で絞った、番号ごと
    noteByNumFilterSet = setNum + "：セット球で絞ったの番号ごと"
    convertedListByNumFilterSet = converter.convertToMapByNumFilterSet(
        dataList, setNum)
    dataListDictionary[setNum] = convertedListByNumFilterSet
    # printData.printData(convertedListByNumFilterSet, noteByNumFilterSet)

# 出力
for i in range(len(dataListByAllNum)):
    oneRowStrHeader = "順位"
    oneRowStr = str(i) + "位"
    for key in dataListDictionary:
        if i == 0:
            oneRowStrHeader = oneRowStrHeader + ",■," + key + ", 回数"
        oneRowStr = oneRowStr + ",■," + \
            str(dataListDictionary[key][i][0]) + "," + \
            str(dataListDictionary[key][i][1])
    if i == 0:
        print(oneRowStrHeader)
    print(oneRowStr)
