import sys
from step_one import step_one
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\assiette\v2")

path_folder_current = "../dataset/image/current/"
path_picture = "../dataset/image/current/current.jpg"
path_position = "../dataset/information_data/current/position.py"

if __name__ == "__main__":
    
    step_one(path_folder_current, path_picture, path_position)
