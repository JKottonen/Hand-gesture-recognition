import cvzone.HandTrackingModule
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = cvzone.HandTrackingModule.HandDetector(mode=False, maxHands=2, detectionCon=0.1)

fingUp = 0

while True:
    # Get image frame
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Find the hand and its landmarks
    hands, img = detector.findHands(img, True, False)

    if hands:
        hand1 = hands[0]
        fingers1 = detector.fingersUp(hand1)
        if fingers1[0] == 1:
            fingers1[0] = 0
        else: 
            fingers1[0] = 1
        fingUp = sum(fingers1)
    if len(hands) == 2:
        hand2 = hands[1]
        lmList2 = hand2["lmList"]
        dist = (detector.findDistance(lmList2[4], lmList2[8])[0])
        text1 = "KOSKETUS"
        if (dist/10) > 3:
            cv2.putText(img, f'{int(dist/10)}',(lmList2[8]), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        else:
            cv2.circle(img, (lmList2[4]), 25, (255, 0, 0), cv2.FILLED)
        

    
    cv2.putText(img, f'SORMIA: {int(fingUp)}',(400,70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    

    # Display
    cv2.imshow("image", img)
    cv2.waitKey(1)