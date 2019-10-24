import os
import cv2
import time
import numpy as np

def open_picture(image):
    """We open picture"""
    img = cv2.imread(image)
    return img

def show_picture(name, image, mode, destroy):
    """Show picture"""
    
    cv2.imshow(name, image)
    cv2.waitKey(mode)
    if mode == 1:
        time.sleep(1)
        cv2.destroyAllWindows()
    if destroy == "y":
        cv2.destroyAllWindows()

def save_picture(name, picture):
    """saving picture"""
    cv2.imwrite(name, picture)

def blanck_picture(img):
    """ Create a black picture"""
    blank_image = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
    blank_image[0:, 0:] = 0, 0, 0
    return blank_image

def to_crop(img):
    """ We recuperate the object from the picture"""

    maxi=0; h=cv2.RETR_EXTERNAL;points=cv2.CHAIN_APPROX_SIMPLE;

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,250,255,cv2.THRESH_BINARY_INV)
    contours, _= cv2.findContours(thresh, h, points)

    for cnt in contours:
        if cv2.contourArea(cnt) > maxi:
            maxi = cv2.contourArea(cnt)
            x, y, w, h = cv2.boundingRect(cnt)

    return img[y:y+h, x:x+w], str(int(x+w/2)), str(y)


def write_position(positionx, positiony, name, path):
    """We recuperate the position of the last box.
    for the detection"""

    with open(path, "a") as file:
        file.write(positionx + "," + positiony + ";" + name + "\n")


def recup_position(name):
    """We treating positions from position.py"""

    path = "dataset/information_data/current/position.py"
    liste = []; coordinate = []; liste_w = [];

    with open(path, "r") as file:
        for i in file:
            increment = ""

            #If caractere is ; or a jump we add increment
            for j in i:
                if j == ";" or j == "\n":
                    liste.append(increment)
                    increment = ""
                else:
                    increment += j

    #We recuperate informations: coordinates and name of picture
    for nb, i in enumerate(liste):
        if nb % 2 == 0:
            coordinate.append(liste_w)
            liste_w = []

        liste_w.append(i)

    coordinate.append(liste_w)

    for i in coordinate:
        if i != []:
            if i[1] == name:
                return i[0]



def recup_label_position(detection):
    """ From the current picture we recuperate
    if yes or no there is a detection for the display
    picture"""

    #no detection put '?'
    if detection[0] == "": detection[0] = "?";

    name = detection[0]; x = 0; y = 0; increment = "";

    for detec in detection[1]:
        for d in detec:
            if d == ",":
                x = int(increment)
                increment = ""
            else:
                increment += d

    y = int(increment)

    return name, x, y



def picture_treatment(image, nb):
    """For the display picture we put
    the picture at center and crop
    to the side"""

    img1 = open_picture(image)
    img1 = cv2.resize(img1, (50, 100))

    if nb == 0:path = "dataset/image/current/current.jpg";
    if nb > 0:path = "dataset/image/current/current_copy.jpg";

    img = open_picture(path)

    if nb == 0:
        img = cv2.resize(img, (200, 200))
        img = cv2.copyMakeBorder(img, 200, 200, 200, 200,
                                 cv2.BORDER_CONSTANT,
                                 value=(177, 151, 151))
    return img1, img




def draw(detection, nb, image):
    """We add border to picture, We course the picture,
    if the course is the picture, we passe. In some,
    We verify slot. If a slot's empty c is egal to 0."""

    img1, img = picture_treatment(image, nb)
    name, x, y = recup_label_position(detection)

    for j in range(0, img.shape[0], img1.shape[0]):
        for i in range(0, img.shape[1], img1.shape[1]):
            if j >= 100 and j <= 380 and i >= 100 and i <= 450:
                pass
            else:
                c = 0
                for jj in range(j, j + img1.shape[0]):
                    for ii in range(i, i + img1.shape[1]): 
                        if img[jj, ii][0] != 177 and\
                           img[jj, ii][1] != 151 and\
                           img[jj, ii][2] != 151:
                            c += 1

                if c == 0:

                    img[j:j + img1.shape[0], i:i + img1.shape[1]] = img1
                    cv2.line(img, (i+ img1.shape[1], j+ img1.shape[0]),
                             (x + 200, y + 200), (0, 0, 0), 2)
                    cv2.putText(img, name, (i,j+img1.shape[0]),
                                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255))

                    return img



def define_size(i):
    """Here we define the dimension for the training
    after have course dimension of picture"""

    out = "";

    #exemple : spoon
    if abs(i[0] - i[1]) > 3.0 and\
       i[0] > i[1]:
        out = [100,200]

    #exemple : plate
    elif abs(i[0] - i[1]) > 2.0 and\
         abs(i[0] - i[1]) < 3.0 and\
         i[0] > i[1]:
        out = [50, 50]

    #exemple : bol
    elif abs(i[0] - i[1]) > 1.0 and\
         abs(i[0] - i[1]) < 2.0 and\
         i[0] > i[1]:
        out = [50, 100]

    #exemple : plate
    elif abs(i[0] - i[1]) > 0.0 and\
         abs(i[0] - i[1]) < 1.0 and\
         i[0] > i[1]:
        out = [50, 50]

    return out



from training.training import picture_writting
def negativ_training(positive, csv_name, size):
    """We training the negatives data,
    there are all other path expect the current in training."""

    path_data = "dataset/image/dataset"
    path_folder = "dataset/image/dataset/{}"
    path_image = "dataset/image/dataset/{}/{}"

    liste = os.listdir(path_data)
    for i in liste:
        if i != positive:
            liste1 = os.listdir(path_folder.format(i))

            picture_writting(csv_name,
                             path_folder.format(i),
                             "",
                             size[0], size[1], "0")
