
# This code will at first load The video from the camera and show it to the screen then if we give c as
# input it will stop presenting video

import cv2

capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture(0)
while True:
    flag, frm = capture.read()
    cv2.imshow('frame', frm)
    key = cv2.waitKey(1)
    if key == ord('c'):
        cv2.destroyAllWindows()
        break
        