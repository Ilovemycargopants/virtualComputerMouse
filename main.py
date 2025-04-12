import cv2


#Opens the camera
cap = cv2.VideoCapture(1)

#keep going until
while True:
    #ignore first value it checks if connection was good (ret), record frame telling us sucessfull connection
    _, frame = cap.read()
    #name window, what am i showing
    cv2.imshow("Virtual Mouse",frame)
    cv2.waitKey(1)
