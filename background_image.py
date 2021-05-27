import cv2
cap = cv2.VideoCapture(0)
# qqqqcap = cv2.VideoCapture('https://192.168.43.1:8080/video')

while cap.isOpened():
    ret, image = cap.read()
    if ret:
        cv2.imshow("image", image)
        if cv2.waitKey(25) == ord('q'):
            # Save the image
            cv2.imwrite('background_image.jpg', image)
            break

cap.release()
cv2.destroyAllWindows()
