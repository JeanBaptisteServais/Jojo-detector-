import os

import sys
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\assiette\v2")

from training.training import head_writting
from training.training import picture_writting
from training.training import train
from ecriture.write import writtte
import importlib


def step_five(path_data):
    """Here we want recup dimension of pictures.
    For that we go on the dataset picture folder.
    We run all of the picture folder,
    recup x and y pixels convert to cm.
    For that we call write who run a thread"""

    liste_path = os.listdir(path_data)

    write = writtte(len(liste_path))

    if write:

        from ecriture.to_thread import main_threading
        liste = main_threading()


    return liste
