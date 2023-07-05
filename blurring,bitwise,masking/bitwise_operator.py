import cv2
import numpy as np

r = cv2.rectangle(np.zeros((500, 500), dtype=np.uint8), (50, 50), (420, 430), 255,-1)
img=np.zeros((500, 500), dtype=np.uint8)
c = cv2.circle(img, (250, 250), 200,255,-1)

b_xor=cv2.bitwise_xor(r,c)
b_not=cv2.bitwise_not(r,c)
b_or=cv2.bitwise_or(r,c)
b_and=cv2.bitwise_and(r,c)

cv2.imshow("", b_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
