# Histogram 
# Dilation and Erosion (Morphological Operations)
# ============================Khom===================

# Digital Image Processing 6 :

# Simply Dilation adds pixels to the boundaries and Erosion removes pixels from the boundaries.
# Dilation helps objects more visible , helps to fill the holes if present in the image. 
# erosion, on the other hand, can break the connectivity between two objects.

import cv2
import numpy as np
from numpy.lib.type_check import imag

# image = cv2.imread(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day1\pictures\ai-buddha.jpg")
image = cv2.imread(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day1\pictures\rose.jpg")
cv2.imshow('original', image)

kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(image, kernel, iterations = 30)
cv2.imshow('dilate', dilation)

file_name_path = r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day6\Dilation\sample_dilate.jpg"
cv2.imwrite(file_name_path, dilation)

cv2.waitKey(0)