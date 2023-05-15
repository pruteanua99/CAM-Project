import cv2


class snapshot:
    def __init__(self):
        pass

    def Pozare(self):
        cam = cv2.VideoCapture(0)
        result, image = cam.read()

        if result:

            cv2.imwrite("win.png", image)
