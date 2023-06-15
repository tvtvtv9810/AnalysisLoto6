import readCsv
import converter
import printData

dataList = readCsv.readCsv("input/loto6_result_set.csv")

# セット球ごと
convertedListBySet = converter.convertToMapBySet(dataList)
printData.printData(convertedListBySet, "セット球")


# 番号ごと
dataListByNum = converter.convertToMapByNum(dataList)
printData.printData(dataListByNum, "番号ごと")


# 対象にする
targetSetNum = convertedListBySet[0][0]


# セット球で絞った、番号ごと
convertedListByNumFilterSet = converter.convertToMapByNumFilterSet(
    dataList, targetSetNum)
printData.printData(convertedListByNumFilterSet, "----セット球で絞ったの番号ごと")
