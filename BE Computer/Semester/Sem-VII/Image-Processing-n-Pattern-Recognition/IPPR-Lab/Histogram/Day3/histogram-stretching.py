# Histogram Stretching
# ============================Khom===================

from cv2 import cv2
import numpy as np
# import math
import matplotlib.pyplot as plt


rose = cv2.imread(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day1\pictures\rose.jpg")
# print(rose)
rose = cv2.resize(rose, (800, 600))
k = rose.shape
# cv2.imshow('original', rose)
roseGray = cv2.cvtColor(rose, cv2.COLOR_BGR2GRAY)  # RGB to Grey
roseGray = cv2.convertScaleAbs(roseGray, alpha=1.10, beta=80)  # Manipulation in Contrast and Brightness

# cv2.imshow('binary', roseGray)
# cv2.waitKey(0)


def Hist(image):
    H = np.zeros(shape=(256,1))
    k = image.shape
    for i in range(k[0]):
        for j in range(k[1]):
            new_var = image[i, j]
            # H[new_var, 0] = H[new_var, 0] + 1
            H[new_var,0] += 1
    return H

histg = Hist(roseGray)
plt.plot(histg)
plt.show()

# ============================== Main code============================== 

x = histg.reshape(1,256)
y = np.zeros((1,256))

for i in range(256):
    if x[0,i] == 0:
        y[0,i] = 0
    else:
        y[0,i] = i

min = np.min(y[np.nonzero(y)])
max = np.max(y[np.nonzero(y)])

stretch = np.round(((255-0) / (max-min)) * (y-min))
stretch[stretch<0] = 0
stretch[stretch>255] = 255  # rounding off  the values using numpy

for i in range(k[0]):
    for j in range(k[1]):
        new_var = roseGray[i,j]
        roseGray[i,j] = stretch[0,new_var]

histg2 = Hist(roseGray)
cv2.imshow('mystretching', roseGray)
plt.plot(histg)
plt.plot(histg2)
plt.show()



