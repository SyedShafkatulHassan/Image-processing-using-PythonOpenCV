import cv2
import numpy as np
Image = cv2.imread('image1.jpg')
change_sized_image = cv2.resize(Image, (700, 700))

# for selecting height and width I have used change_sized_image.shape[:2]
b=np.zeros(change_sized_image.shape[:2],dtype=np.uint8)

m=cv2.rectangle(b, (244, 244), (444, 444), 255, -1)

m1=cv2.bitwise_and(change_sized_image,change_sized_image,mask=m)

cv2.imshow("",m1)
cv2.waitKey(0)
cv2.destroyAllWindows()
