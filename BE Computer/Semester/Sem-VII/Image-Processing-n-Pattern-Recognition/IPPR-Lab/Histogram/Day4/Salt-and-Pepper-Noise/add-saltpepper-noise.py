# Salt and Pepper Noise in Image
# ============================Khom===================


import random
import cv2


def add_noise(img):

    # Getting the dimensions of the image
    row, col = img.shape

    # Randomly pick some pixels in the image for coloring them white 
    # Pick a random number between 300 and 10000. ==>img.shape is (822,1200).
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):

        # pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # color that pixel to white
        img[y_coord][x_coord] = 255


    # Randomly pick some pixels in the image 
    # for coloring them black 
    # Pick a random number between 300 and 10000.
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):

        # pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # color that pixel to white
        img[y_coord][x_coord] = 0

    return img


# salt and pepper noise can be applied only to grayscale image
# Reading the color image in grayscale image

# img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('lena1.png', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day4\Salt-and-Pepper-Noise\lena.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day4\Salt-and-Pepper-Noise\lena1.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow('grayscale', img)

# Storing the image
# imgfinal = cv2.imwrite('salt-and-pepper-lena.jpg', add_noise(img))
# cv2.imshow('after adding salt and pepper noise', imgfinal)

imgfinal = add_noise(img)
# file_name_path = r"./output/salt-and-pepper-lena.jpg"
# file_name_path = r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day4\Salt-and-Pepper-Noise\salt-n-pepper-lena.jpg"
file_name_path = r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Image-Processing-n-Pattern-Recognition\IPPR-Lab\Histogram\Day4\Salt-and-Pepper-Noise\salt-n-pepper-lena1.png"
cv2.imwrite(file_name_path, imgfinal)


cv2.imshow('after salt n pepper noise',imgfinal)




cv2.waitKey(0)


# face =cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
# file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
# cv2.imwrite(file_name_path,face)
