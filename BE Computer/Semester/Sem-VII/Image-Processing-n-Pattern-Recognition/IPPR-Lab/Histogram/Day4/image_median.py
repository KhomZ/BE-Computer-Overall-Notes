# Histogram Convolution and Correlation
# ============================Khom===================

# Median of the Image :
# For this we need an empty kernel  

from cv2 import cv2
import numpy as np

lena = cv2.imread(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day4\Salt-and-Pepper-Noise\salt-n-pepper-lena1.png")
# rose = cv2.imread(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day4\Convolution-n-Correlation\saltnoise.png")
lena = cv2.resize(lena, (800,600))  # Resizing the image

# filt = np.array([(1,1,1,1,1), (1,1,1,1,1), (1,1,1,1,1), (1,1,1,1,1), (1,1,1,1,1)]) * (1/25)  # filter (5,5)
# filt = np.array([(1,1,1),(1,1,1),(1,1,1)]) * (1/9)  # filter (3,3)
filt = np.array([(1,1,1),(1,1,1),(1,1,1)])

S = lena.shape
F = filt.shape

lenaGray = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY)  # binary conversion
cv2.imshow('original', lenaGray)


# Zero padding
# imageSize + kernelSize - 1
# as you increase the kernelSize the image blur also increases
R = S[0] + F[0] - 1
C = S[1] + F[1] - 1
Z = np.zeros((R, C))

for i in range(S[0]):
    for j in range(S[1]):
        Z[i+np.int((F[0] - 1)/2), j+np.int((F[1] - 1)/2)] = lenaGray[i,j]

print(Z)

for i in range(S[0]):
    for j in range(S[1]):
        k = Z[i:i+F[0], j:j+F[1]]
        # l = np.sum(k*filt)
        l = np.median(k)
        lenaGray[i,j] = l

cv2.imshow('final', lenaGray)
cv2.waitKey(0)