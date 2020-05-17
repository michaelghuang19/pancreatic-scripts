import cv2
import matplotlib.pyplot as plt
import numpy as np

# All possible color flags
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

image = cv2.imread('./figures/coloredA-ST1paper.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.show()
