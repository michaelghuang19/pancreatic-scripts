import csv

tsv_list = []
tsv_list.append('GSM4100721_PDAC-A-st2.tsv')
tsv_list.append('GSM4100722_PDAC-A-st3.tsv')
tsv_list.append('GSM4100723_PDAC-B-st2.tsv')
tsv_list.append('GSM4100724_PDAC-B-st3.tsv')
tsv_list.append('GSM4100725_PDAC-D-st1.tsv')
tsv_list.append('GSM4100726_PDAC-E-st1.tsv')
tsv_list.append('GSM4100727_PDAC-F-st1.tsv')
tsv_list.append('GSM4100728_PDAC-G-st1.tsv')

# for each the rest of this?

findd=[]
repl=[]
with open('find_replace_data.csv', mode='r') as infile:
  reader = csv.reader(infile)
  for rows in reader:
      a= rows[0]
      b= rows[1]
      findd.append(a)
      repl.append(b)



ifile = open('infile.csv', 'rb')
reader = csv.reader(ifile)
ofile = open('outfile.csv', 'wb')
writer = csv.writer(ofile)

rep = dict(zip(findd, repl))

s = ifile.read()
for item in findd:
    s = s.replace(item, rep[item])
ofile.write(s)
ifile.close()
ofile.close()
