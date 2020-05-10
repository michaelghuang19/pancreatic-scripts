import pandas as pd

tsv_list = []
tsv_list.append('GSM4100721_PDAC-A-st2.tsv')
tsv_list.append('GSM4100722_PDAC-A-st3.tsv')
tsv_list.append('GSM4100723_PDAC-B-st2.tsv')
tsv_list.append('GSM4100724_PDAC-B-st3.tsv')
tsv_list.append('GSM4100725_PDAC-D-st1.tsv')
tsv_list.append('GSM4100726_PDAC-E-st1.tsv')
tsv_list.append('GSM4100727_PDAC-F-st1.tsv')
tsv_list.append('GSM4100728_PDAC-G-st1.tsv')

# for each this shit

for tsv_file in tsv_list:
    print(tsv_file)
    csv_table=pd.read_csv(tsv_file,sep='\t')
    csv_table.to_csv(tsv_file[0:21] + '.csv',index=False)
