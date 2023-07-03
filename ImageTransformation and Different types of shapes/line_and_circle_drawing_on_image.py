import cv2

image = cv2.imread('image.jpg')

change_sized_image = cv2.resize(image, (500, 500))

cv2.imshow('change_sized_image',change_sized_image)

Line_Drawn_Image=cv2.line(change_sized_image,(30,50),(300,400),(50,25,50),14)

cv2.imshow('Line_Drawn_Image', Line_Drawn_Image)

circle_drawn_image = cv2.circle(Line_Drawn_Image, (200,200), 100, (50,25,50), 14)

cv2.imshow('circle_drawn_image',circle_drawn_image)

cv2.waitKey(0)
