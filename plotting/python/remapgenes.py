import pandas as pd
import numpy as np
import csv

dataindex = '../data/'
# version = 'B-ST1blue'
versionSet = {'B-ST1grey', 'B-ST1pink', 'B-ST1turq', 'A-ST1blue', 'A-ST1green', 'A-ST1pink', 'A-ST1rey'}

def convert_hgnc_to_entrez():
    genekeyfile = dataindex + 'entrez/entrezgene-hgnc-table.csv'
    datafile = dataindex + 'average-' + version + '.csv'

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

def get_metabolic():
    metabolicfile = dataindex + 'section_1point2_tumor_region_evidence_mean.txt'

    meta_data = pd.read_csv(metabolicfile, sep = '\t')
    meta_set = set(meta_data['genes'])

    return meta_set


# evaluate only metabolic?
def keep_metabolic(meta_set, version):
    datafile = dataindex + 'entrez/entrez-' + version + '.csv'
    data = pd.read_csv(datafile)

    with open('metabolic' + version + '.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for i in range(0, len(data)):
            series = data.iloc[i]
            entrez = series['genes']

            if entrez.isnumeric():
                entrez = int(entrez)

                if entrez in meta_set:
                    writer.writerow(series)

def get_cutoff(version):
    datafile = dataindex + 'entrez/entrez-' + version + '.csv'
    metafile = dataindex + 'metabolic/metabolic-' + version + '.csv'

    data = pd.read_csv(datafile)
    meta = pd.read_csv(metafile, header = None)
    meta.columns = ['genes', 'state']

    print(version + ' cutoff is ' + str(meta.iloc[500]['state']))

# only keep median

if __name__ == "__main__":
    # meta_set = get_metabolic()

    for version in versionSet:
        # keep_metabolic(meta_set, version)
        get_cutoff(version)
