import os
from scraping.object_category import main_scrap
from scraping.download_data import download_picture

def step_three(detection, path_folder_current):
    """ Here we scrap by items detected and
    download them"""

    #scrap
    to_search = [i[0] for i in detection if i[0] != "?"]
    liste = [];
    for i in set(to_search):
        items = main_scrap(i)
        for it in items:
            liste.append(it)

    liste_path = os.listdir(path_folder_current)
    for i in liste:
        for j in liste_path:
            if i == j:
                liste.remove(i)


    #Download
    for i in liste:
        download_picture(i, path_folder_current + str(i))

    return liste
