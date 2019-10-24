import os
import cv2
import threading

#Main function picture
from main_function_image import open_picture
from main_function_image import show_picture
from main_function_image import save_picture


#Pictures operations
from picture_operation.background import main_background
from picture_operation.multiple_objects import take_features_multi_obj
from picture_operation.picture_orientation import take_features_position


def to_crop(img):
    """ We recuperate the object from the picture"""

    maxi=0; h=cv2.RETR_EXTERNAL;points=cv2.CHAIN_APPROX_SIMPLE;

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,250,255,cv2.THRESH_BINARY_INV)
    contours, _= cv2.findContours(thresh, h, points)

    for cnt in contours:
        if cv2.contourArea(cnt) > maxi:
            x, y, w, h = cv2.boundingRect(cnt)

    return img[y:y+h, x:x+w], str(int(x+w/2)), str(y)


def write_position(positionx, positiony, name, path):
    """We recuperate the position of the last box.
    for the detection"""

    with open(path, "a") as file:
        file.write(positionx + "," + positiony + ";" + name + "\n")


def step_one(path_folder_current, path_picture, path_position):
    """Here treating entrance picture.
    If there are many objects, we separate them into a new picture.
    For that we need to write them into the current folder from dataset"""

    oInput = input("Enter an image")
    oInput = r"C:\Users\jeanbaptiste\Desktop\assiette\v2\dataset\image\test\assiette1.jpg"

    #Open picture and save it
    img = save_picture(path_picture, open_picture(oInput))

    #Treating background, many objects, position.
    img = save_picture(path_picture, main_background(path_picture))
    img = take_features_multi_obj(path_picture, "")

    #Position objects picture.
    liste = os.listdir(path_folder_current)
    liste.remove("current.jpg"); liste.remove("current_copy.jpg");

    #Make rotation. Write their position. And crop them.
    for i in liste:
        _, posx, posy = to_crop(open_picture(path_folder_current + i))
        write_position(posx, posy, path_folder_current + i, path_position)

        img = take_features_position(path_folder_current + i)
        img, _, _ = to_crop(take_features_position(path_folder_current + i))

        save_picture(str(path_folder_current + i), img)
        show_picture("display", img, 1, "y")
