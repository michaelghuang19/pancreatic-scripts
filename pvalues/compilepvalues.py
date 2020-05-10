import csv
import os
import pandas as pd 
import numpy as np

directory = os.path.join("c:\\", "Users\\junio\\Documents\\_workspace\\_wangspring2020project\\GSE111672\\ST\\tsv\\pvalues\\sig_data")

pval_dict = {}

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".csv"):
            print(file)
            # file = file.apply(lambda s : s.decode('utf-8'))
            df = pd.read_csv(file, header= None)

            # print(file)
            # print(df.size - 1)

            for i in range(int(df.size / 3)):
                gene = df.iloc[i,0]
                adj_pval = df.iloc[i,2]

                if (gene in pval_dict):
                    pval_dict[gene].append(adj_pval)
                else:
                    pval_dict[gene] = [adj_pval]


items = sorted(pval_dict.items(), key = 
    lambda kv:(-len(kv[1])))

# print(type(items))
# print(items)

df = pd.DataFrame(items)
df['gene'] = df[0]
df['significant_appearances'] = df[1]
df['length'] = df[1].str.len()
df = df.reindex(columns=['gene','length','significant_appearances'])

# print(df)

df.to_csv('compiled_pvalues.csv', index = False, header = False)