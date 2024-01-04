imagePath = 'football.jpg'
import cv2 as cv
img =cv.imread(imagePath)
cv.imshow('FOOTBALL' ,img)
cv.waitKey(0)
cv.destroyAllWindows()
