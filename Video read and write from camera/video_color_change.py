import cv2

capture = cv2.VideoCapture(0)

while True:
    flag, frm = capture.read()
    g=cv2.cvtColor(frm,cv2.COLOR_BGR2GRAY)
    print(cv2.CAP_PROP_FPS)
    # for checking frame rate
    cv2.imshow('frame', g) 
    key = cv2.waitKey(1)
    if key == ord('c'):
        cv2.destroyAllWindows()
        break
        