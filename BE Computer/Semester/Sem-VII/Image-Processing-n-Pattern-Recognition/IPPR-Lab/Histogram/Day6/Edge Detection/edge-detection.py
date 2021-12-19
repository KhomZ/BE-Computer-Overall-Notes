# Histogram 
# Dilation and Erosion (Morphological Operations)
# ============================Khom===================

# Digital Image Processing 6 :

# Simply Dilation adds pixels to the boundaries and Erosion removes pixels from the boundaries.
# Dilation helps objects more visible , helps to fill the holes if present in the image. 
# erosion, on the other hand, can break the connectivity between two objects.

import numpy as np
from cv2 import cv2, resize

original = cv2.imread(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day1\pictures\ai-buddha.jpg")
original = cv2.resize(original, (800,600))

edges = cv2.Canny(original, 50, 300)
cv2.imshow('edges', edges)
# cv2.imwrite('sample_edges.jpg',edges)

file_name_path = r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day6\Edge Detection\sample_edges.jpg"
cv2.imwrite(file_name_path, edges)

cv2.waitKey(0)



# also you can use this code to resize your image 
# res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
