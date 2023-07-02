

# Author : Syed Shafkatul Hassan
# This code will at first load The Calculator.jpeg then if we give c as
# input it will create another copy of the image we enter any other key as input it will not copy the image

import cv2

Image = cv2.imread('Calculator.jpeg')
cv2.imshow('Image', Image)
cv2.waitKey(0)

key=cv2.waitKey(0)

if key==ord("C"):
   cv2.imwrite('Copyed.jpeg',Image)
   cv2.destroyAllWindows()
else:
   cv2.destroyAllWindows()