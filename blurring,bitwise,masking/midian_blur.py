import cv2
Image = cv2.imread('image.jpg')
change_sized_image = cv2.resize(Image, (700, 700))
cv2.imshow('image', change_sized_image)

m=cv2.medianBlur(change_sized_image,5)

cv2.imshow('median blur', m)

cv2.waitKey(0)
