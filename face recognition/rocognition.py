import os
import cv2
import numpy as np

ppt = ['shafkat', 'ohi']
pa = r'C:\Users\shafkat\OneDrive\Desktop\opencv\face recognition\persons'

hc = cv2.CascadeClassifier('haarcascades.xml')

f = []
l = []

for p in ppt:
        pat= os.path.join(pa, p)
        la = ppt.index(p)

        file_list = os.listdir(pat)
        j = 0
        while j < len(file_list):
            img = file_list[j]
            ip = os.path.join(pat, img)
            ia = cv2.imread(ip)
            g = cv2.cvtColor(ia, cv2.COLOR_BGR2GRAY)
            frr = hc.detectMultiScale(g, scaleFactor=1.2, minNeighbors=5)

            j += 1

            i = 0
            while i < len(frr):
                (a, b, c, d) = frr[i]
                fr = g[b:b+c, a:a+d]
                l.append(la)
                f.append(fr)
                i += 1

f = np.array(f, dtype='object')
l = np.array(l)


face_recognizer = cv2.face.LBPHFaceRecognizer_create()

face_recognizer.train(f, l)
face_recognizer.save('fg')

np.save('f.npy', f)
np.save('l.npy', l)