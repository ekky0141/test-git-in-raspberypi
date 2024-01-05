#https://www.ultimatepython.co/post/face-detection-opencv-python
imagePath = 'football.jpg'
#imagePath = 'face.jpg'

cascPath = "haarcascade_frontalface_default.xml"

import cv2
i=0

faceCascade = cv2.CascadeClassifier(cascPath)
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Mtt colour", image)
#cv2.imshow("Mtt gray", gray)



faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +cascPath)
faces = faceCascade.detectMultiScale(image)


for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    i=i+1
    print(i,x, y)


cv2.imshow("Faces found", image)
cv2.waitKey(0) 


