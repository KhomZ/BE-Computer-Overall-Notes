# Histogram Equalization
# ============================Khom===================

from cv2 import cv2
import numpy as np
import math
import matplotlib.pyplot as plt


# rose = cv2.imread('..\\Flowers\\flower.jpg')
rose = cv2.imread(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day1\pictures\rose.jpg")
# print(rose)
rose = cv2.resize(rose, (800, 600))
k = rose.shape
# cv2.imshow('original', rose)
roseGray = cv2.cvtColor(rose, cv2.COLOR_BGR2GRAY)
roseGray = cv2.convertScaleAbs(roseGray, alpha=1.10, beta=-20)
# cv2.imshow('binary', roseGray)


def Hist(image):
    H = np.zeros(shape=(256,1))
    k = image.shape
    for i in range(k[0]):
        for j in range(k[1]):
            new_var = image[i, j]
            # H[new_var, 0] = H[new_var, 0] + 1
            H[new_var,0] += 1
    return H

'''
histogram equalization 
Khom
'''
histg = Hist(roseGray)
plt.plot(histg)
x = histg.reshape(1,256)
y = np.array([])
y = np.append(y, x[0,0])

for i in range(255):
    new_var = x[0,i+1] + y[i]
    y = np.append(y, new_var)
y = np.round((y/(k[0]*k[1]))*(256-1))

for i in range(k[0]):
    for j in range(k[1]):
        new_var = roseGray[i, j]
        roseGray[i,j] = y[new_var]

equal = Hist(roseGray)
plt.plot(equal)
plt.show()

# cv2.imshow('myequalize', roseGray)  # more contrast has been seen
# cv2.waitKey(0)
