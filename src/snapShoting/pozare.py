import cv2


def Pozare():
    cam = cv2.VideoCapture(0)
    result, image = cam.read()

    if result:

        cv2.imwrite("win.png", image)
