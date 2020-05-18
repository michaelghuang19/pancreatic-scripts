import pandas as pd

dataindex = '../data'
genekeyfile = dataindex + 'Human_gene_ID_mapping_file.csv'
datafile = dataindex + 'average-B-ST1grey.csv'

genekey = pd.read_csv(genekeyfile)
data = pd.read_csv(datafile)

# TODO: change

# evaluate only metabolic, median?
