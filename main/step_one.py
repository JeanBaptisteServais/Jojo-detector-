import os
import threading

#Main function picture
from main_function_image import to_crop
from main_function_image import open_picture
from main_function_image import show_picture
from main_function_image import save_picture
from main_function_image import write_position

#Pictures operations
from picture_operation.background import main_background
from picture_operation.multiple_objects import take_features_multi_obj
from picture_operation.picture_orientation import take_features_position


def step_one():
    """Here treating entrance picture.
    If there are many objects, we separate them into a new picture.
    For that we need to write them into the current folder from dataset"""


    path_folder_current = "../dataset/image/current/"
    path_picture = "../dataset/image/current/current.jpg"
    path_position = "../dataset/information_data/current/position.py"
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


step_one()
