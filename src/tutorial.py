from platform import system
import cv2
import mediapipe as mp
import time
import keyboard

# GLOBAL OBJECTS:
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()

# GLOBAL VARIABLES:
running = True
showsImage = True
mirroredImage = True

def main():
    """
    Runs mainloop
    """
    # FRAME UPDATE LOOP:
    while running:
        img = captureImage()

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        print(results.multi_hand_landmarks)

        showImage(img)

        keyboardListener()

    exit()

def captureImage():
    """Captures a frame from webcam"""

    success, img = cap.read()
    if mirroredImage:
        img = cv2.flip(img, 1)
    return img

def showImage(img):
    """Projects the current image on the window"""

    if showsImage:
        cv2.imshow("Image", img)
    cv2.waitKey(1)

def keyboardListener():
    """Handles keyboard input"""

    if keyboard.is_pressed("esc"):
        exit()

    if keyboard.is_pressed("q"):
        windowSwitch()
    

def windowSwitch():
    """Switches window on and off"""
    global showsImage

    if showsImage:
        cv2.destroyWindow("Image")
    showsImage = not showsImage



if __name__ == "__main__":
    main()