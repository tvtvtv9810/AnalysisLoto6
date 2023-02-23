import csv

f = open("input/loto6_result.csv", "r")
reader = csv.reader(f)
data = [e for e in reader]
print(data)
f.close()


with open('input/loto6_result.csv') as f:
    resultData = f.read()
    print(resultData)
