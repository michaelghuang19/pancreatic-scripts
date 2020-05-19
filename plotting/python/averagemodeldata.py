import pandas as pd
import csv

version = 'GSM3036911_PDAC-A-ST1'
# version = 'GSM3405534_PDAC-B-ST1'
colorFile = '../data/' + version + 'colors.csv'
dataFile = '../data/' + version + '.tsv'

colordf = pd.read_csv(colorFile)
data = pd.read_csv(dataFile, sep='\t')

# data = data.rename(index = data.iloc[:,0])
# We want to ensure that all locations are at the top, as column headers.
if (version == 'GSM3036911_PDAC-A-ST1'):
    data = data.T

data = data.rename(columns = data.iloc[0])
data = data.drop(data.index[0])
# print(data)

colorDict = dict()

# Categorize locations by annotation category
for i in range(0, len(colordf)):
    color = colordf.iloc[i]['color']
    coord = colordf.iloc[i]['coord']

    if (color not in colorDict):
        colorDict[color] = set()

    colorDict[color].add(coord)

for category in colorDict:
    with open(version + category + '.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # df = pd.DataFrame(data['Genes'])
        df = pd.DataFrame(data.index)
        df = df.set_index(data.index)

        # writer.writerow(data['Genes'])
        writer.writerow(df.iloc[:,0])
        df = df.iloc[:,1:]

        for area in colorDict[category]:
            df[str(area)] = data[str(area)]

        writer.writerow(df.mean(axis=1))

        # print(df)
