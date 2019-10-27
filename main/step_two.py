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

    return name, x, int(increment),



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



def draw_function1(img, j, width, i, height):
    """We verify if there are background pixels"""

    bg_pix = 0;

    for jj in range(j, j + width):
        for ii in range(i, i + height): 
            if img[jj, ii][0] != 177 and\
               img[jj, ii][1] != 151 and\
               img[jj, ii][2] != 151:
                bg_pix += 1

    return bg_pix


def draw_function2(img, img1, i, height, j, width, x, y, name):
    """We put the crop picture on the display picture"""

    font = cv2.FONT_HERSHEY_COMPLEX_SMALL;
    #img[j:j + width, i:i + height] = img1
    cv2.line(img, (i + height, j+ width),
             (x + 200, y + 200), (0, 0, 0), 2)
    cv2.putText(img, name, (i,j+width),
                font, 1, (0, 0, 255))

    return img


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
                bg_pix = draw_function1(img, j, img1.shape[0], i, img1.shape[1])

                if bg_pix == 0:

                    img = draw_function2(img, img1, i, img1.shape[1],
                                         j, img1.shape[0], x, y, name)

                    return img



def predictions(labels, images, detections, models, path_models, image, img):
    """Try to find a detection from the label"""

    for lab in labels:
        _, w, h, l , n = treatment_read([lab])

        try:
            model = path_models + str(models)

            prediction = detection(model, w, h, img)

            if prediction:
                detections.append([n, recup_position(image)])
                images.append(image)
                break
            else:
                detections.append(["", recup_position(image)])
                images.append(image)
                break
        except:
            pass


def liste_treatment(detections):

    #delete None:"" or "":None
    for i in detections:
        if i[1] == None:
            detections.remove(i)
        if i[0] == "" and i[1] == None:
            detections.remove(i)

    #recup position into dico
        #pos = []
    dico = {}
    for i in detections:
        dico[i[1]] = []

    #append item to pos
        #pos = [10, 10]
    for i in detections:
        for key, value in dico.items():
            if i[1] == key:
                value.append(i[0])

    #delete if there are items and ''
        #pos = ['', 10, '']
    for key, value in dico.items():
        delete = False
        for i in value:
            if i != '':
                delete = True
        for i in value:
            if delete is True:
                for i in value:
                    if i == "":
                        value.remove(i)

    #transofr dico into list
    detections = []
    for key, value in dico.items():
        liste_w = []
        for i in value:
            liste_w.append(i)
            liste_w.append(key)
            
            detections.append(liste_w)
            liste_w = []


    return detections



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
            predictions(labels, images, detections, models,
                        path_models, image, img)


    detections = liste_treatment(detections)

    for nb, i in enumerate(detections):

        if i[1] != None:
            #Here
            img = draw(i, nb, images[nb], path_current, path_copy)
            show_picture("display", img, 1, "y")
            save_picture(path_copy, img)
    show_picture("display", img, 0, "y")
    #print(detections)
    return detections

