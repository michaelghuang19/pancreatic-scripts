import matplotlib.pyplot as plt
import PIL
from PIL import Image
import csv

dir = './figures/'
paperPNG = 'coloredA-ST1paper.png'

im = Image.open(dir + paperPNG)
pic = im.load()
# print(im.size)

# pre-sets for A-ST1
# x starts around 4.6, but is really 2 at left
# y starts around 10.8, but is really 34 at top
# 925 x 888, 428 values
# non-inclusive
ax = range(2, 31)
ay = range(8, 35)
axo = 4.6
ayo = 10.8
axi = 29
ayi = 30

# pre-sets for B-ST1
# x starts around 5.8, but is really 15 at left
# y starts around 0, but is really 21 at top
# 784 x 869, 224 values
# non-inclusive
bx = range(15, 33)
by = range(2, 22)
bxo = 5.8
byo = 0
bxi = 40
byi = 40

pink = (229, 42, 137, 255)
blue = (118, 112, 178, 255)
grey = (102, 102, 102, 255)
green = (25, 157, 119, 255)
turq = (141, 208, 197, 255)

aDict = {pink:"pink", blue:"blue", grey:"grey", green:"green"}
bDict = {pink:"pink", turq:"turq", grey:"grey"}

colorDict = aDict
count = 0
xValues = ax
yValues = ay
xOffset = axo
yOffset = ayo
xIter = axi
yIter = ayi

with open(paperPNG + '.csv', mode='w', newline='') as file:

    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for x in xValues:
        for y in yValues:
            xcoord = xOffset + ((x - min(xValues)) * axi)
            ycoord = yOffset + ((y - min(yValues)) * ayi)

            color = pic[xcoord, ycoord]
            if color != (255,255,255,255):
                print(str(xcoord) + ", " + str(ycoord))
                print(str(x) + ", " + str(y))
                print(color)
                writer.writerow([str(xcoord) + ", " + str(ycoord),
                str(x) + ", " + str(y), colorDict[color]])
                count = count + 1

print(count)


# TODO: annotate in csv
# TODO: work on ggplot, which might be easier and more accurate
