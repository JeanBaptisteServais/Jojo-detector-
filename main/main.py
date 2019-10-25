import sys
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\assiette\v2")
from step_one import step_one
from step_two import step_two
from step_three import step_three

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





if __name__ == "__main__":
    
    #step_one(path_folder_current, path_picture, path_position)
    #detections = step_two(path_current, path_copy, path_folder_current,
    #                      path_models, path_label)
    #found = step_three(detections, path_folder_current)
    #step_fourth(objects, path_data, path_folder_format, path_image_format)
