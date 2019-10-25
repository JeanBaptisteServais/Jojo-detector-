def step_seven():

    print("Detection in progress ...")

    path_current = "dataset/image/current/"
    path_models = "training/models/in_training/"
    path_label = "dataset/information_data/label.py"

    liste_picture = os.listdir(path_current)
    model_list = os.listdir(path_models)

    detections = []
    images = []


    for picture in liste_picture:

        if picture != "current.jpg" and\
           picture != "current_copy.jpg":

            image = path_current + str(picture)

            img = open_picture(image)

            for models in model_list:

                model = path_models + str(models)

                labels = read(path_label, str(None))


                for lab in labels:
                    information = treatment_read([lab])

                    w = int(information["dimension"][0])
                    h = int(information["dimension"][1])

                    try:
                        prediction = detection(model, w, h, img)
                        print(models, prediction)
                    except:
                        pass

                    if prediction == 1:
                        detections.append([information["name"], models])
                        images.append(image)

                    else:
                        pass


                    #show_picture("picture", img, 1, "y")


    print(detections)
