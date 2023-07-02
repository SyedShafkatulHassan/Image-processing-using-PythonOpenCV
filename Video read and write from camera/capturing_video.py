import cv2

capture = cv2.VideoCapture(0)
f = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
v = cv2.VideoWriter('recorded video.mp4', f, 30, (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))))
while True:
    flag, frm = capture.read()
    cv2.imshow('frame', frm)
    key = cv2.waitKey(1)
    v.write(frm)
    if key == ord('c'):
        cv2.destroyAllWindows()
        v.release()
        break