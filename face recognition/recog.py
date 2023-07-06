import numpy as np
import cv2 

hc = cv2.CascadeClassifier('haarcascades.xml')

ppt = ['shafkat', 'ohi']

fr = cv2.face.LBPHFaceRecognizer_create()
fr.read('fg.yml')

image = cv2.imread(r"C:\Users\shafkat\Downloads\WhatsApp Image 2023-07-07 at 01.56.47.jpeg")

g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

far = hc.detectMultiScale(g, 1.1, 6)

min_confidence = float('inf')
min_person = ''

i = 0
while i < len(far):
    (a, b, c, d) = far[i]
    fac = g[b:b+d, a:a+c]
    label, confidence = fr.predict(fac)
    i += 1

    if confidence < min_confidence:
        min_confidence = confidence
        min_person = ppt[label]

cv2.putText(image, str(min_person), (100, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), thickness=3)

cv2.imshow('', image)

cv2.waitKey(0)
