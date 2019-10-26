import sys
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\assiette\v2")

import os
import csv

from training.training import csv_to_list
from training.training import training
from training.training import train


def last_csv(liste_csv, path_csv):

    liste_w = []
    for i in liste_csv:
        if i == '.~lock.2.csv#':pass
        else:
            liste_w.append(len(i))
    maxi = max(liste_w)

    liste_w2 = []
    for i in liste_csv:
        if len(i) == maxi:
            liste_w2.append(i)

    labeled = []
    to_read = path_csv + "/" + str(max(liste_w2))

    f =  open(to_read, 'r')
    dataframe = f.readlines()
    dataframe = dataframe
    for i in dataframe:
        try:
            labeled.append(int(i[0]))
        except:
            pass

    labeled = max(list(set(labeled)))

    return labeled, to_read





def step_height(liste, path_csv_training, path_csv,
                path_model_training, path_model):

    name = list(set([i[0] for i in liste]))

    liste_training_csv = os.listdir(path_csv_training)
    liste_csv = os.listdir(path_csv)

    liste_model_training = os.listdir(path_model_training)
    liste_model = os.listdir(path_model)

    labeled, to_read = last_csv(liste_csv, path_csv)
    label = labeled + 1


    to_change = []
    for i in name:
        for csv in liste_training_csv:
            if str(i) + ".csv" == str(csv):
                to_change.append(csv)

    for i in to_change:
        path = path_csv_training + "/" + str(i)
        main = open(to_read, 'a')

        f =  open(path, 'r')
        dataframe = f.readlines()
        dataframe = dataframe

        for j in dataframe:
            ok = False
            if j[0] == "1":
                j = j.split(";")
                j[0] = str(label)
                for k in j[:-1]:
                    main.write(str(k)+";")
                ok = True
            if ok is True:
                main.write("\n")
        label += 1


    X, y = csv_to_list(to_read)
    training(X, Y, to_read)
