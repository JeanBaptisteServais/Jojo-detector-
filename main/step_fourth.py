import os

import sys
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\assiette\v2")

from picture_operation.delete import main_deleting
from picture_operation.background import main_background
from picture_operation.multiple_objects import take_features_multi_obj
from picture_operation.picture_orientation import take_features_position


def step_fourth(objects, path_data, path_folder, path_image):
    """Background, separate many objects,
    make position rotation, delete false picture
    TO INCREASE"""

    liste_path = os.listdir(path_data)

    for i in liste_path:

        picture_folder = os.listdir(path_folder.format(i))

        for j in picture_folder:
            image = path_image.format(i, j)
            save_picture(image, main_background(image))

        for j in picture_folder:
            image = path_image.format(i, j)
            img = take_features_multi_obj(image)

        for j in picture_folder:
            image = path_image.format(i, j)
            save_picture(image, take_features_position(image))


        for j in picture_folder:
            image = path_image.format(i, j)
            delete = main_deleting(image)
            if delete is True:
                os.remove(image)
