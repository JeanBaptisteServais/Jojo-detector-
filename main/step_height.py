import sys
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\assiette\v2")

from step_one import step_one
from step_two import step_two
from step_three import step_three
from step_fourth import step_fourth
from step_five import step_five
from step_six import step_six
from step_seven import step_seven
from step_height import step_height

path_folder_current = "../dataset/image/current/"
path_picture = "../dataset/image/current/current.jpg"
path_position = "../dataset/information_data/current/position.py"
path_models = "../training/models/models/"
path_label = "../dataset/information_data/label.py"
path_copy = "../dataset/image/current/current_copy.jpg"
path_current = "../dataset/image/current/current.jpg"
path_data = "../dataset/image/dataset"
path_folder_format = "../dataset/image/dataset/{}"
path_image_format = "../dataset/image/dataset/{}/{}"
path_csv_name = "../training/csv/in_training/{}.csv"
path_model_name = "../training/models/in_training/{}"
path_to_thread = "../ecriture/to_thread.py"
path_models_training = "../training/models/in_training/"
path_csv = "../training/csv/csv"
path_model = "../training/models/models"
path_csv_training = "../training/csv/in_training"

def raise_file_wrote():
    os.remove(path_to_thread)

if __name__ == "__main__":



    #liste = []; length = 0;
    #while len(liste) != length:

    #raise_file_wrote()

    #length = step_one(path_folder_current, path_picture, path_position)

    #detections = step_two(path_current, path_copy, path_folder_current,
    #                      path_models, path_label)

    #found = step_three(detections, path_folder_current)

    #step_fourth(objects, path_data, path_folder_format, path_image_format)

    #dimensions = step_five(path_data)

##    step_six(dimensions, path_data, path_folder_format,
##             path_image_format, path_label, path_csv_name,
##             path_model_name)

    liste = step_seven(path_folder_current, path_models_training, path_label)
    #liste + b

    step_height(liste, path_csv_training, path_csv,
                path_model, path_models_training)






    
