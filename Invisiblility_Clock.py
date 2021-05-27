import cv2
import numpy as np

cap = cv2.VideoCapture(0)

background_image = cv2.imread('background_image.jpg')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # convert to hsv (refer internet)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Range of red is found (Differ in each package like cv2)
        # [H-10, 100, 100] and [H+10, 255, 255]
        l_red = np.array([0, 100, 100])
        u_red = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, l_red, u_red)
        # cv2.imshow('mask', mask) # displays red as white and others black
        part1 = cv2.bitwise_and(background_image, background_image, mask=mask)

        mask = cv2.bitwise_not(mask)

        part2 = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('final', part1 + part2)

        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
