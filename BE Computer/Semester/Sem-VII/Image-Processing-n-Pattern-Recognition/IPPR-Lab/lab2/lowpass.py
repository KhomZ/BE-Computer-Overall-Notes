from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the image 
rose = cv2.imread(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day1\pictures\rose.jpg")
rose = cv2.resize(rose, (800,600))  # Resizing the image
# obtain the number of rows and columns of the image
# m,n = rose.shape
# print(m,n)
print(rose.shape)
plt.imshow(rose)