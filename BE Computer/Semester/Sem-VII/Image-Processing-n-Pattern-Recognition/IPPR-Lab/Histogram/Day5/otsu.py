# Histogram 
# Otsu's Thresholding (Within-class variance)
# ============================Khom===================

# Digital Image Processing 5.1 :

import numpy as np
from cv2 import cv2
from numpy.lib.type_check import imag

rose = cv2.imread(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day1\pictures\rose.jpg")

rose = cv2.resize(rose, (800,600))

rose_gray = cv2.cvtColor(rose, cv2.COLOR_BGR2GRAY)
cv2.imshow('binary', rose_gray)
# cv2.waitKey(0)

histg = cv2.calcHist(rose_gray, [0], None, [255], [0,255])
print(histg)

# now finding within-class variance
within = []
between = []
for i in range(len(histg)):
    d = 0
    x,y = np.split(histg, [i])
    x1 = np.sum(x)/(rose.shape[0] * rose.shape[1])  # weight of class 1
    y1 = np.sum(y)/(rose.shape[0] * rose.shape[1])

    x2 = np.sum([j*t for j,t in enumerate(x)])/np.sum(x)  # t-pixels & j-indexing values. here, x2 & y2 are mean values
    x2 = np.nan_to_num(x2)
    y2 = np.sum([(j+d)*(t) for j,t in enumerate(y)])/np.sum(y)

    x3 = np.sum([(j-x2)**2*t for j,t in enumerate(x)])/np.sum(x)  # find variance
    # print(x3)  # prints nan value also so we need to change nan values to zeros as
    x3 = np.nan_to_num(x3)
    # print(x3)
    y3 = np.sum([(j+d-y2)**2*t for j,t in enumerate(y)])/np.sum(y)
    d = d+1
    within.append(x1*x3 + y1*y3)
    between.append(x1*y1*(x2-y2)*(x2-y2))

m = np.argmin(within)
n = np.argmax(between)
print(m)
print(n)

(thresh, Bin) = cv2.threshold(rose_gray, m, 255, cv2.THRESH_BINARY)
cv2.imshow('Otsu', Bin)
cv2.waitKey(0)