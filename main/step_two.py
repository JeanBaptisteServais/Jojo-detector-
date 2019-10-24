"""This is the second step. Here we reading the position
of our crop objects.
Next we try so watch if we have from our model
a dections from our labels.
Finally we display the picture."""


import os
import cv2


#Main function picture
from main_function_image import open_picture
from main_function_image import show_picture
from main_function_image import save_picture

def recup_position(name):
    """We treating positions from position.py"""

    path_position = "../dataset/information_data/current/position.py"
    liste = []; coordinate = []; liste_w = [];increment = "";

    file = open(path_position, "r")
    for lign in file:
        for letter in lign:
            if letter in (";", "\n") : liste.append(increment);increment = "";
            else : increment += letter

    for nb, i in enumerate(liste):
        if nb % 2 == 0 : coordinate.append(liste_w);liste_w = [];
        liste_w.append(i)
    coordinate.append(liste_w)

    for i in coordinate:
        if i != [] and i[1] == name : return i[0]


def recup_label_position(detection):
    """ From the current picture we recuperate
    if yes or no there is a detection for the display
    picture"""

    if detection[0] == "" : detection[0] = "?";
    name = detection[0]; x = 0; y = 0; increment = "";

    for detec in detection[1]:
        for d in detec:
            if d == "," : x = int(increment);increment = "";
            else : increment += d;

    return name, x, int(increment)



def picture_treatment(image, nb, path_current, path_copy):
    """For the display picture we put
    the picture at center and crop
    to the side"""

    b_size = 200; border = cv2.BORDER_CONSTANT;color=(177, 151, 151);

    crop = cv2.resize(open_picture(image), (50, 100))

    if nb == 0 : path = path_current;
    if nb > 0 : path = path_copy;

    image = open_picture(path)

    if nb == 0:
        image = cv2.resize(image, (b_size, b_size))
        image = cv2.copyMakeBorder(image, b_size, b_size, b_size, b_size,
                                    border, value=color)
    return crop, image



def draw(detection, nb, image, path_current, path_copy):
    """We add border to picture, We course the picture,
    if the course is the picture, we passe. In some,
    We verify slot. If a slot's empty c is egal to 0."""

    img1, img = picture_treatment(image, nb, path_current, path_copy)
    name, x, y = recup_label_position(detection)

    for j in range(0, img.shape[0], img1.shape[0]):
        for i in range(0, img.shape[1], img1.shape[1]):
            if j >= 100 and j <= 380 and i >= 100 and i <= 450 : pass
            else:
                bg_pix = 0
                for jj in range(j, j + img1.shape[0]):
                    for ii in range(i, i + img1.shape[1]): 
                        if img[jj, ii][0] != 177 and\
                           img[jj, ii][1] != 151 and\
                           img[jj, ii][2] != 151:
                            bg_pix += 1

                if bg_pix == 0:

                    img[j:j + img1.shape[0], i:i + img1.shape[1]] = img1
                    cv2.line(img, (i+ img1.shape[1], j+ img1.shape[0]),
                             (x + 200, y + 200), (0, 0, 0), 2)
                    cv2.putText(img, name, (i,j+img1.shape[0]),
                                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255))

                    return img


#detection, label
from object_detection.objects_detection import detection
from dataset.information_data.labels_function import read
from dataset.information_data.labels_function import treatment_read

def step_two(path_current, path_copy,
             path_folder_current, path_models, path_label):


    liste_picture = os.listdir(path_folder_current)
    liste_picture.remove("current.jpg")
    model_list = os.listdir(path_models)
    detections = [];images = [];

    for picture in liste_picture:
        image = path_folder_current + str(picture)
        img = open_picture(image)

        for models in model_list:
            labels = read(path_label, str(models))

            for lab in labels:
                _, w, h, l , n = treatment_read([lab])

                try:
                    model = path_models + str(models)
                    prediction = detection(model, w, h, img)
                except:
                    pass

                if prediction == l:
                    detections.append([n, recup_position(image)])
                    images.append(image)
                    break
                else:
                    detections.append(["", recup_position(image)])
                    images.append(image)
                    break

    for nb, i in enumerate(detections):

        if i[1] != None:
            img = draw(i, nb, images[nb], path_current, path_copy)
            show_picture("display", img, 1, "y")
            save_picture(path_copy, img)


    return detections

