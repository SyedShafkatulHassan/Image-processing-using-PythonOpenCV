import cv2
import numpy as np
image = cv2.imread('image.jpg')


change_sized_image = cv2.resize(image, (700, 700))

change_sized_image_t = cv2.inRange(change_sized_image, np.array([60,60,60]), np.array([250,250,250]))

c, p = cv2.findContours(change_sized_image_t, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

change_sized_image_c = cv2.drawContours(change_sized_image, c, -1, (255,0, 255), 3)


if c:
    a = max(c, key=cv2.contourArea)
    print(a)
else:
    print("no")
x,y,width,height=cv2.boundingRect(a)

cv2.rectangle(change_sized_image_c,(x,y),(x+width,y+height),(0,0,255),5)
cv2.imshow('change_sized_image_c', change_sized_image_c)
cv2.waitKey(0)
cv2.destroyAllWindows()