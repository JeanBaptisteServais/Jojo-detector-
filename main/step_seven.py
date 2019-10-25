import os
from main_function_image import open_picture
from main_function_image import show_picture
from object_detection.objects_detection import detection
from dataset.information_data.labels_function import read
from dataset.information_data.labels_function import treatment_read


def step_seven(path_current, path_models, path_label):

    liste_picture = os.listdir(path_current)
    model_list = os.listdir(path_models)
    detections = []; images = [];
    liste_picture.remove("current.jpg")
    liste_picture.remove("current_copy.jpg")


    for picture in liste_picture:
        img = open_picture(path_current + str(picture))

        for models in model_list:
            model = path_models + str(models)
            labels = read(path_label, str(None))

            for lab in labels:
                information, w, h = treatment_read([lab])

                try:
                    prediction = detection(model, w, h, img)
                    print(models, prediction)

                    if prediction == 1:
                        detections.append([information["name"], models])
                        images.append(image)

                except ValueError:
                    pass

                show_picture("picture", img, 0, "y")


    print(detections)
    return detections
