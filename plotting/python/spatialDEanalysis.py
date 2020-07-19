from pylab import *
import pandas as pd
import matplotlib.pyplot as plt
import NaiveDE
import SpatialDE

version = 'GSM3036911_PDAC-A-ST1'
# version = 'GSM3405534_PDAC-B-ST1'

dataindex = '../data/raw/'
versionSet = []
conversionTable = {4860 : 'PNP', 54981 : 'NMRK1', 2542 : 'SLC37A4', 56848 : 'SPHK2', 1384 : 'CRAT', 1644 : 'DDC', 3155 : 'HMGCL', 50 : 'ACO2', 65985 : 'AACS', 2936 : 'GSR', 6510 : 'SLC1A5', }

data = pd.read_csv(dataindex + version + '.tsv', sep='\t')
if (version == 'GSM3036911_PDAC-A-ST1'):
    data = data.T

data = data.rename(columns = data.iloc[0])
data = data.drop(data.index[0])

# print(data)

xCoords = []
yCoords = []

for coord in data.columns:
    coord = coord.split('x')
    xCoords.append(int(coord[0]))
    yCoords.append(int(coord[1]))

# this is for general testing of the spatial plot

# rcParams['figure.figsize'] = 6,4
# plt.scatter(xCoords, yCoords, c='k')
# plt.axis('equal')
# plt.savefig('../figures/' + version)

# NaiveDE normalized expression

# norm_expr = NaiveDE.stabilize(data.astype('float').T).T
# print(norm_expr)

for genePair in conversionTable:
    hgnc = conversionTable[genePair]

    if (hgnc in data.T):
        print(hgnc)
        print(data.T[hgnc])
        plt.title('raw st ' + str(genePair) + '/' + hgnc)
        plt.scatter(xCoords, yCoords, c=data.T[hgnc])
        plt.colorbar(ticks=[])
        plt.savefig('../figures/spatial-gradients/' + version + '/' + version + '-' + str(genePair))
        plt.clf()
