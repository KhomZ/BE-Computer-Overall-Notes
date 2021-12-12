import cv2

image = cv2.imread(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day1\pictures\ai-buddha.jpg")
# image = cv2.imread(r".\pictures\ai-buddha.jpg")

resized_image = cv2.resize(image, (300, 300))

cv2.imshow("image", resized_image)
cv2.waitKey(0)