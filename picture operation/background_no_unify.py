import os
import cv2
import math
import imutils
import numpy as np
from PIL import Image
from skimage import io



def open_picture(image):
    """We open picture"""

    img = cv2.imread(image)
    return img

def show_picture(name, image, mode, destroy):
    """
        Show picture
        mode 0 = entrance key  pass to next
        mode y = destroy windows
    """
    
    cv2.imshow(name, image)
    cv2.waitKey(mode)
    if destroy == "y":
        cv2.destroyAllWindows()

def blanck_picture(img):
    """
        Create a black empty picture
    """

    blank_image = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    blank_image[0:, 0:] = 0, 0, 0

    return blank_image


def make_contours(gray):
    th3 = cv2.adaptiveThreshold(gray, 255,
                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY,11,-5)
    show_picture("on", th3, 0, "")

    contours,h=cv2.findContours(th3,cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_NONE)


    return contours


def maxi_contours(contours, blanck):
    maxi = 0
    for cnt in contours:
        if cv2.contourArea(cnt) > maxi:
            maxi =  cv2.contourArea(cnt)

    for cnt in contours:
        if cv2.contourArea(cnt) == maxi:
            cv2.drawContours(blanck,[cnt], -1, (0,255,0), 1)
            cv2.fillPoly(blanck, pts =[cnt], color=(0, 255, 0))


    return blanck

def mask(copy, copy1):

    for i in range(copy.shape[0]):
        for j in range(copy.shape[1]):
            if blanck[i, j][0] == 0 and\
               blanck[i, j][1] == 255 and\
               blanck[i, j][2] == 0:
                copy[i, j] = 0, 0, 0
            else:
                copy1[i, j] = 255, 255, 255

    return copy, copy1


path = r"C:\Users\jeanbaptiste\Desktop\assiette\program\dataset\aa\a.jpg"

def main(path)

    #Open and binarized picture
    img = open_picture(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #found contours
    contours = make_contours(gray)

    #make copies
    copy = img.copy()
    copy1 = img.copy()
    blanck = blanck_picture(img)

    blanck = maxi_contours(contours, blanck)

    copy, copy1 = mask(copy, copy1)


    show_picture("on", blanck, 0, "")
    show_picture("copy", copy, 0, "")
    show_picture("copy1", copy1, 0, "")
















