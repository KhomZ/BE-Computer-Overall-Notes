# Histogram 
# Dilation and Erosion (Morphological Operations)
# ============================Khom===================

import numpy as np
from cv2 import cv2, imread

img = cv2.imread(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day6\Erosion\sample_erode.jpg")
img = cv2.resize(img, (800,600))
cv2.imshow('ori', img)
# cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, bina) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', bina)
# cv2.waitKey(0)

filt = np.array([(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1)])
S = bina.shape
F = filt.shape
bina = bina/255
R = S[0] + F[0] - 1  # size of o/p image
C = S[1] + F[1] - 1
N = np.zeros((R,C))

for i in range(S[0]):
    for j in range(S[1]):
        N[i+1, j+1] = bina[i,j]

for i in range(S[0]):
    for j in range(S[1]):
        k = N[i:i+F[0], j:j+F[1]]
        result = (k==filt)
        # final = np.all(result==True)
        final = np.any(result==True)
        if final:
            bina[i,j] = 1
        else:
            bina[i,j] = 0
cv2.imshow('final', bina)
cv2.waitKey(0)