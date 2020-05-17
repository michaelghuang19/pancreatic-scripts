import pandas as pd

tsv_file='./data/GSM3405534_PDAC-B-ST1.tsv'

csv_table=pd.read_csv(tsv_file,sep='\t')
csv_table.to_csv('GSM3405534_PDAC-B-ST1.csv',index=False)
