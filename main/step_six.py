from main_function_image import define_size
from main_function_image import negativ_training
from training.training import head_writting
from training.training import picture_writting
from training.training import train
from dataset.information_data.labels_function import write_labels
def step_six(liste):

    #Verify csv

    path_data = "dataset/image/dataset"
    path_folder = "dataset/image/dataset/{}"
    path_image = "dataset/image/dataset/{}/{}"
    liste_path = os.listdir(path_data)
    path_label = "dataset/information_data/label.py"


    for i in liste_path:
        print(i)

        picture_folder = os.listdir(path_folder.format(i))

        if len(picture_folder) > 10 and i != "assiette":

            for info_size in liste:
                if info_size[2] == path_folder.format(i):
                    size = define_size(info_size)
                    number_pix = size[0] * size[1]
                    write_labels(path_label, "None", str(i),
                                 "None", str(size[0]), str(size[1]), "None")

            csv_name = "training/csv/in_training/" + str(i) + ".csv"
            model_name = "training/models/in_training/" + str(i)

            head_writting(csv_name, number_pix)

            picture_writting(csv_name,
                             path_folder.format(i),
                             "", 
                             size[0], size[1], "1")

            negativ_training(i, csv_name, size)


            train(csv_name, model_name)

