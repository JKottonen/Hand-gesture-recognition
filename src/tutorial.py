from platform import system
import cv2
import mediapipe as mp
import time
import keyboard

# GLOBAL OBJECTS:
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils

# GLOBAL VARIABLES:
running = True
showsImage = True
mirroredImage = True
showFps = True

pTime = 0

def main():
    """
    Runs mainloop
    """
    hands = mpHands.Hands()

    # FRAME UPDATE LOOP:
    while running:
        img = captureImage()

        findHands(img, hands)
    
        FPScounter(img)

        showImage(img)

        keyboardListener()


    # If update loop somehow breaks, the program exits
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


def findHands(img, hands):
    """Finds hands and draws the landmarks on the image"""

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):

                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)

                if id == 0:
                    cv2.circle(img, (cx, cy), 25, (255, 0, 0), cv2.FILLED)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


def keyboardListener():
    """Handles keyboard input"""

    if keyboard.is_pressed("esc"):
        exit()

    if keyboard.is_pressed("down"):
        windowControls("show")

    if keyboard.is_pressed("up"):
        windowControls("mirror")

    if keyboard.is_pressed("f"):
        windowControls("fps")


def windowControls(case):
    """Switches window visibility, mirroring and FPS counter"""

    global showsImage
    global mirroredImage
    global showFps

    if case == "show":
        if showsImage:
            cv2.destroyWindow("Image")
        showsImage = not showsImage
    
    if case == "mirror":
        mirroredImage = not mirroredImage
    
    if case == "fps":
        showFps = not showFps


def FPScounter(img):
    if showFps:
        global pTime

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}',(10,70), cv2.FONT_HERSHEY_SIMPLEX, 1,
        (0,255,0), 2)


if __name__ == "__main__":
    main()