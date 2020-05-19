import pandas as pd

dataindex = '../data/'
genekeyfile = dataindex + 'entrezgen-hgnc-table.csv'
datafile = dataindex + 'average-B-ST1grey.csv'

genekey = pd.read_csv(genekeyfile)
data = pd.read_csv(datafile)

genekey = genekey.dropna()

print(genekey)



# evaluate only metabolic, median?
