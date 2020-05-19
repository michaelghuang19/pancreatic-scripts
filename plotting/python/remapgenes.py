import pandas as pd

dataindex = '../data/'
genekeyfile = dataindex + 'entrezgene-hgnc-table.csv'
datafile = dataindex + 'average-A-ST1rey.csv'

genekey = pd.read_csv(genekeyfile)
data = pd.read_csv(datafile, header = None)

genekey = genekey.dropna()
genekey = genekey.drop_duplicates()
genekey['entrezgene'] = genekey['entrezgene'].astype(int)
data.columns = {'genes', 'state'}

# print(genekey)
# print(data)
# print(len(data))

for i in range(0,len(data)):
    hgnc_gene = data.iloc[i]['genes']
    entrez_geneseries = genekey.loc[genekey['hgnc_symbol'] == hgnc_gene]

    print(hgnc_gene)

    if entrez_geneseries.empty:
        print(entrez_geneseries)
        data.drop([i])
    else:
        index = entrez_geneseries.index[0]
        print(index)
        data.at[i, 'genes'] = genekey.at[index, 'entrezgene']

data.to_csv('entrez-A-ST1rey.csv', index = False)



# evaluate only metabolic, median?
