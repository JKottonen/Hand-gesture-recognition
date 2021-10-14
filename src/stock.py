import cvzone.HandTrackingModule
import cv2
import keyboard

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = cvzone.HandTrackingModule.HandDetector(mode=False, maxHands=2, detectionCon=0.1)

def screenText(img, text, coordinate):
    """
    :param img: image
    :param text: Text to display
    :param coordinate: Bottom left coordinates of the text
    :example: screenText(img, f'SORMIA: {int(666)}',(400,70))
    """
    cv2.putText(img, text, coordinate, cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

def main():
    """
    main-loop goes on until esc is pressed
    """
    while not keyboard.is_pressed('esc'):

        # Get image frame
        success, img = cap.read()
        img = cv2.flip(img, 1)       

        # Find the hands and their landmarks
        hands, img = detector.findHands(img, True, False)

        # Display
        cv2.imshow("image", img)
        cv2.waitKey(1)



if __name__ == "__main__":
    main()