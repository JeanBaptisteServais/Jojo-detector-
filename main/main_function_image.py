import os
import cv2
import time
import numpy as np

import sys
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\assiette\v2")



def open_picture(image):
    """We open picture"""
    img = cv2.imread(image)
    return img

def show_picture(name, image, mode, destroy):
    """Show picture"""
    
    cv2.imshow(name, image)
    cv2.waitKey(mode)
    if mode == 1:
        time.sleep(1)
        cv2.destroyAllWindows()
    if destroy == "y":
        cv2.destroyAllWindows()

def save_picture(name, picture):
    """saving picture"""
    cv2.imwrite(name, picture)

def blanck_picture(img):
    """ Create a black picture"""
    blank_image = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
    blank_image[0:, 0:] = 0, 0, 0
    return blank_image


def define_size(i):
    """Here we define the dimension for the training
    after have course dimension of picture"""

    out = "";

    #exemple : spoon
    if abs(i[0] - i[1]) > 3.0 and\
       i[0] > i[1]:
        out = [20,100]

    #exemple : plate
    elif abs(i[0] - i[1]) > 2.0 and\
         abs(i[0] - i[1]) < 3.0 and\
         i[0] > i[1]:
        out = [50, 50]

    #exemple : bol
    elif abs(i[0] - i[1]) > 1.0 and\
         abs(i[0] - i[1]) < 2.0 and\
         i[0] > i[1]:
        out = [20, 100]

    #exemple : plate
    elif abs(i[0] - i[1]) > 0.0 and\
         abs(i[0] - i[1]) < 1.0 and\
         i[0] > i[1]:
        out = [50, 50]

    return out



from training.training import picture_writting
def negativ_training(positive, csv_name, size):
    """We training the negatives data,
    there are all other path expect the current in training."""

    path_data = "../dataset/image/dataset"
    path_folder = "../dataset/image/dataset/{}"
    path_image = "../dataset/image/dataset/{}/{}"

    liste = os.listdir(path_data)
    for i in liste:
        for j in positive:
            if i != j:

                liste1 = os.listdir(path_folder.format(i))

                picture_writting(csv_name,
                                 path_folder.format(i),
                                 "",
                                 size[0], size[1], "0")

