import cv2
import mediapipe as mp
import time
import keyboard

showsImage = True

def main():
    # OBJECTS:
    cap = cv2.VideoCapture(0)
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()

    # VARIABLES:
    global showsImage

    while not keyboard.is_pressed("esc"):
        success, img = cap.read()
        img = cv2.flip(img, 1)

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        print(results)

        if showsImage:
            cv2.imshow("Image", img)

        windowControl()
        cv2.waitKey(1)


def windowControl():
    global showsImage

    if keyboard.is_pressed("q"):
        if showsImage:
            cv2.destroyWindow("Image")
        showsImage = not showsImage


if __name__ == "__main__":
    main()