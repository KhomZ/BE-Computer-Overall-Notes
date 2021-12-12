# @KhomZ
# Image Processing and Pattern Recognition
# 12/12/2021 Sunday

# from cv2 import cv2
import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import place

# rose = cv2.imread(r'.\pictures\ai-buddha.jpg')
# rose = cv2.imread(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day1\pictures\Butterfly.jpg")
rose = cv2.imread(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day1\pictures\rose.jpg")
# print(rose)
# rose = cv2.imread('rose.jpg')

rose = cv2.resize(rose, (800, 600))  # (w, h) = (800 px, 600 px)
# cv2.imshow('original', butterfly)
# cv2.waitKey(0)  # here waitKey(0) means whenever key 0 is pressed, closes all the windows 

k = rose.shape
# print(k)
 # gives o/p (600, 800, 3) meaning RGB image


roseGray = cv2.cvtColor(rose, cv2.COLOR_BGR2GRAY)  # here we are using convertColor method
cv2.imshow('Binary', roseGray)
# now let's manipulate the contrast and brightness of the image 
# alpha represents contrast and beta represents brightness.
roseGray = cv2.convertScaleAbs(roseGray, alpha=1.10, beta=-20)
# cv2.imshow('Enhanced', roseGray)
# cv2.waitKey(0)

H = np.zeros(shape=(256,1))  # numpy array of pixels.  total pixels =255 i.e. 0 to 255
print(H)

# if you want to go to every pixels we need a row value and a column value
# for that we need two for loops foreach
# and here we have total 600 rows and 800 columns

for i in range(k[0]):
    for j in range(k[1]):
        new_var = roseGray[i, j]
        H[new_var, 0] = H[new_var, 0] + 1

# print(H)  # prints array of pixels for each value
# now lets plot them

plt.plot(H)
plt.show()  # plots the histogram of our image

# =================================Coding with Khom=======================================================