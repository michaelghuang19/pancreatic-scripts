import pandas as pd

dataindex = '../data/'
genekeyfile = dataindex + 'entrezgene-hgnc-table.csv'
datafile = dataindex + 'average-B-ST1grey.csv'

genekey = pd.read_csv(genekeyfile)
data = pd.read_csv(datafile, header = None)

genekey = genekey.dropna()
genekey = genekey.drop_duplicates()
genekey['entrezgene'] = genekey['entrezgene'].astype(int)
data.columns = {'genes', 'state'}

# print(genekey)
# print(data)

for i in range(0,len(data)):
    hgnc_gene = data.iloc[i]['genes']
    entrez_geneseries = genekey.loc[genekey['hgnc_symbol'] == hgnc_gene]

    if len(entrez_geneseries) > 0:
        # print(hgnc_gene)
        # print(entrez_geneseries)
        index = entrez_geneseries.index[0]
        data.at[i, 'genes'] = genekey.at[index, 'entrezgene']
    else:
        data.drop([i])

# insert writer: this takes forever
print(data)

# evaluate only metabolic, median?
