import os
from main_function_image import open_picture
from main_function_image import show_picture
from object_detection.objects_detection import detection
from dataset.information_data.labels_function import read
from dataset.information_data.labels_function import treatment_read



def treat_detection(liste, element):

    if liste == []:return True;
    for i in liste:
        if i == element: return False;

    return True

def step_seven(path_current, path_models, path_label):

    liste_picture = os.listdir(path_current)
    model_list = os.listdir(path_models)
    detections = [];
    liste_picture.remove("current.jpg")
    liste_picture.remove("current_copy.jpg")

    for picture in liste_picture:
        img = open_picture(path_current + str(picture))
 
        for models in model_list:
            model = path_models + str(models)
            labels = read(path_label, str(None))

            for lab in labels:
                information, w, h, _, _ = treatment_read([lab])

                try:
                    print(model)
                    prediction = detection(model, w, h, img)
                    if prediction != 0:
                        print(prediction)
                        add = treat_detection(detections, [models, w, h, path_current + str(picture)])
                        if add is True: detections.append([models, w, h, path_current + str(picture)])

                except ValueError:
                    pass


    print(detections)
    return detections
