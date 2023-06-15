def printData(dataList, title):
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
