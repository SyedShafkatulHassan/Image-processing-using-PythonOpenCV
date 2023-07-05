import cv2
Image = cv2.imread('image.jpg')
change_sized_image = cv2.resize(Image, (700, 700))
cv2.imshow('image', change_sized_image)

avg=cv2.blur(change_sized_image,(5,5))

cv2.imshow('avg blur', avg)

cv2.waitKey(0)
