import PIL
from PIL import Image

im = Image.open('./figures/coloredA-ST1paper.png')
pic = im.load()
print(im.size)
print(pic[150,100])

print("pink " + str(pic[150,101]))
print("blue " + str(pic[550,675]))
print("grey " + str(pic[360,375]))
print("green " + str(pic[520,315]))

# pre-sets for A-ST1
# x starts around 4.6, but is really 2 at left
# y starts around 10.8, but is really 34 at top
# 925 x 888
# non-inclusive
ax = range(2, 31)
ay = range(8, 35)
axo = 4.6
ayo = 10.8
axi = 31.7
ayi = 32.1

# 43.5
# 75.7
# 107.9
# diff of exactly 32.2 accordingly

pink = (229, 42, 137, 255)
blue = (118, 112, 178, 255)
grey = (102, 102, 102, 255)
green = (25, 157, 119, 255)

aSet = {pink, blue, grey, green}

colorSet = aSet
count = 0
xValues = ax
yValues = ay 
xOffset = axo
yOffset = ayo
xIter = axi
yIter = ayi

for x in xValues:
    for y in yValues:
        xcoord = xOffset + ((x - min(xValues)) * axi)
        ycoord = yOffset + ((y - min(yValues)) * ayi)

        color = pic[xcoord, ycoord]
        if color != (255,255,255,255):
            print(xcoord, ycoord)
            print(color)
            count = count + 1

print(count)


# TODO: annotate in csv
# TODO: work on ggplot, which might be easier and more accurate
