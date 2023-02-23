import pandas as pd

dataList = pd.read_csv("input/loto6_result.csv").values.tolist()
# print(dataList)

countDictionary = {}
for data in dataList:
    # print('■')
    for i in range(7):
        # print(data[i])
        number = data[i]
        if number in countDictionary:
            countDictionary[number] += 1
        else:
            countDictionary[number] = 0

# キー（Loto6番号）でソート
print(sorted(countDictionary.items()))

print("-------")

# 回数でソート
print(sorted(countDictionary.items(),  key=lambda x: x[1]))
