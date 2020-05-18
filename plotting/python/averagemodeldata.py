import os
import csv
import numpy as np
import pandas as pd

# version = 'GSM3036911_PDAC-A-ST1'
version = 'GSM3405534_PDAC-B-ST1'
colorFile = '../data/' + version + 'colors.csv'
dataFile = '../data/' + version + '.tsv'

colordf = pd.read_csv(colorFile)
data = pd.read_csv(dataFile, sep='\t')

# We want to ensure that all locations are at the top, as column headers.
if (version == 'GSM3036911_PDAC-A-ST1'):
    data = data.T


# data.set_index('Gene')
# data.set_index(data.index)
print(data)

colorDict = dict()

# Categorize locations by annotation category
for i in range(0, len(colordf)):
    color = colordf.iloc[i]['color']
    coord = colordf.iloc[i]['coord']

    if (color not in colorDict):
        colorDict[color] = set()

    colorDict[color].add(coord)

# print(colorDict)
# data[]

# for category in colorDict:
    # colorDict[category]
