from training.training import train
from training.training import head_writting
from main_function_image import define_size
from training.training import picture_writting
from main_function_image import negativ_training
from dataset.information_data.labels_function import write_labels



def step_six(liste, path_data, path_folder, path_image, path_label,
             csv_name, model_name):

    no = "None";
    liste_path = os.listdir(path_data)

    #picture folder path
    for i in liste_path:
        picture_folder = os.listdir(path_folder.format(i))

        #less 10 pictures
        if len(picture_folder) > 10 and i != "assiette":
            for info_size in liste:

                #write their dimensions for training
                if info_size[2] == path_folder.format(i):
                    size = define_size(info_size)
                    write_labels(path_label, no, str(i), no,
                                 str(size[0]), str(size[1]),
                                 no)

            #label and pixels descriptions
            head_writting(csv_name.format(i), size[0] * size[1])

            #write picture into csv file
            picture_writting(csv_name.format(i),
                             path_folder.format(i),
                             "", 
                             size[0], size[1], "1")
            #train negatives pictures
            negativ_training(i, csv_name.format(i), size)

            #train
            train(csv_name.format(i), model_name.format(i))

